# -*- coding: utf-8 -*-

import re
import os
import codecs
import json

from pprint import pprint
from markdown import markdown

from docutils import nodes
from docutils.parsers.rst import Directive, directives
from sphinx import addnodes
from sphinx.roles import XRefRole
from sphinx.locale import _
from sphinx.domains import Domain, ObjType, Index
from sphinx.directives import ObjectDescription
from sphinx.util import logging
from sphinx.util.nodes import make_refnode
from sphinx.util.docfields import Field, GroupedField, TypedField
from sphinx.environment import BuildEnvironment
from sphinx.builders import Builder
from typing import Any, Dict, Iterable, Iterator, List, Tuple, Optional, Union
from collections import defaultdict


sig_re = re.compile(r'''^(\w+)\s*\((.*)\)$''', re.VERBOSE)

def _pseudo_parse_arglist(sig_node: addnodes.desc_signature, arg_list: str):
    param_list = addnodes.desc_parameterlist()
    stack = [param_list]

    processed_args_list = []
    try:
        for argument in arg_list.split(','):
            argument = argument.strip()
            ends_open = ends_close = 0
            while argument.startswith('['):
                stack.append(addnodes.desc_optional())
                stack[-2] += stack[-1]
                argument = argument[1:].strip()
            while argument.startswith(']'):
                stack.pop()
                argument = argument[1:].strip()
            while argument.endswith(']') and not argument.endswith('[]'):
                ends_close += 1
                argument = argument[:-1].strip()
            while argument.endswith('['):
                ends_open += 1
                argument = argument[:-1].strip()
            if argument:
                stack[-1] += addnodes.desc_parameter(argument, argument)
                processed_args_list.append({ "name" : argument })

                if ends_close > 0:
                    processed_args_list[-1]["optional"] = True
            while ends_open:
                stack.append(addnodes.desc_optional())
                stack[-2] += stack[-1]
                ends_open -= 1
            while ends_close:
                stack.pop()
                ends_close -= 1
        if len(stack) != 1:
            raise IndexError
    except IndexError:
        # if there are too few or too many elements on the stack, just give up
        # and treat the whole argument list as one argument, discarding the
        # already partially populated paramlist node
        sig_node += addnodes.desc_parameterlist()
        sig_node[-1] += addnodes.desc_parameter(arg_list, arg_list)
    finally:
        sig_node += param_list

    return processed_args_list

def preprocess_doc(val):
    val = val.strip()
    val = val.replace(':qcs:function:', "")
    val = val.replace(':qcs:type:', "")
    val = val.replace(':qcs:enum:', "")
    val = val.replace(':qcs:series:', "")
    val = val.replace('For example:', "")
    val = val.replace(':code:', "")

    return markdown(val)[3:-4]

def get_arg(signature, arg_name, allowNew):
    for arg in signature["args"]:
        if arg["name"] == arg_name:
            return arg

    if allowNew:
        signature["args"].append({ "name": arg_name })
        return signature["args"][-1]

    return None

def build_lines_list(content):
    currentLine = ""
    linesList = []
        
    for contentLine in content:
        if len(contentLine) == 0:
            if len(currentLine) > 0:
                linesList.append(currentLine)
            currentLine = ""
        elif len(currentLine) > 0 and contentLine.startswith(':'):
            linesList.append(currentLine)
            currentLine = contentLine
        else:
            if len(currentLine) > 0:
                currentLine = currentLine + " " + contentLine
            else:
                currentLine = contentLine

    if len(currentLine) > 0:
        linesList.append(currentLine)

    return linesList


class QCSFunction(ObjectDescription):

    option_spec = {
        'category': directives.unchanged_required,
        'has_table_overload': directives.flag,
        'table_call': directives.flag
    }

    doc_field_types = [
        TypedField('parameter', label=_('Parameters'),
                      names=('param', 'parameter', 'arg', 'argument'),
                      typerolename='class', typenames=('paramtype', 'type'),
                      can_collapse=False),
        Field('returnvalue', label=_('Returns'), has_arg=False,
              names=('returns', 'return'))
    ]
    
    allow_nesting = False

    known_signatures_postfix = {}

    def register_signature(self, name, sig):  
        if not name in self.known_signatures_postfix:
            self.known_signatures_postfix[name] = {}
            self.known_signatures_postfix[name][sig] = ''
        else:
            self.known_signatures_postfix[name][sig] = "_{}".format(len(self.known_signatures_postfix[name]) + 1)

    def handle_signature(self, sig: str, sig_node: addnodes.desc_signature) -> str:    
        self.input_sig = sig
        self.table_call = "table_call" in self.options

        if self.table_call:
            print(re.search(r'([A-Za-z_-]+)\b', sig).group(1))
            self.obj_name = re.search(r'([A-Za-z_-]+)\b', sig).group(1)
            self.register_signature(self.obj_name, sig)

            sig_node += addnodes.desc_name(sig, sig)
        else:
            m = sig_re.match(sig)

            if m is None:
                raise ValueError

            name, arg_list = m.groups()

            if name is None:
                raise ValueError

            self.register_signature(name, sig)

            sig_node += addnodes.desc_name(name, name)

            self.parsed_args = _pseudo_parse_arglist(sig_node, arg_list)
            self.obj_name = name

        if "has_table_overload" in self.options:
            sig_node += addnodes.desc_optional("has-table-overload", "has-table-overload")

        if self.table_call:
            sig_node += addnodes.desc_optional("table_call", "table_call")

        return sig

    def after_content(self):
        linesList = build_lines_list(self.content)

        qcs_domain = self.env.get_domain('qcs')

        name = self.obj_name if hasattr(self, "obj_name") else self.input_sig
        
        function_doc = {
            "type": "function",
            "name": name,
            "signatures": []
        }

        if name in qcs_domain.data["api_doc"]["functions"]:
            function_doc = qcs_domain.data["api_doc"]["functions"][name]
        else:
            qcs_domain.data["api_doc"]["functions"][name] = function_doc
        
        if "category" in self.options:
            function_doc["category"] = self.options["category"]

        signature = {
            "args": self.parsed_args if hasattr(self, "parsed_args") else []
        }

        if "has_table_overload" in self.options:
            signature["has_table_overload"] = True

        if self.table_call:
            signature["table_call"] = True

        for line in linesList:
            if line.startswith(":returns:"):
                signature["returns"] = preprocess_doc(line[len(":returns:"):])
            elif line.startswith(":param "):
                param_start = len(":param ")
                param_end = line.find(":", param_start)
                param_name = line[param_start:param_end]
                
                arg = get_arg(signature, param_name, self.table_call)

                if arg:
                    arg["description"] = preprocess_doc(line[(param_end + 1):])
            elif line.startswith(":type "):
                type_start = len(":type ")
                type_end = line.find(":", type_start)
                param_name = line[type_start:type_end]
                
                arg = get_arg(signature, param_name, self.table_call)

                if arg:
                    arg["type"] = preprocess_doc(line[(type_end + 1):])
            else:
                function_doc["description"] = preprocess_doc(line)
                break

        function_doc["signatures"].append(signature)


    def add_target_and_index(self, name_cls: str, sig: str, sig_node: addnodes.desc_signature) -> None:
        category = self.options.get("category", "default")
        
        target_name = '{}.{}{}'.format('qcs.fn', self.obj_name, self.known_signatures_postfix[self.obj_name][sig])

        print("Adding {} to category {} as {}".format(sig, category, target_name))
        
        qcs_domain = self.env.get_domain('qcs')
        qcs_domain.add_function(target_name, sig, category)

        sig_node['names'].append(target_name)
        sig_node['ids'].append(target_name)
        sig_node['first'] = (not self.names)

        self.state.document.note_explicit_target(sig_node)

        self.indexnode['entries'].append(('single', "{} ({})".format(sig, category), sig, '', None))


class QCSEnum(ObjectDescription):
    doc_field_types = [
            Field('description', label=_('Description'), names=('description'), has_arg=False),
            GroupedField('item', label=_('Enum Items'), names=('item', 'item'), can_collapse=False),
        ]
    
    allow_nesting = False

    def handle_signature(self, sig: str, sig_node: addnodes.desc_signature) -> str: 
        sig_node += addnodes.desc_name(sig, sig)
        self.obj_name = sig
        return sig

    def after_content(self):
        enum_doc = {
            "type": "enum",
            "name": self.obj_name,
            "items": []
        }

        linesList = build_lines_list(self.content)

        for line in linesList:
            if line.startswith(":description:"):
                enum_doc["description"] = preprocess_doc(line[len(":description:"):])
            elif line.startswith(":item "):
                item_start = len(":item ")
                item_end = line.find(":", item_start)
                item_name = line[item_start:item_end]
                
                item = {
                    "name": item_name,
                    "description": preprocess_doc(line[(item_end + 1):])
                }

                enum_doc["items"].append(item)

        qcs_domain = self.env.get_domain('qcs')
        qcs_domain.data["api_doc"]["enums"][self.obj_name] = enum_doc


    def add_target_and_index(self, name_cls: str, sig: str, sig_node: addnodes.desc_signature) -> None:
        qcs_domain = self.env.get_domain('qcs')
        qcs_domain.add_enum(sig)

        target_name = "qcs.enum.{}".format(sig)

        sig_node['names'].append(target_name)
        sig_node['ids'].append(target_name)
        sig_node['first'] = (not self.names)

        self.state.document.note_explicit_target(sig_node)

class QCSType(ObjectDescription):
    allow_nesting = False

    def handle_signature(self, sig: str, sig_node: addnodes.desc_signature) -> str:
        sig_node += addnodes.desc_name(sig, sig)
        self.obj_name = sig
        return sig

    def after_content(self):
        type_doc = {
            "type": "type",
            "name": self.obj_name
        }

        linesList = build_lines_list(self.content)

        if len (linesList) > 0:
            type_doc["description"] = preprocess_doc(linesList[0])

        qcs_domain = self.env.get_domain('qcs')
        qcs_domain.data["api_doc"]["types"][self.obj_name] = type_doc


    def add_target_and_index(self, name_cls: str, sig: str, sig_node: addnodes.desc_signature) -> None:
        qcs_domain = self.env.get_domain('qcs')
        qcs_domain.add_type(sig)

        target_name = "qcs.type.{}".format(sig)

        sig_node['names'].append(target_name)
        sig_node['ids'].append(target_name)
        sig_node['first'] = (not self.names)

        self.state.document.note_explicit_target(sig_node)

class QCSConstant(ObjectDescription):
    allow_nesting = False

    def handle_signature(self, sig: str, sig_node: addnodes.desc_signature) -> str:
        sig_node += addnodes.desc_name(sig, sig)
        self.obj_name = sig
        return sig

    def after_content(self):
        constant_doc = {
            "type": "constant",
            "name": self.obj_name
        }

        linesList = build_lines_list(self.content)

        if len (linesList) > 0:
            constant_doc["description"] = preprocess_doc(linesList[0])

        qcs_domain = self.env.get_domain('qcs')
        qcs_domain.data["api_doc"]["constants"][self.obj_name] = constant_doc


    def add_target_and_index(self, name_cls: str, sig: str, sig_node: addnodes.desc_signature) -> None:
        qcs_domain = self.env.get_domain('qcs')
        qcs_domain.add_constant(sig)

        target_name = "qcs.constant.{}".format(sig)

        sig_node['names'].append(target_name)
        sig_node['ids'].append(target_name)
        sig_node['first'] = (not self.names)

        self.state.document.note_explicit_target(sig_node)

        
class QCSSeries(ObjectDescription):

    option_spec = {
        'overlayable': directives.flag
    }

    allow_nesting = False

    def handle_signature(self, sig: str, sig_node: addnodes.desc_signature) -> str:
        sig_node += addnodes.desc_name(sig, sig)

        if 'overlayable' in self.options:
            sig_node += addnodes.desc_annotation('overlayable', '\toverlayable')

        self.obj_name = sig

        return sig

    def after_content(self):
        series_doc = {
            "type": "series",
            "name": self.obj_name
        }

        linesList = build_lines_list(self.content)

        for line in linesList:
            if line.startswith(":overlayable:"):
                series_doc["overlayable"] = True
            else:
                series_doc["description"] = preprocess_doc(line)
                break

        qcs_domain = self.env.get_domain('qcs')
        qcs_domain.data["api_doc"]["series"][self.obj_name] = series_doc


    def add_target_and_index(self, name_cls: str, sig: str, sig_node: addnodes.desc_signature) -> None:
        qcs_domain = self.env.get_domain('qcs')
        qcs_domain.add_series(sig)

        target_name = "qcs.series.{}".format(sig)

        sig_node['names'].append(target_name)
        sig_node['ids'].append(target_name)
        sig_node['first'] = (not self.names)

        self.state.document.note_explicit_target(sig_node)


class QCSIndex(Index):
    name = 'qcs'
    localname = _('QCS Language Reference')
    shortname = _('QCS')

    def generate(self, docnames=None):
        content = defaultdict(list)

        objects = self.domain.get_objects()
        objects = sorted(objects, key=lambda obj: obj[0])

        for name, dispname, typ, docname, anchor, _ in objects:
            #[name, subtype, docname, anchor, extra, qualifier, descr]
            content[typ].append(
                (dispname, 0, docname, anchor, '', '', ''))

        # convert the dict to the sorted list of tuples expected
        content = sorted(content.items())

        # Dump apidoc_en
         
        apidoc = []

        def process_docs(type_key):
            docs = self.domain.data["api_doc"][type_key]

            for key in docs:
                apidoc.append(docs[key])


        process_docs("functions")
        process_docs("enums")
        process_docs("constants")
        process_docs("series")

        pprint(self.domain.env.srcdir)

        outfilename = os.path.join(self.domain.env.srcdir, "..", "apidoc_en.json")

        try:
            f = codecs.open(outfilename, 'w', 'utf-8')

            try:
                f.write(json.dumps(apidoc, indent=2))
            finally:
                f.close()
        except (IOError, OSError) as err:
            print("error writing file %s: %s" % (outfilename, err))

        return content, True

class QCSDomain(Domain):
    name = 'qcs'
    label = _('Quadcode Script')

    roles = {
        'function': XRefRole(),
        'type': XRefRole(),
        'enum': XRefRole(),
        'constant': XRefRole(),
        'series': XRefRole(),
    }

    directives = {
        'function': QCSFunction,
        'type': QCSType, 
        'enum': QCSEnum,
        'constant': QCSConstant,
        'series': QCSSeries,
    }

    indices = [
        QCSIndex
    ]

    initial_data = {
        "types": [],
        "functions": [],
        "api_doc": {
            "functions":{},
            "enums": {},
            "types": {},
            "constants": {},
            "series": {}
        }
    }

    data_version = 18

    def _find_reference(self, objects_list, target):
        for name, dispname, typ, docname, anchor, _ in objects_list:
            if dispname.startswith(target):
                return name, docname, anchor
            
        return None

    def resolve_xref(self, env: BuildEnvironment, from_doc_name: str, builder: Builder,
                    type: str, target: str, node: nodes.Element, cont_node: nodes.Node)-> Optional[nodes.Node]:
        target_object = None

        if type == "type" or type == "enum":
            target_object = self._find_reference(self.data["types"], target)
        elif type == "function":
            target_object = self._find_reference(self.data["functions"], target)

        if target_object is None:
            print('resolve_xref failed {} {} {}'.format(from_doc_name, type, target))
            return None

        return make_refnode(builder, from_doc_name, target_object[1], target_object[0], cont_node)


    def get_objects(self) -> Iterator[Tuple[str, str, str, str, str, int]]:
        for obj in self.data["types"]:
            yield(obj)

        for obj in self.data["functions"]:
            yield(obj)


    def get_full_qualified_name(self, node: nodes.Element) -> Optional[str]:
        return '{}.{}'.format('qcs', node.arguments[0])


    def add_function(self, name: str, sig: str, category: str) -> None:
        self.data["functions"].append ((name, sig, "Functions ({})".format(category), self.env.docname, name, 0))

    def add_type(self, sig: str) -> None:
        print("Adding type `%s`" % sig)
        name = '{}.{}'.format('qcs.type', sig)
        
        self.data["types"].append ((name, sig, 'Types', self.env.docname, name, 0))

    def add_enum(self, sig: str) -> None:
        print("Adding enum `%s`" % sig)
        name = '{}.{}'.format('qcs.enum', sig)
        
        self.data["types"].append ((name, sig, 'Enums', self.env.docname, name, 0))

    def add_constant(self, sig: str) -> None:
        print("Adding constant `%s`" % sig)
        name = '{}.{}'.format('qcs.constant', sig)
        
        self.data["types"].append ((name, sig, 'Constants', self.env.docname, name, 0))

    def add_series(self, sig: str) -> None:
        print("Adding series `%s`" % sig)
        name = '{}.{}'.format('qcs.series', sig)
        
        self.data["types"].append ((name, sig, 'Constants', self.env.docname, name, 0))

def setup(app):
    print("QCS Domain created")
    app.add_domain(QCSDomain)

    return {
        'version': '1.0'
    }

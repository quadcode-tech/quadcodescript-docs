input_group
===========

.. qcs:function:: input_group { name="", description="", inputs... }
    :category: input
    :table_call:

    :param name: Name of the input input group. :code:`name=` can be omitted.
    :type name: :qcs:type:`string`

    :param description: Description for the input group.
    :type description: :qcs:type:`string`

    :param inputs: List of inputs. See below.

    **input_group** allows to implicitly create the group of :qcs:function:`input`. 
    Depending on the type of inputs and on the platforms - the way the inputs are 
    displayed varies.

    .. image:: /_static/input_groups.png

    **Example:**

    .. code-block::

        input_group {
            "Line",
            color = input { default = "#56CEFF", type = input.color },
            width = input { default = 1, type = input.line_width}
        }


input
=====

    
.. qcs:enum:: input_type

    :item input.integer: Integer value. 
    :item input.double: Numeric value.
    :item input.boolean: Boolean value. Presented as a checkbox.
    :item input.active: Currently not supported.
    :item input.candle_duration: Currently not supported.
    :item input.string: String value.
    :item input.integer_selection: Selection from the predefined list of integers.
    :item input.double_selection: Selection from the predefined list of numerics.
    :item input.string_selection: Selection from the predefined list of strings.
    :item input.color: Color value.
    :item input.line_width: Line width value.
    :item input.plot_visibility: Plot visibility settings. Presented as a checkbox.
    :item input.plot_shape_style: Shape style value. Not supported on mobile platforms.
    :item input.plot_shape_size: Shape size value. Not supported on mobile platforms.
    :item input.plot_shape_location: Shape location value. Not supported on mobile platforms.


.. qcs:function:: input([default], [name], [type], [options])
    :category: input
    :has_table_overload:

.. qcs:function:: input([default], [name], [type], [min], [max], [step]) 
    :category: input  
    :has_table_overload:

    :param default: Default return value for the input. Default value depends on :code:`type`.
    
    :param name: Name of the input. Can be a localisation key. Default value is :code:`""`.
    :type name: :qcs:type:`string`
    
    :param type: Input type. Default value depends on :code:`value`.
    :type type: :qcs:enum:`input_type`
    
    :param min: Minimal allowed value. Default value depends on :code:`type`.
    
    :param max: Maximal allowed value. Default value depends on :code:`type`.
    
    :param step: Value step. Default value depends on :code:`type`.
    
    :param options: Array of options for the *input.integer_selection*, *input.double_selection*, *input.string_selection*. Default value is :code:`nil`.
    :type options: :code:`array[integer]`
    
    :returns: Same type, as :code:`default`

    **input** creates a user-modifiable value to fine tune the instrument. 
    Inputs can control both the evaluation and the 
    visual settings of the indicator. To execute successfully **input** 
    must have a type set either explicitly or deduced 
    from the default value. Thus either *default* or *type* 
    must be present in the invocation. Not all input types can be 
    manually deduced, these types must be set explicitly. 

    **Indicator Settings**

    +---------------------------+-------+-----------------+----------------+----------------------+
    |type                       |default|min              |max             |step                  |
    +===========================+=======+=================+================+======================+
    |**input.integer**          |0      |:math:`-2^{63}-1`|:math:`2^{63}-1`|1                     |
    +---------------------------+-------+-----------------+----------------+----------------------+
    |**input.double**           |0      |:math:`-1.8e+308`|:math:`1.8e+308`|1                     |
    +---------------------------+-------+-----------------+----------------+----------------------+
    |**input.boolean**          |false  |*N/A*            |*N/A*           |*N/A*                 |
    +---------------------------+-------+-----------------+----------------+----------------------+
    |**input.string**           |``""`` |*N/A*            |*N/A*           |1                     |
    +---------------------------+-------+-----------------+----------------+----------------------+
    |**input.integer_selection**|1      |*N/A*            |*N/A*           |:code:`array[integer]`|
    +---------------------------+-------+-----------------+----------------+----------------------+
    |**input.double_selection** |1      |*N/A*            |*N/A*           |:code:`array[double]` |
    +---------------------------+-------+-----------------+----------------+----------------------+ 
    |**input.string_selection** |1      |*N/A*            |*N/A*           |:code:`array[string]` |
    +---------------------------+-------+-----------------+----------------+----------------------+

    **Visual Settings**

    +---------------------------+---------+
    | type                      | default |
    +===========================+=========+
    | **input.color**           | "white" |
    +---------------------------+---------+
    | **input.line_width**      | 1       |
    +---------------------------+---------+
    | **input.plot_visibility** | true    |
    +---------------------------+---------+ 

    **Source and Average Selectors**

    For convenience, there are predefined arrays to create **source** and **moving average** selectors.

    Input Sources for overlay instruments:

    .. code-block:: lua

        src_idx = input(inputs.close, "Source", input.string_selection, inputs.titles_overlay)
        local source = inputs [src_idx]


    Input Sources for standalone instruments:

    .. code-block:: lua

        src_idx = input(inputs.close, "Source", input.string_selection, inputs.titles)
        local source = inputs [src_idx]

    Moving Averages:

    .. code-block:: lua

        avg_idx = input (averages.sma, "Average", input.string_selection, averages.title)
        local average = averages [avg_idx]


    **Example:**

    .. code-block:: lua

        period = input (9, "front.period", input.integer, 1)
        source = input (1, "front.ind.source", input.string_selection,  inputs.titles)

        plot (sma (inputs [source], period), "SMA")

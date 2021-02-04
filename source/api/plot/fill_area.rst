fill_area
=========

.. qcs:function:: fill_area(first, second, [name], [color])
    :category: plot
    :has_table_overload:

    :param first: First value
    :type first: :qcs:type:`series` or :qcs:type:`numeric`

    :param second: Second value
    :type second: :qcs:type:`series` or :qcs:type:`numeric`

    :param name: Plot name. Default name is :code:`"fill_area(first, second)"`
    :type name: :qcs:type:`string`

    :param color: Plot color. Default value is :code:`"white"`
    :type color: :qcs:type:`color`

    Fills the area between the current values of the `first` and `second`.

    **Example:**

    .. code-block::

        overbought = input(80, "Overbought")
        oversold = input(20, "Oversold")

        fill_area {
            first = overbought, 
            second = oversold,
            color = rgba(255,255,255,0.2)
        }

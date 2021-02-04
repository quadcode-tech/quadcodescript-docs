rect
====

.. qcs:function:: rect(first, second, [name], [color], [width])
    :category: plot
    :has_table_overload:

    :param first: First series.
    :type first: :qcs:type:`series` or :qcs:type:`numeric`

    :param second: Second series.
    :type second: :qcs:type:`series` or :qcs:type:`numeric`

    :param name: Plot name. Default name is :code:`"rect(first, second)"`
    :type name: :qcs:type:`string`

    :param color: Plot color. Default value is :code:`"white"`
    :type color: :qcs:type:`color`

    :param width: The width of the rectangle relative to the bar size. Default value is **1**.
    :type width: :qcs:type:`numeric`

    Plots a rectangle with the given `width` and values defined by the `first` and `last`.

    **Example:**

    .. code-block::

        rect {
            first = 0,
            second = ao,
            color = ao >= ao[1] and up_color or down_color,
            width = 0.8
        }


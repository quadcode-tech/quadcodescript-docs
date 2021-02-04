hline
=====

.. qcs:function:: hline(source,[name, color, line_width, offset, plot_style, show_label])
    :category: plot
    :has_table_overload:

    :param source: Input series or a value.
    :type source: :qcs:type:`series` or :qcs:type:`numeric`
    :param name: Name of the plot. Default value is :code:`"hline(source)"`.
    :type name: :qcs:type:`string`
    :param color: Line color. Default value is :code:`"white"`.
    :type color: :qcs:type:`color`
    :param line_width: Line width. Default value is :code:`1`.
    :type line_width: :qcs:type:`integer`
    :param offset: Offset in bars (not yet handled by the engine). Default value is :code:`0`.
    :type offset: :qcs:type:`integer`
    :param plot_style: Plot style. One of *style.solid_line*, *style.dashed_line*. Not yet handled by the engine. Default value is :code:`style.solid_line`.
    :type plot_style: :qcs:type:`plot_style`
    :param show_label: Contols, if the label with value is shown for this line. Default value is :code:`true`.
    :type show_label: :qcs:type:`boolean`

    Plots a horizontal line throughout the whole instrument plot 
    area through the latest value in the **source**.

    .. code-block::

        overbought = input(80, "Overbought")
        hline (overbought, "Overbought", "red")




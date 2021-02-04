plot
====

.. qcs:enum:: plot_style 

    :description: Style for the line plots.

    :item style.solid_line: Solid line.
    :item style.dash_line: Dashed line.
    :item style.area: Area plot.
    :item style.points: Points plot.
    :item style.crosses: Crosses plot.
    :item style.levels: Levels plot.


.. qcs:enum:: na_mode

    :description: The way the plot handles **nan** values in the input series.
    
    :item na_mode.restart: The line is not drawn over the areas, where series values are **nan**
    :item na_mode.continue: The line connects subsequent valid values.


.. qcs:function:: plot(series, [name], [color], [line_width], [offset], [plot_style], [na_handling_mode])
    :category: plot
    :has_table_overload:

    :param series: Input series.
    :type series: :qcs:type:`series[numeric]`

    :param name: Name of the plot. Default value is :code:`"plot(first,second)"`
    :type name: :qcs:type:`string`

    :param color: Color of the plot. Default value is :code:`"white"`
    :type color: :qcs:type:`color`

    :param line_width: Width of the line. Default value is **1**
    :type line_width: :qcs:type:`integer`

    :param offset: The offset in bars to shift the line left or right. Default value is **0**.
    :type offset: :qcs:type:`integer`

    :param plot_style: Plot style. Not yet handled by the engine. Default value is :code:`style.solid_line`.
    :type plot_style: :qcs:enum:`plot_style`

    :param na_handling_mode: The mode for handling **nan** data in the input `series`. Default value is **na_mode.restart**.
    :type na_handling_mode: :qcs:enum:`na_mode`

    Plots the input `series` as a linear plot.

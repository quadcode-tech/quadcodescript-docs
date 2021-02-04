plot_shape
==========

.. warning::

    This function is not supported on mobile platforms.

.. qcs:enum:: shape_style

    :item shape_style.arrowdown: The shape is drawn as |arrowdown|.
    :item shape_style.arrowup: The shape is drawn as |arrowup|.
    :item shape_style.circle: The shape is drawn as |circle|.
    :item shape_style.cross: The shape is drawn as |cross|.
    :item shape_style.diamond: The shape is drawn as |diamond|.
    :item shape_style.flag: The shape is drawn as |flag|.
    :item shape_style.labeldown: The shape is drawn as |labeldown|.
    :item shape_style.labelup: The shape is drawn as |labelup|.
    :item shape_style.square: The shape is drawn as |square|.
    :item shape_style.triangledown: The shape is drawn as |triangledown|.
    :item shape_style.triangleup: The shape is drawn as |triangleup|.
    :item shape_style.xcross: The shape is drawn as |xcross|.


.. qcs:enum:: shape_location

    :item shape_location.abovebar: The shape is plotted above the bar.
    :item shape_location.belowbar: The shape is plotted below the bar.
    :item shape_location.bottom: The shape is plotted near the bottom chart border.
    :item shape_location.top: The shape is plotted near the top chart border.
    :item shape_location.absolute: The shape position is determined by the series.


.. qcs:enum:: shape_size

    :item shape_size.auto: The shape size depends on the bar size.
    :item shape_size.huge: The shape size is constantly huge.
    :item shape_size.large: The shape size is constantly large.
    :item shape_size.normal: The shape size is constantly normal.
    :item shape_size.small: The shape size is constantly small.
    :item shape_size.tiny: The shape size is constantly tiny.


.. qcs:function:: plot_shape(series, [name], [plot_shape_style], [plot_shape_size], [shape_color], [plot_shape_location], [offset], [text], [text_color])
    :category: plot
    :has_table_overload:

    :param series: Input series. 
        The values are treated as :qcs:type:`boolean`, if the `plot_shape_style` is not 
        **shape_location.absolute**

    :type series: :qcs:type:`series`

    :param name: The plot name. Default value is `series.name`. 
    :type name: :qcs:type:`string`

    :param plot_shape_style: The style of the shape. Default value is **shape_style.xcross**.
    :type plot_shape_style: :qcs:enum:`shape_style`

    :param plot_shape_size: The size of the shape. Default value is **shape_size.auto**.
    :type plot_shape_size: :qcs:enum:`shape_size`. 

    :param shape_color: The color of the shape. Default value is :code:`"white"`.
    :type shape_color: :qcs:type:`color`

    :param plot_shape_location: The location of the shape. Default value is **shape_location.abovebar**.
    :type plot_shape_location: :qcs:enum:`shape_location`

    :param offset: The offset in bars to shift the shape left or right. Default value is **0**.
    :type offset: :qcs:type:`integer`

    :param text: The text to display. Default value is :code:`""`
    :type text: :qcs:type:`string`

    :param text_color: The color of the text to display. Default value is :code:`"white"`
    :type text_color: :qcs:type:`color`


    Plots a shape defined by the `plot_shape_style`. This type of plot is the most useful for 
    the overlay instruments.

    **Example:**

    .. code-block:: lua

        plot_shape {
            series = close > open
        }


.. |arrowdown| image:: /_static/input_shapes/arrowdown.png
    :align: middle

.. |arrowup| image:: /_static/input_shapes/arrowup.png
    :align: middle

.. |circle| image:: /_static/input_shapes/circle.png
    :align: middle

.. |cross| image:: /_static/input_shapes/cross.png
    :align: middle

.. |diamond| image:: /_static/input_shapes/diamond.png
    :align: middle

.. |flag| image:: /_static/input_shapes/flag.png
    :align: middle

.. |labeldown| image:: /_static/input_shapes/labeldown.png
    :align: middle

.. |labelup| image:: /_static/input_shapes/labelup.png
    :align: middle

.. |square| image:: /_static/input_shapes/square.png
    :align: middle

.. |triangledown| image:: /_static/input_shapes/triangledown.png
    :align: middle

.. |triangleup| image:: /_static/input_shapes/triangleup.png
    :align: middle

.. |xcross| image:: /_static/input_shapes/xcross.png
    :align: middle

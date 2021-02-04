plot_candle
===========

.. qcs:function:: plot_candle(open, high, low, close, [name], [candle_color])
    :category: plot
    :has_table_overload:

    :param open: Candle open value
    :type open: :qcs:type:`series` or :qcs:type:`numeric`

    :param high: Candle high value
    :type high: :qcs:type:`series` or :qcs:type:`numeric`

    :param low: Candle low value
    :type low: :qcs:type:`series` or :qcs:type:`numeric`

    :param close: Candle close value
    :type close: :qcs:type:`series` or :qcs:type:`numeric`

    :param name: Plot name. Default value is :code:`"pc(open,high,low,close)"`
    :type name: :qcs:type:`string`

    :param candle_color: Candle color
    :type candle_color: :qcs:type:`color`

    Plots a candlestick defined by the `open`, `high`, `low` and `close` values.

    .. image:: /_static/candlestick.png

    **Example:**

    .. code-block:: lua

        plot_candle {
            open = o, 
            high = h, 
            low = l, 
            close = c, 
            color = iff (c > o, "green", "red")
        }


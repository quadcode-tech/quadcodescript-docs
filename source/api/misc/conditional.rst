conditional
===========

.. qcs:function:: conditional(x)
    :category: misc

    :param x: Value for the current bar
    :type x: :qcs:type:`boolean`

    :returns: :qcs:type:`series[boolean]`

    Converts a boolean value into the series of boolean values. 
    Value for the current bar is set, when the function is invoked.

    **Example:**
    
    .. code-block:: lua

        uptrend = conditional(close > open)
        color = iff (uptrend [1], 'green', 'red')


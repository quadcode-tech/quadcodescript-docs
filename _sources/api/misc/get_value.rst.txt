get_value
=========

.. qcs:function:: get_value(x, [default])
    :category: misc

    :param x: Input value
    :param default: Optional default value

    :returns: type of **x**

    Returns the value of **x** at the current bar or **default** value,
    if **x** does not have the current value

    This function is helpful when one needs to use the series as a 
    condition for the *if* statement.

    If type of **x** is not :qcs:type:`series` - **x** is returned, 
    if **x** is not **nil**, **default** otherwise

    .. code-block:: lua
    
        uptrend = conditional (close > open)

        if get_value (uptrend) then
            print ("Going up")
        end

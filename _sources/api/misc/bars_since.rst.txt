bars_since
==========

.. qcs:function:: bars_since(condition)
    :category: misc
    
    :param condition: A condition value fot the current bar
    :type condition: :qcs:type:`series` or :qcs:type:`numeric` or :qcs:type:`boolean`
    :returns: `series[integer]`

    Returns the number of bars since **condition** was true. 
    Condition is considered to be **false** if condition is **false**, **nil** or **zero**


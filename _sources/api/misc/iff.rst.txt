iff
===

.. qcs:function:: iff(condition, then, else)
    :category: misc

    :param condition: The condition expression. Condition is considered to be false, if it is **nil**, **nan**, **false** or **0**, true otherwise.
    :param then: A value to be set for the current bar of the returned series, if the *condition* is true.
    :param else: A value to be set for the current bar of the returned series, if the *condition* is false.

    :returns: :qcs:type:`series` if any of the args is :qcs:type:`series`. :qcs:type:`numeric` otherwise.

    A functional version of the `if ... then ... else ...` operator. Returns the series with the values from the *then* and 
    *else* arguments depending on the *condition*. This is the safest and the shortest version of the ternary operator (?:), 
    as *Lua* does not support ternary operators. 


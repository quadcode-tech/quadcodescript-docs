bars_since_highest
==================

.. qcs:function:: bars_since_highest(series, n)
    :category: misc

    :param series: Input series
    :type series: :qcs:type:`series`

    :param n: Number of bars to look behind into the history
    :type n: :qcs:type:`integer`

    :returns: `series[integer]`

    Returns the number of bars since the highest value 
    within the last **n** bars in the **series**


.. qcs:function:: bars_since_highest(n)
    :category: misc

    :param n: Number of bars to look behind into the history
    :type n: :qcs:type:`integer`

    :returns: `series[integer]`

    Same as

    .. code-block:: lua

        bars_since_highest(high, n)
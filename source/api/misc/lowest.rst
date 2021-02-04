lowest
======

.. qcs:function:: lowest(series, n)
    :category: misc

    :param series: Input series
    :type series: :qcs:type:`series`

    :param n: Number of bars to look behind into the history
    :type n: :qcs:type:`integer`

    :returns: `series`

    Returns the lowest value of **input** within the last **n** bars.


.. qcs:function:: lowest(n)
    :category: misc

    :param n: Number of bars to look behind into the history
    :type n: :qcs:type:`integer`

    :returns: `series`

    Same as

    .. code-block:: lua

        lowest(low, n)
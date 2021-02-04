highest
=======

.. qcs:function:: highest(series, n)
    :category: misc

    :param series: Input series
    :type series: :qcs:type:`series`

    :param n: Number of bars to look behind into the history
    :type n: :qcs:type:`integer`

    :returns: `series`

    Returns the highest value of **input** within the last **n** bars.


.. qcs:function:: highest(n)
    :category: misc

    :param n: Number of bars to look behind into the history
    :type n: :qcs:type:`integer`

    :returns: `series`

    Same as

    .. code-block:: lua

        highest(high, n)
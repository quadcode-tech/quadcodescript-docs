median
======

.. qcs:function:: median(series, period)
    :category: math

    :param series: Input series
    :type series: :qcs:type:`series`

    :param period: Input period
    :type period: :qcs:type:`integer`

    :returns: :qcs:type:`series`

    Returns the median of the last `period` values in the `series`.

    Same as 

    .. code::

        percentile_nearest_rank (series, period, 50)

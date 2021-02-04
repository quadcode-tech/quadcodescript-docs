percentile_nearest_rank
=======================

.. qcs:function:: percentile_nearest_rank(source, period, percentage)
    :category: math

    :param source: Input series
    :type source: :qcs:type:`series`

    :param period: Input period
    :type period: :qcs:type:`integer`

    :param percentage: Percentage to select. Must be in the :math:`[0,100]` range.
    :type percentage: :qcs:type:`numeric`

    :returns: :qcs:type:`series`

    Calculates percentile using the method of Nearest Rank.

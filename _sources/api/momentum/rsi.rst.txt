rsi
===

.. qcs:function:: rsi(series, period)
    :category: momentum

    :param series: Input series
    :type series: :qcs:type:`series`

    :param period: Input period
    :type period: :qcs:type:`integer`

    :returns: :qcs:type:`series`

    Returns the relative strength index. 

    .. math::

        \delta &= \mathrm{series} - \mathrm{series}_1\\
        u &= \mathrm{rma}(max(\delta, 0), \mathrm{period})\\
        d &= \mathrm{rma}(max(-\delta, 0), \mathrm{period})\\
        \mathrm{rsi} &= 100 - 100 \frac{1}{1 + \frac{u}{d}}

mad
===

.. qcs:function:: mad(series, period)
    :category: math

    :param series: Input series
    :type series: :qcs:type:`series`

    :param period: Input period
    :type period: :qcs:type:`integer`

    :returns: :qcs:type:`series`

    Returns the mean absolute deviation of the `series` over the last `period` bars.

    .. math::

        \overline{x} &= \frac{\sum_{i=0}^{n-1}x_i}{n}\\
        \mathrm{MAD} &= \frac{\sum_{i=0}^{n-1}|x_i - \overline{x}|}{n}

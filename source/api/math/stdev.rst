stdev
=====

.. qcs:function:: stdev(series, period)
    :category: math

    :param series: Input series
    :type series: :qcs:type:`series`

    :param period: Input period
    :type period: :qcs:type:`integer`

    :returns: :qcs:type:`series`

    Returns the standart deviation (:math:`\sigma`) of the last `period` bars in the `series`.

    .. math::

        \overline{x} &= \frac{\sum_{i=0}^{period - 1}x_i}{period}\\
        \sigma &= \sqrt{\frac{\sum_{i=0}^{period - 1}(x_i - \overline{x})^2}{period - 1}}

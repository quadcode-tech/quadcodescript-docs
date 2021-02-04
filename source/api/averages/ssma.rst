ssma
====

.. qcs:function:: ssma(series, period)
    :category: averages

    :param source: Input series
    :type source: :qcs:type:`series`

    :param period: MA period
    :type period: :qcs:type:`numeric`

    :returns: :qcs:type:`series`

    Returns the smoothed simple moving average of **source** for the **period** bars. 
    If there are less than `period` values in the series - the result is **nan**. 
    The first value of :qcs:function:`ssma` is calculated as :code:`sma(series, period)`.
    Subsequent values are calculated according to the formula:
    
    .. math::

        \mathrm{ssma} = \frac{\mathrm{(\mathrm{period} - 1)\mathrm{ssma}_1 + \mathrm{series}_0}}{\mathrm{period}}


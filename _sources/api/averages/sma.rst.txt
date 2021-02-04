sma
===

.. qcs:function:: sma(series, period)
    :category: averages

    :param source: Input series
    :type source: :qcs:type:`series`

    :param period: MA period
    :type period: :qcs:type:`numeric`

    :returns: :qcs:type:`series`

    Returns the simple moving average of **source** for the **period** bars. If there are less
    than `period` values in the series - the result is **nan**.
    
    .. math::

        \mathrm{sma} = \frac{\sum_{i=0}^{period - 1}\mathrm{series}_i}{period}

tma
===

.. qcs:function:: tma(series, period)
    :category: averages

    :param source: Input series
    :type source: :qcs:type:`series`

    :param period: MA period
    :type period: :qcs:type:`numeric`

    :returns: :qcs:type:`series`

    Returns the triangular moving average of **source** for the **period** bars. 
    If there are less than :math:`2\mathrm{period} - 1` values in the series - the result is **nan**. 
    The first value of :qcs:function:`ssma` is calculated as :code:`sma(series, period)`.
    Subsequent values are calculated according to the formula:
    
    .. math::

        \mathrm{tma} = \frac{\sum_{i=0}^{\mathrm{period}-1} \mathrm{sma}_i(\mathrm{series},\mathrm{period})}{2 \mathrm{period} - 1}

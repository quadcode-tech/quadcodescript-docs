vwma
====

.. qcs:function:: vwma(series, period)
    :category: averages

    :param source: Input series
    :type source: :qcs:type:`series`

    :param period: MA period
    :type period: :qcs:type:`numeric`

    :returns: :qcs:type:`series`

    Returns the volume weighted moving average of **source** for the **period** bars.
    
    .. math::

        \mathrm{wma} = \frac{\sum_{i=0}^{\mathrm{period} - 1}\mathrm{volume}_i \mathrm{series}_i}{\sum_{i=0}^{\mathrm{period-1}}\mathrm{volume}_i}


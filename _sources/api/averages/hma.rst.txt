hma
===

.. qcs:function:: hma(series, period)
    :category: averages

    :param series: Input series
    :type series: :qcs:type:`series`

    :param period: MA period
    :type period: :qcs:type:`numeric`

    :returns: :qcs:type:`series`

    Returns the Hull moving average of **source** for the **period** bars. :qcs:function:`hma`
    is a composition of the :qcs:function:`wma` by the following rule:
    
    .. math::

        \mathrm{hma} = \mathrm{wma}(2 \mathrm{wma}(\mathrm{series}, \frac{n}{2}) - \mathrm{wma}(\mathrm{series}, n), \sqrt{n})

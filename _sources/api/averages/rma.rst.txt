rma
===

.. qcs:function:: rma(series, period)
    :category: averages

    :param source: Input series
    :type source: :qcs:type:`series`

    :param period: MA period
    :type period: :qcs:type:`numeric`

    :returns: :qcs:type:`series`

    Returns the rolling moving average of **source** for the **period** bars. 
    
    .. math::

        \mathrm{rma} = \frac{\mathrm{(\mathrm{period} - 1)\mathrm{rma}_1 + \mathrm{series}_0}}{\mathrm{period}}

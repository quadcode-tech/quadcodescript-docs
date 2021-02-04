ema
===

.. qcs:function:: ema(source, period)
    :category: averages

    :param source: Input series.
    :type source: :qcs:type:`series`

    :param period: MA period.
    :type period: :qcs:type:`numeric`

    :returns: :qcs:type:`series`

    Returns the exponential moving average of **source** for the **period** bars.
    
    .. math::

        \alpha &= \frac{2}{\mathrm{period} + 1}\\
        \mathrm{ema} &= \alpha \mathrm{source} + (1 - \alpha)  \mathrm{ema}_1
    
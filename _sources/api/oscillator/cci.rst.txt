cci
===

.. qcs:function:: cci(series, period)
    :category: oscillator

    :param series: Input series
    :type series: :qcs:type:`series`

    :param period: Input period
    :type period: :qcs:type:`integer`

    :returns: :qcs:type:`series`

    Returns the commodity channel index.

    .. math::

        \mathrm{cci} = \frac{1}{0.015}\frac{\mathrm{series} - \mathrm{sma}(\mathrm{series},\mathrm{period})}{\mathrm{mad}(\mathrm{series},\mathrm{period})}

stochastic
==========

.. qcs:function:: stochastic(series, period)
    :category: oscillator

    :param series: Input series
    :type series: :qcs:type:`series`

    :param period: Input period
    :type period: :qcs:type:`integer`

    :returns: :qcs:type:`series`

    Returns the stochastic oscillator.

    .. math::

        \mathrm{stoch} = \frac{\mathrm{series}-\mathrm{lowest}(\mathrm{series}, \mathrm{period})}{\mathrm{highest}(\mathrm{series}, \mathrm{period})-\mathrm{lowest}(\mathrm{series}, \mathrm{period})}

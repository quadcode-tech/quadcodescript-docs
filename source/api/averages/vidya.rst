vidya
=====

.. qcs:function:: vidya(series, period)
    :category: averages

    :param source: Input series
    :type source: :qcs:type:`series`

    :param period: MA period
    :type period: :qcs:type:`numeric`

    :returns: :qcs:type:`series`

    Returns the Chande volatility index dynamic moving average of **source** for 
    the **period** bars. :qcs:function:`vidya` is based on the :qcs:function:`cmo`.
    
    .. math::

        \alpha &= \frac{2|\mathrm{cmo}(\mathrm{series}, \mathrm{period})|}{\mathrm{period} + 1} \\
        \mathrm{vidya} &= \alpha \mathrm{source} + (1 - \alpha)  \mathrm{vidya}_1

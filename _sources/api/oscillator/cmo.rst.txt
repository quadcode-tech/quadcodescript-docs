cmo
===

.. qcs:function:: cmo(series, period)
    :category: oscillator

    :param series: Input series
    :type series: :qcs:type:`series`

    :param period: Input period
    :type period: :qcs:type:`integer`

    :returns: :qcs:type:`series`

    Returns the Chande momentum oscillator.

    .. math::

        \delta &= \mathrm{series} - \mathrm{series}_1\\
        h &= \mathrm{sum}(max(\delta, 0), \mathrm{period})\\
        l &= \mathrm{sum}(max(-\delta, 0), \mathrm{period})\\
        \mathrm{cmo} &=  \frac{h-l}{h+l} \times 100


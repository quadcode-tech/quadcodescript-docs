roc
===

.. qcs:function:: roc(series, [period])
    :category: momentum

    :param series: Input series
    :type series: :qcs:type:`series`

    :param period: Input period. Default value is **1**
    :type period: :qcs:type:`integer`

    :returns: :qcs:type:`series`

    Returns the rate of change between the current value and the value
    `period` bars ago

    .. math::

        \mathrm{roc} = \frac{\mathrm{series}_0 - \mathrm{series}_{period}}{\mathrm{series}_{period}}100 


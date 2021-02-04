alma
====

.. qcs:function:: alma(series, period, offset, sigma)
    :category: averages

    :param series: Input series.
    :type series: :qcs:type:`series`

    :param period: MA Period.
    :type period: :qcs:type:`integer`

    :param offset: 
        Gaussian Distribution mean value. 
        Controls responsiveness of the filter, 
        where 0 is the least responsive and 1 is the most responsive
    :type offset: :qcs:type:`numeric`
 
    :param sigma: 
        Gaussian Distribution standard deviation. 
        Controls the smoothness of the filter.
    :type sigma: :qcs:type:`numeric`

    :returns: :qcs:type:`series`


    Calculates Arnaud Legoux Moving Average. 

    .. math::

        norm &= \sum_{i=0}^{period- 1}e^{-\frac{(i - offset)^2}{\sigma^2}} \\
        alma &= \frac{1}{norm}\sum_{i=0}^{period- 1}input_i e^{-\frac{(i - offset)^2}{\sigma^2}}

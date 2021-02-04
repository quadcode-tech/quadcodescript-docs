linreg
======

.. qcs:function:: linreg(x, n, offset)
    :category: math

    :param x: Input series
    :type x: :qcs:type:`series`

    :param n: Number of bars to calculate the regression
    :type n: :qcs:type:`integer`

    :param offset: Regression offset
    :type offset: :qcs:type:`numeric`

    :returns: :qcs:type:`series`

    Linear regression curve. A line that best fits the prices 
    specified over a user-defined time period. It is calculated using the 
    least squares method. 

    .. math::

        \hat{b} &= \frac{\sum_{i=0}^{n-1}x_i \sum_{i=0}^{n-1}i^2 - \sum_{i=0}^{n-1}i \sum_{i=0}^{n-1}i x_i}{n \sum_{i=0}^{n-1}i^2 - (\sum_{i=0}^{n-1}i)^2}\\
        \hat{a} &= \frac{n \sum_{i=0}^{n-1}i x_i - \sum_{i=0}^{n-1}i \sum_{i=0}^{n-1}x_i}{n \sum_{i=0}^{n-1}i^2 - (\sum_{i=0}^{n-1}i)^2}\\
        \mathrm{linreg} &= \hat{b} - \hat{a} \mathrm{offset}
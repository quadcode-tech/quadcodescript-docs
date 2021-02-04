correlation
===========

.. qcs:function:: correlation(x,y,n)
    :category: math

    :param x: First series
    :type x: :qcs:type:`series`

    :param y: Second series
    :type y: :qcs:type:`series`

    :param n: Number of bars
    :type n: :qcs:type:`integer`

    :returns: :qcs:type:`series`

    Calculates the correlation coefficient
    between series **a** and **b** in the last **n** bars

    .. math::

        \overline{x} &= \frac{1}{n}\sum_{i=0}^{n-1}x_i \quad \overline{y} = \frac{1}{n}\sum_{i=0}^{n-1}y_i\\
        r_{xy}       &= \frac{\sum_{i=0}^{n-1}(x_i-\overline{x})(y_i-\overline{y})}{\sqrt{\sum_{i=0}^{n-1}(x_i-\overline{x})^2(y_i-\overline{y})^2}}

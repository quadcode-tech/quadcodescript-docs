advise
======

.. qcs:enum:: advice

    :item advice.buy: The current instrument value advises to buy the current security.
    :item advice.neutral: The current instrument value could not be used to determine the future trend for the current security.
    :item advice.sell: The current instrument value advises to sell the current security.

.. qcs:function:: advise(advice)
    :category: misc

    :param advice: advice
    :type advice: :qcs:enum:`advice`

    Sets the current advice for the instrument based on its current and historical values. 

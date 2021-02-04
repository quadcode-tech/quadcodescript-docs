sar
===

.. qcs:function:: sar(minaf,step,maxaf)
    :category: misc

    :param minaf: Minimal acceleration factor.
    :type minaf: :qcs:type:`numeric`

    :param step: Acceleration change step.
    :type step: :qcs:type:`numeric`

    :param maxaf: Maximal acceleration factor.
    :type maxaf: :qcs:type:`numeric`

    :returns: :qcs:type:`series`

    Returns the **parabolic stop and reverse** instrument for the current security. 

    **Calculation**
    
    Let:
    
    * `EP` to be the highest high of the current uptrend or the lowest low of the 
      current downtrend.
    
    * `AF` to be the acceleration factor. `AF` starts at `minaf` and increases by 
      `step` every time the EP rises in a Rising SAR or EP falls in a Falling SAR.
      `AF` is limited by `maxaf`

    Then:

    * For the rising *rising* Parabolic SAR: :math:`\mathrm{sar} = \mathrm{sar}_1 + \mathrm{AF}_1 (\mathrm{EP}_1 - \mathrm{sar}_1)`

    * For the *falling* Parabolic SAR: :math:`\mathrm{sar} = \mathrm{sar}_1 - \mathrm{AF}_1 (\mathrm{sar}_1 - \mathrm{EP}_1)`


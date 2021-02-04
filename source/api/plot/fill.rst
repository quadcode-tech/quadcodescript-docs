fill
====

.. qcs:function:: fill(first,second,[name,color])
    :category: plot
    :has_table_overload:

    :param first: First series
    :type first: :qcs:type:`series` or :qcs:type:`numeric`

    :param second: Second series
    :type second: :qcs:type:`series` or :qcs:type:`numeric`

    :params name: Name of the plot. Default value is :code:`"fill(first,second)"`
    :type name: :qcs:type:`string`

    :params color: Color of the plot. Default value is :code:`"white"`
    :type color: :qcs:type:`color`

    Fills the area between **first** and **second** with **color**. 
    If **color** changes between bars where **first** crosses **second** - 
    color change will occur at the intersection between the sources. 

    .. code-block:: lua
        
        fill (high, low)    

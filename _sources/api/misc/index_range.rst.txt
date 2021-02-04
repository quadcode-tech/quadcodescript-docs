index_range
===========

.. qcs:function:: index_range(start_index)
    :category: misc

    :param start_index: Starting index of the series. Default value is **1**.
    :type start_index: :qcs:type:`integer`
    :returns: :qcs:type:`series[integer]`

    Returns a series such as :code:`series [0] == start_index` 
    and :code:`series [i] == start_index + i`.    

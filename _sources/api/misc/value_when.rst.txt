value_when
==========

.. qcs:function:: value_when(condition, series, occurrence)
    :category: misc

    :param condition: condition
    :type condition: :qcs:type:`boolean` or :qcs:type:`series[boolean]`

    :param series: series
    :type series: :qcs:type:`series`

    :param occurrence: occurrence
    :type occurrence: :qcs:type:`integer`

    :returns: :qcs:type:`series`

    Returns the source `series` value when the condition was **true** on the n-th most recent 
    occurrence.

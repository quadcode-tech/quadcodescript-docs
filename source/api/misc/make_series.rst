make_series
===========

.. qcs:function:: make_series([name])
    :category: misc

    :param name: Optional name of the series.
    :type name: :qcs:type:`string`

    :returns: :qcs:type:`series`

    Explicitly creates a series. Use the `set` method to set the current value.
    This function is rarely needed. The primary use is to overcome the limitations 
    of the underlying engine, which does not treat :qcs:type:`numeric` values as 
    :qcs:type:`series`.

    **Example**:

    .. code-block::

        cg = make_series ()
        cg:set(1)
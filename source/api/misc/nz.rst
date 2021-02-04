nz
==

.. qcs:function:: nz(value, [default])
    :category: misc

    :param value: Input value
    :type value: :qcs:type:`series` or :qcs:type:`numeric`

    :param value: Optional default value. **0** if default is not set.
    :type value: :qcs:type:`series` or :qcs:type:`numeric`

    :returns: :qcs:type:`series` or :qcs:type:`numeric`

    If value is :qcs:type:`series`, then function returns a :qcs:type:`series` with the 
    all **nan** values in the input `series` replaced with the `default` value. 
    Otherwise, returns `value` if **value** is not **nan** or **nil**. 
    Otherwise, returns `default`. 

    If `default` is :qcs:type:`series`, the function will use the current value of `default` 
    if needed.

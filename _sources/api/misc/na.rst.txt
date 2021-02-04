na
==

.. qcs:function:: na(value)
    :category: misc

    :param value: Input value

    :returns: :qcs:type:`boolean`

    Checks if the `value` is available, i.e., the `value` is not  **nan** or **nil**. 
    This function can be implemented as:

    .. code-block::

        function na (value)
            local value = get_value (value)
            return isnan (value)
        end

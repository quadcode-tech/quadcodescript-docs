date
====

.. qcs:function:: date([timestamp])
    :category: misc

    :param timestamp: A unix timestamp. The default value is the current bar open time
    :type timestamp: :qcs:type:`integer`

    :returns: Lua table

    Returns a parsed date and time as a lua table in the OS timezone.

    .. code-block::

        {
            year = 1998, 
            month = 9, 
            day = 16, 
            yday = 259, 
            wday = 4,
            hour = 23, 
            min = 48, 
            sec = 10
        }

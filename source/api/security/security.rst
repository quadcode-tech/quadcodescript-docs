security
========

.. qcs:function:: security(ticker_id, resolution)
    :category: security

    :param ticker_id: The ID of the ticker. 
        The ID can be retrieved using the :qcs:function:`get_ticker_id(ticker)`.

    :type ticker_id: :qcs:type:`integer`

    :param resolution: The resolution of the returned security. 
        See description for the possible values.
        
    :type resolution: :qcs:type:`string`

    :returns: A lua table.

    Returns a set of :qcs:type:`series` which represents the given `ticker` at the
    `resolution`.

    The retuned table contains the following fields of the type :qcs:type:`series`:
    
    .. code-block::

        {
            close,
            open,
            high,
            low,
            volume,
            open_time,
            close_time
        }
        
    Possible values for the `resolution` are: :code:`"1s"`, :code:`"5s"`, :code:`"10s"`, :code:`"15s"`, :code:`"30s"`, :code:`"1m"`, 
    :code:`"2m"`, :code:`"5m"`, :code:`"10m"`, :code:`"15m"`, :code:`"30m"`, :code:`"1H"`, 
    :code:`"2H"`, :code:`"4H"`, :code:`"8H"`, :code:`"12H"`, :code:`"1D"`, :code:`"1W"`, 
    :code:`"1M"`, :code:`"1Y"`.

    **Example:**

    .. code-block::

        sec = security (current_ticker_id, "1s")

        plot(sec.close)
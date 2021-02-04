get_ticker_id
=============

.. qcs:function:: get_ticker_id(ticker)
    :category: security

    :param ticker: Input ticker.
    :type ticker: :qcs:type:`string`

    :returns: :qcs:type:`integer`

    Retrieves the ID of the given `ticker`. If the `ticker` is not found - the function returns 
    **nil**.

    **Example:**

    .. code-block::

        local ticker_id = get_ticker_id("EURUSD")


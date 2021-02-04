Built-in Types
==============


.. qcs:type:: series

    **Series** is a list of values that stretches back in time from the current bar. 
    Indexing the series returns the new series shifted by the specified amount of bars 
    backward. For example: 

    +--------+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+
    |Index   |0    |1    |2    |3    |4    |5    |6    |7    |8    |9    |
    +========+=====+=====+=====+=====+=====+=====+=====+=====+=====+=====+
    |close   |15.25|15.46|15.35|15.03|15.02|14.80|15.01|12.87|12.53|12.43|
    +--------+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+
    |close[1]|nil  |15.25|15.46|15.35|15.03|15.02|14.80|15.01|12.87|12.53|
    +--------+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+
    |close[2]|nil  |nil  |15.25|15.46|15.35|15.03|15.02|14.80|15.01|12.87|
    +--------+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+
    |close[3]|nil  |nil  |nil  |15.25|15.46|15.35|15.03|15.02|14.80|15.01|
    +--------+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+

    Series support the number of arithmetic and comparison operations. 
    For example, :code:`(open+close)/2` will return the series, which values are the 
    half sum of the open and close.

    +---------+-----------------+-----------------+-------+
    |Operator |Left-hand side   |Right-hand side  |Result |
    +=========+=================+=================+=======+
    |+,-,*,/,^|series or numeric|series or numeric|series |
    +---------+-----------------+-----------------+-------+
    |<,>,<=,>=|series or numeric|series or numeric|boolean|
    +---------+-----------------+-----------------+-------+
    |==, ~=   |series           |series           |boolean|
    +---------+-----------------+-----------------+-------+
    |`-`      |series           |                 |series |
    +---------+-----------------+-----------------+-------+

    Where:

    * `^` - power operator.
    * `~=` - inequality operator.

    Due to Lua limitations, it is not possible to compare :qcs:type:`series` and a value directly.
    In this case, :qcs:function:`get_value` should be used.

    For example:

    .. code-block::

        if get_value(open) > 10 then
            print ("Hooray!")
        end

    The same restriction applies when using the series as a condition.


.. qcs:type:: series[numeric]

    A :qcs:type:`series` that consists of :qcs:type:`numeric` values.


.. qcs:type:: series[integer]

    A :qcs:type:`series` that consists of :qcs:type:`integer` values.


.. qcs:type:: series[boolean]

    A :qcs:type:`series` that consists of :qcs:type:`boolean` values.


.. qcs:type:: integer

    A 64-bit signed integer value. 

.. qcs:type:: numeric

    A 64-bit floating point value.

.. qcs:type:: boolean

    A boolean value with the values **true** and **false**. By default, in Lua the condition
    is considered to be false when its value is **false** or **nil**. In some cases,
    that are explicitly documented, we also consider **0** to be false.


.. qcs:type:: string

    A string value.


.. qcs:type:: color

    A string, that represents the color in the following formats:

    * :code:`"#RRGGBB"`
    * :code:`"#RRGGBB"`
    * :code:`"#RRGGBBAA"`
    * :code:`"rgb(255,255,255)"`
    * :code:`"rgb(255,255,255,1.0)"`
    * HTML color name_

    For convenience, there are two functions available to create the color:
    :qcs:function:`rgb` and :qcs:function:`rgba`.


    
.. _name: https://htmlcolorcodes.com/color-names/
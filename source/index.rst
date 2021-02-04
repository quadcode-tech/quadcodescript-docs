Quadcode Script
===============

QCS is a language that allows creating custom technical analysis instruments. Currently, the language is based on Lua 5.3 and supports most of the Lua language features.

The script on QCS defines the calculation of the single instrument value using the current security values, historical data and the user input. 

Example
-------

.. code-block::
   :linenos:

   instrument { name = "Simple Moving Average", short_name = "SMA", overlay = true }
 
   period = input (14, "Period", input.integer, 1)
   
   input_group {
      "Line",
      color = input { default = "red", type = input.color },
      width = input { default = 1, type = input.line_width}
   }
   
   ma = sma (close, period)
   
   plot (ma, "SMA", color, width)

.. code::
   
   instrument { name = "Simple Moving Average", short_name = "SMA", overlay = true }

This line defines the full and short names for the instrument. The full name is used in the 
add instruments popup. The short name is displayed on the plot. Additionally, this line 
sets that the instrument will be plotted as a plot overlay. For more information, 
see :qcs:function:`instrument`.


.. code::

   period = input (14, "Period", input.integer, 1)


Defines a user-settable period that is an integer value not less than 1. For more information,
see :qcs:function:`input`.


.. code::

   input_group {
      "Line",
      color = input { default = "red", type = input.color },
      width = input { default = 1, type = input.line_width}
   }

Defines an input group for the instrument visuals. For more information, see 
:qcs:function:`input_group`.

.. code::

   ma = sma (close, period)

This line calculates the simple moving average of the `close` value.

.. code:: 

   plot (ma, "SMA", color, width)

This line plots the previously calculated moving average.

For more examples, the source code of the built in library is available: https://github.com/quadcode-tech/quadcodescript-library

Built-in series
---------------

.. qcs:series:: open
   :overlayable:

   Open value of the current candle 

.. qcs:series:: close
   :overlayable:

   Close value of the current candle

.. qcs:series:: high
   :overlayable:

   High value of the current candle         

.. qcs:series:: low
   :overlayable:

   Low value of the current candle           

.. qcs:series:: volume

   Volume of the current candle      

.. qcs:series:: hml
   :overlayable:

   :code:`high - low`             

.. qcs:series:: hl2
   :overlayable:

   :code:`(high + low) / 2`        

.. qcs:series:: hlc3
   :overlayable:

   :code:`(high + low + close) / 3` (aka `typical price`)       

.. qcs:series:: ohlc4
   :overlayable:

   :code:`(open + high + low + close) / 4`           

.. qcs:series:: hlcc4
   :overlayable:

   :code:`(high + low + close + close) / 4`     

.. qcs:series:: tr

   :code:`max (high - low, high - close [1], close [1] - low)` (aka `true range`)

.. qcs:series:: close_time

   Candle closing time (unix time)       

.. qcs:series:: open_time

   Candle opening time (unix time)              

.. qcs:series:: day

   Candle opening time (day number in a year)          

.. qcs:series:: week_day

   Candle opening time (day number in a week)       

.. qcs:series:: month

   Candle opening time (month)               

.. qcs:series:: year

   Candle opening time (year)                

.. qcs:series:: hour

   Candle opening time (hour)                             

.. qcs:series:: minute

   Candle opening time (minute)                           

.. qcs:series:: second

   Candle opening time (second)     


Built-in functions
------------------

For convenience and performance reasons, QCS has a wide range of built-in functions. 

**Averages**

.. toctree::
   :glob:

   api/averages/*

**User Input**

.. toctree::
   :glob:

   api/input/*

**Plots**

.. toctree::
   :glob:

   api/plot/*

**Math**

.. toctree::
   :glob:

   api/math/*

**Oscillators**

.. toctree::
   :glob:

   api/oscillator/*

**Momentum Instruments**

.. toctree::
   :glob:

   api/momentum/*

**Miscellaneous**

.. toctree::
   :glob:

   api/misc/*

**Security**

.. toctree::
   :glob:

   api/security/*

**State Variables**

.. toctree::
   :glob:

   api/state/*
   built_in_types


Indices
=======

* :ref:`Built-in Types`
* :ref:`qcs-qcs`
* :ref:`genindex`

assert
======

.. qcs:function:: assert(condition, [message])
    :category: misc

    :param condition: A condition to assert on
    :type condition: :qcs:type:`boolean`

    :param message: An optional error message
    :type message: :qcs:type:`string`

    Stops the script execution if the `condition` is **false**. Emits the error `message` to log.
    Useful for debugging

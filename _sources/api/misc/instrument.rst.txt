instrument
==========

.. qcs:function:: instrument(name, short_name_or_overlay, description_or_overlay, icon_or_overlay, overlay)
    :category: misc
    :has_table_overload:

    :param name: Display name of the instrument
    :type name: :qcs:type:`string`

    :param short_name_or_overlay: Abbreviated name of the instrument. If the value is boolean, then the value is treated as `overlay`.
    :type short_name_or_overlay: :qcs:type:`string` or :qcs:type:`boolean`

    :param description_or_overlay: 
        Description of the instrument. If the value is boolean, 
        then the value is treated as `overlay`.
    :type description_or_overlay: :qcs:type:`string` or :qcs:type:`boolean`

    :param icon_or_overlay: 
        Icon of the instrument. If the value is boolean, then the value 
        is treated as `overlay`.
    :type icon_or_overlay: :qcs:type:`string` or :qcs:type:`boolean`

    :param overlay: 
        If **true** - the instrument is an overlay for the main plot. 
        Otherwise, the instrument is in a separate panel below the main plot.
    :type overlay: :qcs:type:`boolean`


    This function determines the base parameters of the instrument. It should be called exactly once at the beginning of the script.

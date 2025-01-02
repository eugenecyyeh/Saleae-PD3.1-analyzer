
pdo_type = {
    0b00: 'Fixed Supply',
    0b01: 'Battery',
    0b10: 'Variable Supply',
    0b11: 'Augmented Power Data Object',
}
augmented_pdo_type = {
    0b00: 'SPR Programmable Power Supply',
    0b01: 'EPR Adjustable Voltage Supply',
    0b10: 'Reserved',
    0b11: 'Reserved',
}

fixed_supply_sink_fast_role_swap_required_current = {
    0b00: 'Fast Swap not supported',
    0b01: 'Default USB Power',
    0b10: '1.5A @ 5V',
    0b11: '3.0A @ 5V',
}

bist_modes = {
    0b0000: 'Reserved',
    0b0001: 'Reserved',
    0b0010: 'Reserved',
    0b0011: 'Reserved',
    0b0100: 'Reserved',
    0b0101: 'BIST Carrier Mode',
    0b0110: 'Reserved',
    0b0111: 'Reserved',
    0b1000: 'BIST Test Data',
    0b1001: 'BIST Shared Test Mode Entry',
    0b1010: 'BIST Shared TestMode Exit',
    0b1011: 'Reserved',
    0b1100: 'Reserved',
    0b1101: 'Reserved',
    0b1110: 'Reserved',
    0b1111: 'Reserved',
}

vdm_type = {
    0b0: 'Unstructured VDM',
    0b1: 'Structured VDM',
}

structured_vdm_version_major = {
    0b00: 'Version 1.0',
    0b01: 'Version 2.0',
    0b10: 'Reserved',
    0b11: 'Reserved',
}

structured_vdm_version_minor = {
    0b00: 'Version 2.0',
    0b01: 'Version 2.1',
    0b10: 'Reserved',
    0b11: 'Reserved',
}

vdo_object_position = {
    0b000: 'Reserved',
    0b001: 1,
    0b010: 2,
    0b011: 3,
    0b100: 4,
    0b101: 5,
    0b110: 6,
    0b111: 'Exit all Active Modes',
}

vdo_command_type = {
    0b00: 'REQ',
    0b01: 'ACK',
    0b10: 'NAK',
    0b11: 'BUSY',
}

battery_charging_status = {
    0b00: 'Battery is Charging',
    0b01: 'Battery is Discharging',
    0b10: 'Battery is Idle',
    0b11: 'Reserved',
}

vdo_command= {
    0b00000: 'Reserved',
    0b00001: 'Discover Identity',
    0b00010: 'Discover SVIDs',
    0b00011: 'Discover Modes',
    0b00100: 'Enter Mode',
    0b00101: 'Exit Mode',
    0b00110: 'Attention',
    0b00111: 'Reserved',
    0b01000: 'Reserved',
    0b01001: 'Reserved',
    0b01010: 'Reserved',
    0b01011: 'Reserved',
    0b01100: 'Reserved',
    0b01101: 'Reserved',
    0b01110: 'Reserved',
    0b01111: 'Reserved',
    0b10000: 'DisplayPort Status update',
    0b10001: 'DisplayPort Configure',
    0b10010: 'SVID Specific Command [18]',
    0b10011: 'SVID Specific Command [19]',
    0b10100: 'SVID Specific Command [20]',
    0b10101: 'SVID Specific Command [21]',
    0b10110: 'SVID Specific Command [22]',
    0b10111: 'SVID Specific Command [23]',
    0b11000: 'SVID Specific Command [24]',
    0b11001: 'SVID Specific Command [25]',
    0b11010: 'SVID Specific Command [26]',
    0b11011: 'SVID Specific Command [27]',
    0b11100: 'SVID Specific Command [28]',
    0b11101: 'SVID Specific Command [29]',
    0b11110: 'SVID Specific Command [30]',
    0b11111: 'SVID Specific Command [31]'
}

usb_mode = {
    0b000: 'USB 2.0',
    0b001: 'USB 3.2',
    0b010: 'USB 4',
    0b011: 'Reserved',
    0b100: 'Reserved',
    0b101: 'Reserved',
    0b110: 'Reserved',
    0b111: 'Reserved',
}

cable_speed = {
    0b000: 'USB2.0',
    0b001: 'USB3.1 Gen1',
    0b010: 'USB3.2 Gen2/USB4 Gen2',
    0b011: 'USB4 Gen3',
    0b100: 'USB4 Gen4',
    0b101: 'Reserved',
    0b110: 'Reserved',
    0b111: 'Reserved',
}

cable_type = {
    0b00: 'Passive',
    0b01: 'Active Re-timer',
    0b10: 'Active Re-driver',
    0b11: 'Optically Isolated',
}

cable_current = {
    0b00: 'Vbus not supported',
    0b01: 'Reserved',
    0b10: '3A',
    0b11: '5A',
}

usb4_drd = {
    0b0: 'Not capable of operating as a USB4 Device',
    0b1: 'Capable of operating as a USB4 Device',
}

usb3_drd = {
    0b0: 'Not capable of operating as a USB3.2 Device',
    0b1: 'Capable of operating as a USB3.2 Device',
}

product_type_ufp_sop = {
    0b000: 'Not a UFP',
    0b001: 'PDUSB Hub',
    0b010: 'PDUSB Peripheral',
    0b011: 'PSD',
    0b100: 'Reserved',
    0b101: 'Alternate Mode Adapter',
    0b110: 'VCONN-Powered USB Device',
    0b111: 'Reserved',
}

product_type_ufp_sop_prime = {
    0b000: 'Not a Cable Plug\VPD',
    0b001: 'Reserved',
    0b010: 'Reserved',
    0b011: 'Passive Cable',
    0b100: 'Active Cable',
    0b101: 'Reserved',
    0b110: 'VCONN-Powered USB Device(VPD)',
    0b111: 'Reserved',
}

product_type_dfp_sop = {
    0b000: 'Not a DFP',
    0b001: 'PDUSB Hub',
    0b010: 'PDUSB Host',
    0b011: 'Power Brick',
    0b100: 'Alternate Mode Controller',
    0b101: 'Reserved',
    0b110: 'Reserved',
    0b111: 'Reserved',
}

connector_type = {
    0b00: 'Reserved, for compatibility with legacy systems',
    0b01: 'Reserved',
    0b10: 'USB Type-C Receptacle',
    0b11: 'USB Type-C Plug',
}

product_vdo_ver = {
    0b000: 'Ver.1.0',
    0b001: 'Ver.1.1',
    0b010: 'Ver.1.2',
    0b011: 'Ver.1.3',
    0b100: 'Reserved',
    0b101: 'Reserved',
    0b110: 'Reserved',
    0b111: 'Reserved',
}

product_vdo_connector_type = {
    0b00: 'Reserved',
    0b01: 'Reserved',
    0b10: 'USB Type-C Receptacle',
    0b11: 'USB Type-C Captive Plug',
}

usb_highest_speed = {
    0b000: 'USB2.0 Only',
    0b001: 'USB3.2 Gen1',
    0b010: 'USB3.2 Gen2/USB4 Gen2',
    0b011: 'USB4 Gen3',
    0b100: 'Reserved',
    0b101: 'Reserved',
    0b110: 'Reserved',
    0b111: 'Reserved',
}

ama_vdo_ver = {
    0b000: 'Ver.1.0',
    0b001: 'Reserved',
    0b010: 'Reserved',
    0b011: 'Reserved',
    0b100: 'Reserved',
    0b101: 'Reserved',
    0b110: 'Reserved',
    0b111: 'Reserved',
}

vconn_power = {
    0b000: '1W',
    0b001: '1.5W',
    0b010: '2W',
    0b011: '3W',
    0b100: '4W',
    0b101: '5W',
    0b110: '6W',
    0b111: 'Reserved',
}

yesno = {
    0b0: 'No',
    0b1: 'Yes',
}

ama_usb_highest_speed = {
    0b000: 'USB2 Only',
    0b001: 'USB3.2 Gen1 and USB2',
    0b010: 'USB3.2 Gen1/Gen2 and USB2',
    0b011: 'USB2 billboard only',
    0b100: 'Reserved',
    0b101: 'Reserved',
    0b110: 'Reserved',
    0b111: 'Reserved',
}

maximum_vbus_voltage = {
    0b00: '20V',
    0b01: '30V',
    0b10: '40V',
    0b11: '50V',
}

cable_connector_type = {
    0b00: 'Reserved',
    0b01: 'Reserved',
    0b10: 'USB Type-C',
    0b11: 'Captive',
}

activecable_latency = {
    0b0000: 'Reserved',
    0b0001: '<10ns(1m)',
    0b0010: '10ns~20ns(2m)',
    0b0011: '20ns~30ns(3m)',
    0b0100: '30ns~40ns(4m)',
    0b0101: '40ns~50ns(5m)',
    0b0110: '50ns~60ns(6m)',
    0b0111: '60ns~70ns(7m)',
    0b1000: '1000ns(100m)',
    0b1001: '2000ns(200m)',
    0b1010: '3000ns(300m)',
    0b1011: 'Reserved',
    0b1100: 'Reserved',
    0b1101: 'Reserved',
    0b1110: 'Reserved',
    0b1111: 'Reserved',
}

passivecable_latency = {
    0b0000: 'Reserved',
    0b0001: '<10ns(1m)',
    0b0010: '10ns~20ns(2m)',
    0b0011: '20ns~30ns(3m)',
    0b0100: '30ns~40ns(4m)',
    0b0101: '40ns~50ns(5m)',
    0b0110: '50ns~60ns(6m)',
    0b0111: '60ns~70ns(7m)',
    0b1000: '>70ns(>7m)',
    0b1001: 'Reserved',
    0b1010: 'Reserved',
    0b1011: 'Reserved',
    0b1100: 'Reserved',
    0b1101: 'Reserved',
    0b1110: 'Reserved',
    0b1111: 'Reserved',
}

vbus_current_handling_capability = {
    0b00: 'USB Type-C Default current',
    0b01: '3A',
    0b10: '5A',
    0b11: 'Reserved',
}

u3cld_power = {
    0b000: '>10mW',
    0b001: '5~10mW',
    0b010: '1~5mW',
    0b011: '0.5~1mW',
    0b100: '0.2~0.5mW',
    0b101: '50~200µW',
    0b110: '<50µW',
    0b111: 'Reserved',
}

svid_mode = {
    0xFF01: 'VESA/DisplayPort',
    0x8087: 'Thunderbolt',
}

port_capability = {
    0b00: 'Reserved',
    0b01: 'UFP_D capable',
    0b10: 'DFP_D capable',
    0b11: 'DFP_D and UFP_D capable',
}

dfp_ufp_connected = {
    0b00: 'Neither DFP_D nor UFP_D is connected',
    0b01: 'DFP_D is connected',
    0b10: 'UFP_D is connected',
    0b11: 'Both DFP_D and UFP_D are connected',
}

configure_ufp_pin_assignment = {
    0b00000000: 'De-select',
    0b00000001: 'A',
    0b00000010: 'B',
    0b00000100: 'C',
    0b00001000: 'D',
    0b00010000: 'E',
    0b00100000: 'F',
}

signaling_for_transport_of_dp_protocol = {
    0b0000: 'Signaling unspecified',
    0b0001: 'Select DP v1.3 signaling rates and electrical settings',
    0b0010: 'Select Gen 2 signaling rates and electrical specifications',
    0b0011: 'Reserved',
    0b0100: 'Reserved',
    0b0101: 'Reserved',
    0b0110: 'Reserved',
    0b0111: 'Reserved',
    0b1000: 'Reserved',
    0b1001: 'Reserved',
    0b1010: 'Reserved',
    0b1011: 'Reserved',
    0b1100: 'Reserved',
    0b1101: 'Reserved',
    0b1110: 'Reserved',
    0b1111: 'Reserved',
}

select_configuration = {
    0b00: 'Set configuration for USB',
    0b01: 'Set configuration for UFP_U as DFP_D',
    0b10: 'Set configuration for UFP_U as UFP_D',
    0b11: 'Reserved',
}

legacy_tbt_mdp_cable_status = {
    0b00: 'No Cable connected',
    0b01: 'TBT Cable',
    0b10: 'DP Cable',
    0b11: 'Other Cable/Adapter',
}


def decode_source_power_data_object(word, object_index): #3.1
    data = {
        'data_object_type': f'PDO{object_index}'
    }
    frame_type = 'object'
    _pdo_type = (word >> 30) & 0x3
    pdo_type_str = pdo_type[_pdo_type]
    if word == 0x0:
        frame_type = str('epr_mode_pdo_null')
        data['pdo_type'] = str('null')
    elif _pdo_type == 0b11:
        _augmented_pdo_type = (word >> 28) & 0x3
        pdo_type_str = str(augmented_pdo_type[_augmented_pdo_type])
        if _augmented_pdo_type == 0x00:
            #SPR Programmable Power Supply Augmented Power Data Object
            pps_power_limited = (word >> 27) & 0x1
            maximum_voltage = int((word >> 17) & 0xFF)*0.1
            minimum_voltage = int((word >> 8) & 0xFF)*0.1
            maximum_current = int(word & 0x7F)*0.05
            data['maximum_voltage_V'] = str(f'{maximum_voltage}V')
            data['minimum_voltage_V'] = str(f'{minimum_voltage}V')
            data['maximum_current_A'] = str(f'{maximum_current}A')
            frame_type = 'spr_source_programmable_supply_pdo'
        if _augmented_pdo_type == 0b01:
            #EPR Programmable Power Supply Augmented Power Data Object
            peak_current = (word >> 26) & 0x3
            maximum_voltage = int((word >> 17) & 0x1FF)*0.1
            minimum_voltage = int((word >> 8) & 0xFF)*0.1
            PDP = int(word & 0xFF)
            if peak_current == 0b00:
                data['peak_current'] = str('00b(Peak current equals Ioc)')
            elif peak_current == 0b01:
                data['peak_current'] = str('01b(Peak current equals 125% Ioc for 2ms@10% duty cycle)')
            elif peak_current == 0b10:
                data['peak_current'] = str('10b(Peak current equals 150% Ioc for 2ms@10% duty cycle)')
            elif peak_current == 0b11:
                data['peak current'] = str('11b(Peak current equals 175% Ioc for 2ms@10% duty cycle)')
            data['maximum_voltage_V'] = str(f'{maximum_voltage}V')
            data['minimum_voltage_V'] = str(f'{minimum_voltage}V')
            data['PDP'] = str(f'{PDP}W')
            frame_type = 'epr_source_adjustable_voltage_supply_pdo' 
        data['pdo_type'] = pdo_type_str
    elif _pdo_type == 0b00:
        # Fixed Supply Power Data Object
        dual_role_power = (word >> 29) & 0x1
        usb_suspend_supported = (word >> 28) & 0x1
        unconstrained_power = (word >> 27) & 0x1
        usb_communications_capable = (word >> 26) & 0x1
        dual_role_data = (word >> 25) & 0x1
        unchecked_extended_messages_supported = (word >> 24) & 0x1
        epr_mode_capable = (word >> 23) & 0x1
        peak_current = (word >> 20) & 0x3
        voltage = int((word >> 10) & 0x3FF) * 0.05
        maximum_current = int((word & 0x3FF)) * 0.01
        data['dual_role_power'] = dual_role_power
        data['usb_suspend_supported'] = usb_suspend_supported
        data['unconstrained_power'] = unconstrained_power
        data['usb_communications_capable'] = usb_communications_capable
        data['dual_role_data'] = dual_role_data
        data['unchecked_extended_messages_supported'] = unchecked_extended_messages_supported
        data['epr_mode_capable'] = epr_mode_capable
        if peak_current == 0b00:
            data['peak_current'] = str('00b(Peak current equals Ioc)')
        elif peak_current == 0b01:
            data['peak_current'] = str('01b(Peak current equals 150% Ioc for 1ms@5% duty cycle)')
        elif peak_current == 0b10:
            data['peak_current'] = str('10b(Peak current equals 200% Ioc for 1ms@5% duty cycle)')
        else:
            peak_current = peak_current
        data['voltage_V'] = str(f'{voltage}V')
        data['maximum_current_A'] = str(f'{maximum_current}A')
        frame_type = 'source_fixed_supply_pdo'
        data['pdo_type'] = pdo_type_str
    elif _pdo_type == 0b10:
        # variable supply (non-battery) Power Data Object - source
        maximum_voltage = int((word >> 20) & 0x3FF) * 0.05
        minimum_voltage = int((word >> 10) & 0x3FF) * 0.05
        maximum_current = int(word & 0x3FF) * 0.01
        data['maximum_voltage_V'] = str(f'{maximum_voltage}V')
        data['minimum_voltage_V'] = str(f'{minimum_voltage}V')
        data['maximum_current_A'] = str(f'{maximum_current}A')
        frame_type = 'source_variable_supply_pdo'
        data['pdo_type'] = pdo_type_str
    elif _pdo_type == 0b01:
        # Battery Supply Power Data Object
        maximum_voltage_50mv_units = int((word >> 20) & 0x3FF) * 0.05
        minimum_voltage_50mv_units = int((word >> 10) & 0x3FF) * 0.05
        maximum_allowable_power = int(word & 0x3FF) * 0.25
        data['maximum_voltage_V'] = str(f'{maximum_voltage}V')
        data['minimum_voltage_V'] = str(f'{minimum_voltage}V')
        data['maximum_allowable_power_W'] = str(f'{maximum_allowable_power}W')
        frame_type = 'source_battery_supply_pdo'
        data['pdo_type'] = pdo_type_str

    return frame_type, data

# sink_capabilities,
def decode_sink_power_data_object(word, object_index):
    data = {
        'data_object_type': f'PDO{object_index}-Sink'
    }
    frame_type = 'object'

    _pdo_type = (word >> 30) & 0x3
    pdo_type_str = pdo_type[_pdo_type]
    if _pdo_type == 0b11:
        _augmented_pdo_type = (word >> 28) & 0x3
        pdo_type_str = augmented_pdo_type[_augmented_pdo_type]
        if _augmented_pdo_type == 0b00:
            # Programmable Power Supply Augmented Power Data Object
            maximum_voltage_V = int((word >> 17) & 0xFF) * 0.1
            minimum_voltage_V = int((word >> 8) & 0xFF) * 0.1
            maximum_current_A = int(word & 0x7F) * 0.05
            data['maximum_voltage_V'] = str(f'{maximum_voltage_V}V')
            data['minimum_voltage_V'] = str(f'{minimum_voltage_V}V')
            data['maximum_current_A'] = str(f'{maximum_current_A}A')
            frame_type = 'sink_programmable_supply_pdo'
        elif _augmented_pdo_type == 0b01:
            #EPR
            maximum_voltage_V = int((word >> 17) & 0x1FF) * 0.1
            minimum_voltage_V = int((word >> 8) & 0xFF) * 0.1
            pd_power_W = int(word & 0xFF) * 1
            data['maximum_voltage_V'] = str(f'{maximum_voltage_V}V')
            data['minimum_voltage_V'] = str(f'{minimum_voltage_V}V')
            data['pd_power_W'] = str(f'{pd_power_W}W')
            frame_type = 'sink_programmable_supply_pdo'
    else:
        if _pdo_type == 0b00:
            # Fixed Supply Power Data Object
            dual_role_power = (word >> 29) & 0x1
            higher_capability = (word >> 28) & 0x1
            unconstrained_power = (word >> 27) & 0x1
            usb_communications_capable = (word >> 26) & 0x1
            dual_role_data = (word >> 25) & 0x1
            fast_role_swap_required_current = (word >> 23) & 0x3
            voltage_V = int((word >> 10) & 0x3FF) * 0.05
            operational_current_A = int(word & 0x3FF) * 0.01
            data['dual_role_power'] = dual_role_power
            data['higher_capability'] = higher_capability
            data['unconstrained_power'] = unconstrained_power
            data['usb_communications_capable'] = usb_communications_capable
            data['dual_role_data'] = dual_role_data
            data['fast_role_swap_required_current'] = fixed_supply_sink_fast_role_swap_required_current[fast_role_swap_required_current]
            data['voltage_V'] = str(f'{voltage_V}V')
            data['operational_current_A'] = str(f'{operational_current_A}A')
            frame_type = 'sink_fixed_supply_pdo'

        elif _pdo_type == 0b10:
            # variable supply (non-battery) Power Data Object - source
            maximum_voltage_V = int((word >> 20) & 0x3FF) * 0.05
            minimum_voltage_V = int((word >> 10) & 0x3FF) * 0.05
            maximum_current_A = int(word & 0x3FF) * 0.01
            data['maximum_voltage_V'] = str(f'{maximum_voltage_V}V')
            data['minimum_voltage_V'] = str(f'{minimum_voltage_V}V')
            data['maximum_current_A'] = str(f'{maximum_current_A}A')
            frame_type = 'sink_variable_supply_pdo'
        elif _pdo_type == 0b01:
            # Battery Supply Power Data Object
            maximum_voltage_V = int((word >> 20) & 0x3FF) * 0.05
            minimum_voltage_V = int((word >> 10) & 0x3FF) * 0.05
            maximum_allowable_power_W = int(word & 0x3FF) * 0.25
            data['maximum_voltage_V'] = str(f'{maximum_voltage_V}V')
            data['minimum_voltage_V'] = str(f'{minimum_voltage_V}V')
            data['maximum_allowable_W'] = str(f'{maximum_allowable_power_W}W')
            frame_type = 'sink_battery_supply_pdo'

    data['pdo_type'] = pdo_type_str

    return frame_type, data

def decode_bist_data_object(word, object_index):
    if object_index == 1:
        data = {
            'data_object_type': 'BIST Data Object'
        }
        frame_type = 'bist_bdo'
        bist_mode = (word >> 28) & 0xF
        data['bist_mode'] = bist_modes[bist_mode] 
    else:
        data = {
            'data_object_type': 'BIST Test Data'
        }
        frame_type = 'bist_test_data'
    return frame_type, data


def decode_request_data_object(word, pdo_type): #3.1
    data = {
        'data_object_type': 'Request Data Object'
    }
    frame_type = 'object'
    if pdo_type == 'Fixed Supply' or pdo_type == 'Variable Supply':
        object_position = (word >> 28) & 0xF
        giveback_flag = (word >> 27) & 0x1
        capability_mismatch = (word >> 26) & 0x1
        usb_communications_capable = (word >> 25) & 0x1
        no_usb_suspend = (word >> 24) & 0x1
        unchunked_extended_messages_supported = (word >> 23) & 0x1
        erp_mode_capable = (word >> 22) & 0x1
        operating_current_A = int((word >> 10) & 0x3FF) * 0.01
        maximum_operating_current_A = int(word & 0x3FF) * 0.01
        data['object_position'] = object_position
        data['giveback_flag'] = giveback_flag
        data['capability_mismatch'] = capability_mismatch
        data['usb_communications_capable'] = usb_communications_capable
        data['no_usb_suspend'] = no_usb_suspend
        data['unchunked_extended_messages_supported'] = unchunked_extended_messages_supported
        data['erp_mode_capable'] = erp_mode_capable
        data['operating_current_A'] = str(f'{operating_current_A}A')
        if giveback_flag == 0b1:
            data['minimum_operating_current_A'] = str(f'{maximum_operating_current_A}A')
            if pdo_type == 'Fixed Supply':
                frame_type = 'fixed_supply_rdo_giveback'
            if pdo_type == 'Variable Supply':
                frame_type = 'variable_supply_rdo_giveback'
        else:
            data['maximum_operating_current_A'] = str(f'{maximum_operating_current_A}A')
            if pdo_type == 'Fixed Supply':
                frame_type = 'fixed_supply_rdo'
            if pdo_type == 'Variable Supply':
                frame_type = 'variable_supply_rdo'
    elif pdo_type == 'Battery':
        object_position = (word >> 28) & 0xF
        giveback_flag = (word >> 27) & 0x1
        capability_mismatch = (word >> 26) & 0x1
        usb_communications_capable = (word >> 25) & 0x1
        no_usb_suspend = (word >> 24) & 0x1
        unchunked_extended_messages_supported = (word >> 23) & 0x1
        erp_mode_capable = (word >> 22) & 0x1
        operating_power_W = int((word >> 10) & 0x3FF) * 0.25
        maximum_operating_power_W = int(word & 0x3FF) * 0.25
        data['object_position'] = object_position
        data['giveback_flag'] = giveback_flag
        data['capability_mismatch'] = capability_mismatch
        data['usb_communications_capable'] = usb_communications_capable
        data['no_usb_suspend'] = no_usb_suspend
        data['unchunked_extended_messages_supported'] = unchunked_extended_messages_supported
        data['erp_mode_capable'] = erp_mode_capable
        data['operating_power_W'] = str(f'{operating_power_W}W')
        if giveback_flag == 0b1:
            data['minimum_operating_power_W'] = str(f'{maximum_operating_power_W}W')
            frame_type = 'battery_rdo_giveback'
        else:
            data['maximum_operating_power_W'] = str(f'{maximum_operating_power_W}W')
            frame_type = 'battery_rdo'
    elif pdo_type == 'SPR Programmable Power Supply':
        object_position = (word >> 28) & 0xF
        capability_mismatch = (word >> 26) & 0x1
        usb_communications_capable = (word >> 25) & 0x1
        no_usb_suspend = (word >> 24) & 0x1
        unchunked_extended_messages_supported = (word >> 23) & 0x1
        erp_mode_capable = (word >> 22) & 0x1
        output_voltage_V = int((word >> 9) & 0xFFF) * 0.02
        operating_current_A = int(word & 0x7F) * 0.05
        data['object_position'] = object_position
        data['capability_mismatch'] = capability_mismatch
        data['usb_communications_capable'] = usb_communications_capable
        data['no_usb_suspend'] = no_usb_suspend
        data['unchunked_extended_messages_supported'] = unchunked_extended_messages_supported
        data['erp_mode_capable'] = erp_mode_capable
        data['output_voltage_V'] = str(f'{output_voltage_V}V')
        data['operating_current_A'] = str(f'{operating_current_A}A')
        frame_type = 'pps_rdo'
    elif pdo_type == 'EPR Adjustable Voltage Supply':
        object_position = (word >> 28) & 0x7
        capability_mismatch = (word >> 26) & 0x1
        usb_communications_capable = (word >> 25) & 0x1
        no_usb_suspend = (word >> 24) & 0x1
        unchunked_extended_messages_supported = (word >> 23) & 0x1
        erp_mode_capable = (word >> 22) & 0x1
        output_voltage_V = int((word >> 9) & 0xFFF) * 0.025
        operating_current_A = int(word & 0x7F) * 0.05
        data['object_position'] = object_position
        data['capability_mismatch'] = capability_mismatch
        data['usb_communications_capable'] = usb_communications_capable
        data['no_usb_suspend'] = no_usb_suspend
        data['unchunked_extended_messages_supported'] = unchunked_extended_messages_supported
        data['erp_mode_capable'] = erp_mode_capable
        data['output_voltage_V'] = str(f'{output_voltage_V}V')
        data['operating_current_A'] = str(f'{operating_current_A}A')
        frame_type = 'avs_rdo'
    
    elif pdo_type == 'null':
        frame_type = 'null_rdo'
    return frame_type, data

## For PD3.1
def decode_vendor_header_data_object_31(word):
    data = {
        'data_object_type': 'VDM_Header'
    }
    vendor_id = (word >> 16) & 0xFFFF
    _vdm_type = (word >> 15) & 0x1
    data['vendor_id'] = str(hex(vendor_id))
    data['vdm_type'] = vdm_type[_vdm_type]
    if _vdm_type == 0b1:
        frame_type = 'structured_header_vdo_31'
        _structured_vdm_version_major = (word >> 13) & 0x3
        _structured_vdm_version_minor = (word >> 11) & 0x3
        object_position = (word >> 8) & 0x7
        command_type = (word >> 6) & 0x3
        command = word & 0x1F
        data['structured_vdm_version_major'] = structured_vdm_version_major[_structured_vdm_version_major]
        data['structured_vdm_version_minor'] = structured_vdm_version_minor[_structured_vdm_version_minor]
        data['object_position'] = vdo_object_position[object_position]
        data['command_type'] = vdo_command_type[command_type]
        data['command'] = vdo_command[command]
    else :
        frame_type = 'unstructured_header_vdo'
        
    return frame_type, data

def decode_id_header_data_object(word, address_cmd):
    data = {
        'data_object_type': 'ID Header VDO'
    }
    frame_type = 'id_header_vdo'

    usb_communications_capable_as_usb_host = (word >> 31) & 0x1
    usb_communications_capable_as_usb_device = (word >> 30) & 0x1
    _product_type_ufp = (word >> 27) & 0x7
    modal_operation_supported = (word >> 26) & 0x1
    _product_type_dfp = (word >> 23) & 0x7
    _connector_type = (word >> 21) & 0x3
    usb_vendor_id = word & 0xFFFF
    data['usb_communications_capable_as_usb_host'] = usb_communications_capable_as_usb_host
    data['usb_communications_capable_as_usb_device'] = usb_communications_capable_as_usb_device
    if address_cmd == 'SOP':
        data['product_type_ufp'] = product_type_ufp_sop[_product_type_ufp]
        data['product_type_dfp'] = product_type_dfp_sop[_product_type_dfp]
    if address_cmd == 'SOP_prime':
        data['product_type_ufp'] = product_type_ufp_sop_prime[_product_type_ufp]
        data['product_type_dfp'] = str('Reserved')
    data['modal_operation_supported'] = modal_operation_supported
    data['connector_type'] = connector_type[_connector_type]
    data['usb_vendor_id'] = str(hex(usb_vendor_id)) 
    return frame_type, data
    
def decode_cert_stat_vdo(word):
    data = {
        'data_object_type': 'Cert Stat VDO'
    }
    frame_type = 'cert_stat_vdo'

    xid = word & 0xFFFFFFFF
    data['xid'] = str(hex(xid))
        
    return frame_type, data

def decode_product_vdo(word):
    data = {
        'data_object_type': 'Product VDO'
    }
    frame_type = 'product_vdo'

    usb_product_id = (word >> 16) & 0xFFFF
    bcddevice = word & 0xFF
    data['usb_product_id'] = str(hex(usb_product_id))
    data['bcddevice'] = str(hex(bcddevice))
        
    return frame_type, data
    
def decode_ufp_vdo1(word):
    data = {
        'data_object_type': 'UFP VDO1'
    }
    frame_type = 'ufp_vdo1'

    _ufp_vdo1_ver = (word >> 29) & 0x7
    usb4_capable = (word >> 27) & 0x1
    usb3_capable = (word >> 26) & 0x1
    usb2_capable_billboardonly = (word >> 25) & 0x1
    usb2_capable = (word >> 24) & 0x1
    _ufp_vdo1_connector_type = (word >> 22) & 0x3
    supports_alt_modes_not_reconfigured_signals_on_usb2 = (word >> 5) & 0x1
    supports_alt_modes_reconfigured_signals_on_usb2 = (word >> 4) & 0x1 
    support_tbt3_alt_mode = (word >> 3) & 0x1
    _usb_highest_speed = word & 0x7
    data['ufp_vdo1_ver'] = product_vdo_ver[_ufp_vdo1_ver]
    data['usb4_capable'] = usb4_capable
    data['usb3_capable'] = usb3_capable
    data['usb2_capable_billboardonly'] = usb2_capable_billboardonly
    data['usb2_capable'] = usb2_capable
    data['ufp_vdo1_connector_type'] = product_vdo_connector_type[_ufp_vdo1_connector_type]
    data['supports_alt_modes_do_not_reconfigured_signals_on_usb2'] = supports_alt_modes_not_reconfigured_signals_on_usb2
    data['supports_alt_modes_reconfigured_signals_on_usb2'] = supports_alt_modes_reconfigured_signals_on_usb2
    data['support_tbt3_alt_mode'] = support_tbt3_alt_mode
    data['usb_highest_speed'] = usb_highest_speed[_usb_highest_speed]
        
    return frame_type, data

def decode_ufp_vdo2(word):
    data = {
        'data_object_type': 'UFP VDO2'
    }
    frame_type = 'ufp_vdo2'

    usb4_min_power = (word >> 23) & 0x7F
    usb4_max_power = (word >> 16) & 0x7F
    usb3_min_power = (word >> 7) & 0x7F
    usb3_max_power = word & 0x7F
    data['usb4_min_power'] = usb4_min_power
    data['usb4_max_power'] = usb4_max_power
    data['usb3_min_power'] = usb3_min_power
    data['usb3_max_power'] = usb3_max_power
        
    return frame_type, data

def decode_dfp_vdo(word):
    data = {
        'data_object_type': 'DFP VDO'
    }
    frame_type = 'dfp_vdo'
    
    _dfp_vdo_ver = (word >> 29) & 0x7
    dfp_usb4_capable = (word >> 26) & 0x1
    dfp_usb3_capable = (word >> 25) & 0x1
    dfp_usb2_capable = (word >> 24) & 0x1
    _dfp_vdo_connector_type = (word >> 22) & 0x3
    port_number = word &  0x1F
    data['dfp_vdo_ver'] = product_vdo_ver[_dfp_vdo_ver]
    data['usb4_host_capable'] = dfp_usb4_capable
    data['usb3_host_capable'] = dfp_usb3_capable
    data['usb2_host_capable'] = dfp_usb2_capable
    data['dfp_vdo_connector_type'] = product_vdo_connector_type[_dfp_vdo_connector_type]
    data['port_number'] = port_number
        
    return frame_type, data
    
def decode_ama_vdo(word):
    data = {
        'data_object_type': 'Alternate Mode Adapter VDO'
    }
    frame_type = 'ama_vdo'
    
    hw_version = (word >> 28) & 0xF
    fw_version = (word >> 24) & 0xF
    _vdo_version = (word >> 21) & 0x7
    _vconn_power = (word >> 5) & 0x7
    _vconn_required = (word >> 4) & 0x1
    _vbus_required = (word >> 3) & 0x1
    _ama_usb_highest_speed = word &  0x7
    data['hw_version'] = str(hex(hw_version))
    data['fw_version'] = str(hex(fw_version))
    data['vdo_version'] = ama_vdo_ver[_vdo_version]
    data['vconn_power'] = vconn_power[_vconn_power]
    data['vconn_required'] = yesno[_vconn_required]
    data['vbus_required'] = yesno[_vbus_required]
    data['ama_usb_highest_speed'] = ama_usb_highest_speed[_ama_usb_highest_speed]
        
    return frame_type, data
    
def decode_vdp_vdo(word):
    data = {
        'data_object_type': 'VCONN-Powered Device'
    }
    frame_type = 'vdp_vdo'
    
    hw_version = (word >> 28) & 0xF
    fw_version = (word >> 24) & 0xF
    _vdo_version = (word >> 21) & 0x7
    _maximum_vbus_voltage = (word >> 15) & 0x3
    charge_through_current_support = (word >> 14) & 0x1
    vbus_impedance = (word >> 7) & 0x3F
    ground_impedance = (word >> 1) & 0x3F
    charge_through_support = word & 0x1
    data['hw_version'] = str(hex(hw_version))
    data['fw_version'] = str(hex(fw_version))
    data['vdo_version'] = ama_vdo_ver[_vdo_version]
    data['maximum_vbus_voltage'] = maximum_vbus_voltage[_maximum_vbus_voltage]
    if charge_through_current_support == 0x0:
        data['charge_through_current_support'] = str('3A capable')
    elif charge_through_current_support == 0x1:
        data['charge_through_current_support'] = str('5A capable')
    else:
        data['charge_through_current_support'] = str(hex(charge_through_current_support))
    if charge_through_support == 0x0:
        data['vbus_impedance'] = vbus_impedance & 0x0
        data['ground_impedance'] = ground_impedance & 0x0
        data['charge_through_support'] = str('VPD does not support Charge Through')
    elif charge_through_support == 0x1:
        data['vbus_impedance'] = int(vbus_impedance) * 2
        data['ground_impedance'] = int(ground_impedance) * 1
        data['charge_through_support'] = str('VPD supports Charge Through')
    else:
        data['vbus_impedance'] = str(hex(vbus_impedance))
        data['ground_impedance'] = str(hex(ground_impedance))
        data['charge_through_support'] = str(hex(charge_through_support))
        
    return frame_type, data
    
def decode_activecable_vdo1(word):
    data = {
        'data_object_type': 'Active Cable VDO1'
    }
    frame_type = 'activecable_vdo1'
    
    hw_version = (word >> 28) & 0xF
    fw_version = (word >> 24) & 0xF
    vdo_version = (word >> 21) & 0x7
    _connector_type = (word >> 18) & 0x3
    _activecable_latency = (word >> 13) & 0xF
    cable_terminiation_type = (word >> 11) & 0x3
    _maximum_vbus_voltage = (word >> 9) & 0x3
    sbu_supported = (word >> 8) & 0x1
    sbu_type = (word >> 7) & 0x1
    _vbus_current_handling_capability = (word >> 5) & 0x3
    _vbus_through_cable = (word >> 4) & 0x1
    sop_double_prime_present = (word >> 3) & 0x1
    _usb_highest_speed = word & 0x3

    data['hw_version'] = str(hex(hw_version))
    data['fw_version'] = str(hex(fw_version))
    if vdo_version == 0x3:
        data['vdo_version'] = str('Ver.1.3')
    elif vdo_version == 0x1 or vdo_version == 0x2:
        data['vdo_version'] = str(bin(vdo_version))
    else:
        data['vdo_version'] = str('Reserved')
    data['connector_type'] = cable_connector_type[_connector_type]
    data['cable_latency'] = activecable_latency[_activecable_latency]
    if cable_terminiation_type == 0b10:
        data['cable_terminiation_type'] = str('One end Active,one end passive,VCONN required')
    elif cable_terminiation_type == 0b11:
        data['cable_terminiation_type'] = str('Both ends Active,VCONN required')
    else:
        data['cable_terminiation_type'] = str('Reserved')
    data['maximum_vbus_voltage'] = maximum_vbus_voltage[_maximum_vbus_voltage]
    if sbu_supported == 0x0:
        data['sbu_supported'] = str('SBUs connections supported')
        if sbu_type == 0x0:
            data['sbu_type'] = str('SBU is passive')
        elif sbu_type == 0x1:
            data['sbu_type'] = str('SBU is active')
        else:
            data['sbu_type'] = str(hex(sbu_type))
    elif sbu_supported == 0x1:
        data['sbu_supported'] = str('SBU connections are not supported')
        data['sbu_type'] = str('ignored')
    else:
        data['sbu_supported'] = str(bin(sbu_supported))
        data['sbu_type'] = str(hex(sbu_type))
    if _vbus_through_cable == 0x1:
        data['vbus_current_handling_capability'] = vbus_current_handling_capability[_vbus_current_handling_capability]
    elif _vbus_through_cable == 0x0:
        data['vbus_current_handling_capability'] = str('ignored')
    else:
        data['vbus_current_handling_capability'] = str(hex(_vbus_current_handling_capability))
    data['vbus_through_cable'] = yesno[_vbus_through_cable]
    if sop_double_prime_present == 0x0:
        data['sop_double_prime_controller_present'] = str('No SOP" controller present')
    elif sop_double_prime_present == 0x1:
        data['sop_double_prime_controller_present'] = str('SOP" controller present')
    data['usb_highest_speed'] = usb_highest_speed[_usb_highest_speed]
    
    return frame_type, data
    
def decode_activecable_vdo2(word):
    data = {
        'data_object_type': 'Active Cable VDO2'
    }
    frame_type = 'activecable_vdo2'
    
    maximum_operating_temperature = (word >> 24) & 0xFF
    shutdown_temperature = (word >> 16) & 0xFF
    _u3cld_power = (word >> 12) & 0x7
    u3tou0_transition_mode = (word >> 11) & 0x1
    physical_connection = (word >> 10) & 0x1
    active_element = (word >> 9) & 0x1
    usb4_supported = (word >> 8) & 0x1
    usb2_hub_hops_consumed = (word >> 6) & 0x3
    usb2_supported = (word >> 5) & 0x1
    usb3_supported = (word >> 4) & 0x1
    usb_lanes_supported = (word >> 3) & 0x1
    _optically_isolated_active_cable = (word >> 2) & 0x1
    usb_gen = word & 0x1
    data['maximum_operating_temperature'] = maximum_operating_temperature
    data['shutdown_temperature'] = shutdown_temperature
    data['_u3cld_power'] = u3cld_power[_u3cld_power]
    if u3tou0_transition_mode == 0x0:
        data['u3tou0_transition_mode'] = str('U3toU0 direct')
    elif u3tou0_transition_mode == 0x1:
        data['u3tou0_transition_mode'] = str('U3toU0 through U3S')
    else:
        data['u3tou0_transition_mode'] = str(u3tou0_transition_mode)
    if physical_connection == 0x0:
        data['physical_connection'] = str('Copper')
    elif physical_connection == 0x1:
        data['physical_connection'] = str('Optical')
    else:
        data['physical_connection'] = str(hex(physical_connection))
    if active_element == 0x0:
        data['active_element'] = str('Active Redriver')
    elif active_element == 0x1:
        data['active_element'] = str('Active Retimer')
    else:
        data['active_element'] = str(hex(active_element))
    if usb4_supported == 0x0:
        data['usb4_supported'] = str('USB4 supported')
    elif usb4_supported == 0x1:
        data['usb4_supported'] = str('USB4 not supported')
    else:
        data['usb4_supported'] = str(hex(usb4_supported))
    data['usb2_hub_hops_consumed'] = usb2_hub_hops_consumed
    if usb2_supported == 0x0:
        data['usb2_supported'] = str('USB2 supported')
    elif usb2_supported == 0x1:
        data['usb2_supported'] = str('USB2 not supported')
    else:
        data['usb2_supported'] = str(hex(usb2_supported))
    if usb3_supported == 0x0:
        data['usb3_supported'] = str('USB3 SS supported')
    elif usb3_supported == 0x1:
        data['usb3_supported'] = str('USB3 SS not supported')
    else:
        data['usb3_supported'] = str(hex(usb3_supported))
    if usb_lanes_supported == 0x0:
        data['usb_lanes_supported'] = str('One lane')
    elif usb_lanes_supported == 0x1:
        data['usb_lanes_supported'] = str('Two lanes')
    else:
        data['usb_lanes_supported'] = str(hex(usb_lanes_supported))
    data['optically_isolated_active_cable'] = yesno[_optically_isolated_active_cable]
    if usb_gen == 0x0:
        data['usb_gen'] = str('Gen1')
    elif usb_gen == 0x1:
        data['usb_gen'] = str('Gen2 or higher')
    else:
        data['usb_gen'] = str(hex(usb_gen))
    
    return frame_type, data
    
def decode_passivecable_vdo(word):
    data = {
        'data_object_type': 'Passive Cable VDO'
    }
    frame_type = 'passivecable_vdo'
    
    hw_version = (word >> 28) & 0xF
    fw_version = (word >> 24) & 0xF
    _vdo_version = (word >> 21) & 0x7
    _connector_type = (word >> 18) & 0x3
    _passivecable_latency = (word >> 13) & 0xF
    cable_terminiation_type = (word >> 11) & 0x3
    _maximum_vbus_voltage = (word >> 9) & 0x3
    #sbu_supported = (word >> 8) & 0x1
    #sbu_type = (word >> 7) & 0x1
    _vbus_current_handling_capability = (word >> 5) & 0x3
    #_vbus_through_cable = (word >> 4) & 0x1
    #sop_double_prime_present = (word >> 3) & 0x1
    _usb_highest_speed = word & 0x3

    data['hw_version'] = str(hex(hw_version))
    data['fw_version'] = str(hex(fw_version))
    data['vdo_version'] = ama_vdo_ver[_vdo_version]
    data['connector_type'] = cable_connector_type[_connector_type]
    data['cable_latency'] = passivecable_latency[_passivecable_latency]
    if cable_terminiation_type == 0b00:
        data['cable_terminiation_type'] = str('VCONN not required')
    elif cable_terminiation_type == 0b01:
        data['cable_terminiation_type'] = str('VCONN required')
    else:
        data['cable_terminiation_type'] = str('Reserved')
    data['maximum_vbus_voltage'] = maximum_vbus_voltage[_maximum_vbus_voltage]
    if _vbus_current_handling_capability == 0x0:
        data['vbus_current_handling_capability'] = str('Reserved')
    else:
        data['vbus_current_handling_capability'] = vbus_current_handling_capability[_vbus_current_handling_capability]
    data['usb_highest_speed'] = usb_highest_speed[_usb_highest_speed]
    
    return frame_type, data
    
def decode_dsvid_vdo(word, n):
    data = {
        'data_object_type': 'Discovery SVIDs VDO'
    }
    frame_type = 'dsvid_vdo'
    _svidn = (word >> 16) & 0xFFFF
    _svidn1 = word & 0xFFFF
    data['svidn_number'] = n
    
    if svid_mode.get(_svidn, None) == None:
        data['svidn'] = str(hex(_svidn))
    else:
        data['svidn'] = str(hex(_svidn) + '(' + svid_mode[_svidn] + ')')
    data['svidn1_number'] = n + 1
    if svid_mode.get(_svidn1, None) == None:
        data['svidn1'] = str(hex(_svidn1))
    else:
        data['svidn1'] = str(hex(_svidn1) + '(' + svid_mode[_svidn1] + ')')
    n = n + 2

    return frame_type, data, n

def decode_dp_mode(word, n):
    data = {
        'data_object_type': 'DP mode'
    }
    
    frame_type = 'dp_mode'
    
    ufp_pin_assignment_supported = []
    dfp_pin_assignment_supported = []
    signaling_for_transport_of_dp_protocol = []
    ufp_pin_assignment_e = (word >> 20) & 0x1
    ufp_pin_assignment_d = (word >> 19) & 0x1
    ufp_pin_assignment_c = (word >> 18) & 0x1
    ufp_pin_assignment_b = (word >> 17) & 0x1
    ufp_pin_assignment_a = (word >> 16) & 0x1
    dfp_pin_assignment_f = (word >> 13) & 0x1
    dfp_pin_assignment_e = (word >> 12) & 0x1
    dfp_pin_assignment_d = (word >> 11) & 0x1
    dfp_pin_assignment_c = (word >> 10) & 0x1
    dfp_pin_assignment_b = (word >> 9) & 0x1
    dfp_pin_assignment_a = (word >> 8) & 0x1
    _usb2_signaling_not_used = (word >> 7) & 0x1
    receptacle_indication = (word >> 6) & 0x1
    sinaling_of_protocol_usb = (word >> 3) & 0x1
    sinaling_of_protocol_dp = (word >> 2) & 0x1
    _port_capability = word & 0x3
    
    if (word >> 16) & 0x1F == 0x0:
        data['ufp_d_pin_assignment_supported'] = str('not supported')
    else:
        if ufp_pin_assignment_a == 0x1:
            ufp_pin_assignment_a = str('A')
            ufp_pin_assignment_supported.append(ufp_pin_assignment_a)
        if ufp_pin_assignment_b == 0x1:
            ufp_pin_assignment_b = str('B')
            ufp_pin_assignment_supported.append(ufp_pin_assignment_b)
        if ufp_pin_assignment_c == 0x1:
            ufp_pin_assignment_c = str('C')
            ufp_pin_assignment_supported.append(ufp_pin_assignment_c)
        if ufp_pin_assignment_d == 0x1:
            ufp_pin_assignment_d = str('D')
            ufp_pin_assignment_supported.append(ufp_pin_assignment_d)
        if ufp_pin_assignment_e == 0x1:
            ufp_pin_assignment_e = str('E')
            ufp_pin_assignment_supported.append(ufp_pin_assignment_e)
        data['ufp_d_pin_assignment_supported'] = str(','.join(ufp_pin_assignment_supported))

    if (word >> 8) & 0x3F == 0x0:
        data['dfp_d_pin_assignment_supported'] = str('not supported')
    else:
        if dfp_pin_assignment_a == 0x1:
            dfp_pin_assignment_a = str('A')
            dfp_pin_assignment_supported.append(dfp_pin_assignment_a)
        if dfp_pin_assignment_b == 0x1:
            dfp_pin_assignment_b = str('B')
            dfp_pin_assignment_supported.append(dfp_pin_assignment_b)
        if dfp_pin_assignment_c == 0x1:
            dfp_pin_assignment_c = str('C')
            dfp_pin_assignment_supported.append(dfp_pin_assignment_c)
        if dfp_pin_assignment_d == 0x1:
            dfp_pin_assignment_d = str('D')
            dfp_pin_assignment_supported.append(dfp_pin_assignment_d)
        if dfp_pin_assignment_e == 0x1:
            dfp_pin_assignment_e = str('E')
            dfp_pin_assignment_supported.append(dfp_pin_assignment_e)
        if dfp_pin_assignment_f == 0x1:
            dfp_pin_assignment_f = str('F')
            dfp_pin_assignment_supported.append(dfp_pin_assignment_f)
        data['dfp_d_pin_assignment_supported'] = str(','.join(dfp_pin_assignment_supported))
    data['usb2_signaling_not_used'] = yesno[_usb2_signaling_not_used]
    if receptacle_indication == 0x0:
       data['receptacle_indication'] = str('Type-C Plug')
    else:
       data['receptacle_indication'] = str('Type-C Receptacle')
    
    if sinaling_of_protocol_dp == 0x1:
        sinaling_of_protocol_dp = str('Supports DP v1.3')
        signaling_for_transport_of_dp_protocol.append(sinaling_of_protocol_dp)
    elif sinaling_of_protocol_usb == 0x1:
        sinaling_of_protocol_usb = str('Supports USB Gen2 rate')
        signaling_for_transport_of_dp_protocol.append(sinaling_of_protocol_usb)
    else:
        signaling_for_transport_of_dp_protocol.append(str('Reserved'))
    data['signaling_for_transport_of_dp_protocol'] = str(','.join(signaling_for_transport_of_dp_protocol))
    data['port_capability'] = port_capability[_port_capability]
    n = n + 1
    
    return frame_type, data, n
    
def decode_dp_status(word):
    data = {
        'data_object_type': 'DP Status Update'
    }
    
    frame_type = 'dp_status'
    
    irq_hpd = (word >> 8) & 0x1
    hpd_state = (word >> 7) & 0x1
    _exit_dp_mode_request = (word >> 6) & 0x1
    usb_config_request = (word >> 5) & 0x1
    multifunction_preferred = (word >> 4) & 0x1
    enabled = (word >> 3) & 0x1
    power_low = (word >> 2) & 0x1
    _dfp_ufp_connected = word & 0x3
    if (word >> 8) & 0x1 == 0x0:
        data['irq_hpd'] = str('No IRQ_HPD')
    elif (word >> 8) & 0x1 == 0x1:
        data['irq_hpd'] = str('IRQ_HPD')
    else:
        data['irq_hpd'] = str(hex(irq_hpd))
    if (word >> 7) & 0x1 == 0x0:
        data['hpd_state'] = str('HPD_Low')
    elif (word >> 7) & 0x1 == 0x1:
        data['hpd_state'] = str('HPD_High')
    else:
        data['hpd_state'] = str(hex(hpd_state))
    data['exit_dp_mode_request'] = yesno[_exit_dp_mode_request]
    if (word >> 5) & 0x1 == 0x0:
        data['usb_config_request'] = str('Maintain current configuration')
    elif (word >> 5) & 0x1 == 0x1:
        data['usb_config_request'] = str('Request switch to USB configuration')
    else:
        data['usb_config_request'] = str(hex(usb_config_request))
    if (word >> 4) & 0x1 == 0x0:
        data['multifunction_preferred'] = str('No preference for multifunction')
    elif (word >> 4) & 0x1 == 0x1:
        data['multifunction_preferred'] = str('Multi-function preferred')
    else:
        data['multifunction_preferred'] = str(hex(multifunction_preferred))
    if (word >> 3) & 0x1 == 0x0:
        data['enabled'] = str('Adaptor DisplayPort functionality is disabled')
    elif (word >> 3) & 0x1 == 0x1:
        data['enabled'] = str('Adaptor DisplayPort functionality is enabled')
    else:
        data['enabled'] = str(hex(enabled))
    if (word >> 2) & 0x1 == 0x0:
        data['power_low'] = str('Adaptor is functioning normally or is disabled')
    elif (word >> 2) & 0x1 == 0x1:
        data['power_low'] = str('Adaptor has detected low power and disabled DisplayPort support')
    else:
        data['power_low'] = str(hex(power_low))
    data['dfp_ufp_connected'] = dfp_ufp_connected[_dfp_ufp_connected]
    
    return frame_type, data
    
def decode_dp_configure(word):
    data = {
        'data_object_type': 'DP Configure'
    }
    
    frame_type = 'dp_configure'
    _configure_ufp_pin_assignment = (word >> 8) & 0xFF
    _signaling_for_transport_of_dp_protocol = (word >> 2) & 0xF
    _select_configuration = word & 0x3
    if configure_ufp_pin_assignment.get(_configure_ufp_pin_assignment, None) == None:
        data['configure_ufp_pin_assignment'] = str('Reserved')
    else:
        data['configure_ufp_pin_assignment'] = configure_ufp_pin_assignment[_configure_ufp_pin_assignment]
    data['signaling_for_transport_of_dp_protocol'] = signaling_for_transport_of_dp_protocol[_signaling_for_transport_of_dp_protocol]
    data['select_configuration'] = select_configuration[_select_configuration]
    
    return frame_type, data
    
def decode_tbt_mode(word, sop_type):
    data = {
        'data_object_type': 'TBT mode VDO'
    }
    
    if sop_type == 'SOP':
        frame_type = 'tbt_mode_adapter'
        legacy_tbt_adapter = (word >> 16) & 0x1
        tbt_alt_mode = word & 0xFFFF
        if legacy_tbt_adapter == 0x1:
            data['legacy_tbt_adapter'] = str('1h(2nd Gen TBT Adapter)')
            if tbt_alt_mode == 0x0001:
                data['tbt_alt_mode'] = str('0001h(TBT mode)')
            else:
                data['tbt_alt_mode'] = str(hex(tbt_alt_mode))
        else:
            frame_type = 'tbt_mode_device'
            _vpro_avaliable = (word >> 18) & 0x1F
            data['vpro_avaliable'] = yesno[_vpro_avaliable]
            data['legacy_tbt_adapter'] = str('0h(3rd Gen TBT Device)')
            if tbt_alt_mode == 0x0001:
                data['tbt_alt_mode'] = str('0001h(TBT mode)')
            else:
                data['tbt_alt_mode'] = str(hex(tbt_alt_mode))
    else:
        frame_type = 'tbt_cable_mode'
        active_cable_plug_link_training = (word >> 23) & 0x1
        cable_active_passive = (word >> 22) & 0x1
        cable_type = (word >> 21) & 0x1
        tbt_cable_gen = (word >> 19) & 0x3
        cable_speed = (word >> 16) & 0x7
        tbt_alt_mode = word & 0xFFFF
        if active_cable_plug_link_training == 0x0:
            data['active_cable_plug_link_training'] = str('0h(Passive/Active with bi-directional LSRX)')
        else:
            data['active_cable_plug_link_training'] = str('1h(Active with uni-directional LSRX)')
        if cable_active_passive == 0x0:
            data['cable_active_passive'] = str('Passive Cable')
        else:
            data['cable_active_passive'] = str('Active Cable')
        if cable_type == 0x0:
            data['cable_type'] = str('Non-Optical Cable')
        else:
            data['cable_type'] = str('Optical Cable')
        if tbt_cable_gen == 0x0:
            data['tbt_cable_gen'] = str('3rd Gen Non-Rounded TBT')
        elif tbt_cable_gen == 0x1:
            data['tbt_cable_gen'] = str('4th Gen Rounded and Non-Rounded TBT')
        else:
            data['tbt_cable_gen'] = str(hex(tbt_cable_gen) + ' ' + 'Reserved')
        if cable_speed == 0x1:
            data['cable_speed'] = str('01h(USB3.1 Gen1 Cable)')
        elif cable_speed == 0x2:
            data['cable_speed'] = str('02h(10Gbps)')
        elif cable_speed == 0x3:
            data['cable_speed'] = str('03h(10Gbps and 20Gbps)')
        else:
            data['cable_speed'] = str('Reserved')
        if tbt_alt_mode == 0x0001:
            data['tbt_alt_mode'] = str('0001h(TBT mode)')
        else:
            data['tbt_alt_mode'] = str(hex(tbt_alt_mode))
    
    return frame_type, data
    
def decode_tbt_enter_mode(word):
    data = {
        'data_object_type': 'TBT Enter Mode VDO'
    }
    
    frame_type = 'tbt_enter_mode'
    vpro_dock_and_host = (word >> 26) & 0x1
    dfp_legacy_tbt_adapter = (word >> 24) & 0x1
    active_cable_plug_link_training = (word >> 23) & 0x1
    cable_active_passive = (word >> 22) & 0x1
    cable_type = (word >> 21) & 0x1
    tbt_cable_gen = (word >> 19) & 0x3
    cable_speed = (word >> 16) & 0x7
    mode = word & 0xFFFF
    if vpro_dock_and_host == 0x0:
        data['vpro_dock_and_host'] = str('Host/Dock do not support vPro')
    else:
        data['vpro_dock_and_host'] = str('vPro Host and Dock detected')
    if dfp_legacy_tbt_adapter == 0x0:
        data['dfp_legacy_tbt_adapter'] = str('3rd Gen TBT')
    else:
        data['dfp_legacy_tbt_adapter'] = str('2nd Gen TBT Adapter')
    if active_cable_plug_link_training == 0x0:
        data['active_cable_plug_link_training'] = str('0h(Passive/Active with bi-directional LSRX)')
    else:
        data['active_cable_plug_link_training'] = str('1h(Active with uni-directional LSRX)')
    if cable_active_passive == 0x0:
        data['cable_active_passive'] = str('Passive Cable')
    else:
        data['cable_active_passive'] = str('Active Cable')
    if cable_type == 0x0:
        data['cable_type'] = str('Non-Optical Cable')
    else:
        data['cable_type'] = str('Optical Cable')
    if tbt_cable_gen == 0x0:
        data['tbt_cable_gen'] = str('3rd Gen Non-Rounded TBT')
    elif tbt_cable_gen == 0x1:
        data['tbt_cable_gen'] = str('4th Gen Rounded and Non-Rounded TBT')
    else:
        data['tbt_cable_gen'] = str(hex(tbt_cable_gen) + ' ' + 'Reserved')
    if cable_speed == 0x0:
        data['cable_speed'] = str('00h(No TBT support)')
    elif cable_speed == 0x1:
        data['cable_speed'] = str('01h(USB3.1 Gen1 Cable)')
    elif cable_speed == 0x2:
        data['cable_speed'] = str('02h(10Gbps)')
    elif cable_speed == 0x3:
        data['cable_speed'] = str('03h(10Gbps and 20Gbps)')
    else:
        data['cable_speed'] = str('Reserved')
    if mode == 0x0001:
        data['tbt_alt_mode'] = str('0001h(TBT mode)')
    else:
        data['tbt_alt_mode'] = str(hex(tbt_alt_mode))
            
    return frame_type, data
    
def decode_tbt_attention(word):
    data = {
        'data_object_type': 'TBT Status VDO'
    }
    
    frame_type = 'tbt_attention'
    exit_tbt_mode_request = (word >> 4) & 0x1
    usb2_billboard_status = (word >> 2) & 0x3
    _legacy_tbt_mdp_cable_status = word & 0x3
    if exit_tbt_mode_request == 0x0:
        data['exit_tbt_mode_request'] = str('0b(Maintain TBT Mode)')
    else:
        data['exit_tbt_mode_request'] = str('1b(Exit TBT Mode)')
    if usb2_billboard_status == 0x0:
        data['usb2_billboard_status'] = str('00b(USB2 billboard not being presented.In TBT Mode)')
    elif usb2_billboard_status == 0x3:
        data['usb2_billboard_status'] = str('11b(USB2 billboard being presented.Exit TBT Mode)')
    else:
        data['usb2_billboard_status'] = str('Reserved')
    data['legacy_tbt_mdp_cable_status'] = legacy_tbt_mdp_cable_status[_legacy_tbt_mdp_cable_status]
            
    return frame_type, data

def decode_battery_status_data_object(word):
    data = {
        'data_object_type': 'Battery Status Data Object'
    }
    frame_type = 'bsdo'
    battery_present_capacity = (word >> 16) & 0xFFFF
    if battery_present_capacity == 0xFFFF:
        data['battery_preset_Capacity_WH'] = str('SOC unknown')
    else:
        data['battery_preset_Capacity_WH'] = int(battery_present_capacity) * 0.1
    battery_info = (word >> 8) & 0xFF
    invalid_battery_reference = battery_info & 0x1
    battery_is_present = (battery_info >> 1) & 0x1
    _battery_charging_status = (battery_info >> 2) & 0x3
    data['invalid_battery_reference'] = invalid_battery_reference
    if battery_is_present == 0b0:
        data['battery_present'] = str('Battery is not present')
        data['battery_charging_status'] = str('Reserved')
    elif battery_is_present == 0b1:
        data['battery_present'] = str('battery_is_present')
        data['battery_charging_status'] = battery_charging_status[_battery_charging_status]

    return frame_type, data


def decode_alert_data_object(word):
    data = {
        'data_object_type': 'Alert Data Object'
    }
    frame_type = 'ado'

    type_of_alert = (word >> 24) & 0x7

    fixed_batteries = (word >> 20) & 0xF
    hot_swappable_batteries = (word >> 16) & 0xF
    battery_status_change_event = (type_of_alert >> 1) & 0x1
    ocp_event = (type_of_alert >> 2) & 0x1
    otp_event = (type_of_alert >> 3) & 0x1
    operating_condition_change = (type_of_alert >> 4) & 0x1
    source_input_change = (type_of_alert >> 5) & 0x1
    ovp_event = (type_of_alert >> 6) & 0x1

    data['fixed_batteries'] = fixed_batteries
    data['hot_swappable_batteries'] = hot_swappable_batteries
    data['battery_status_change_event'] = battery_status_change_event
    data['ocp_event'] = ocp_event
    data['otp_event'] = otp_event
    data['operating_condition_change'] = operating_condition_change
    data['source_input_change'] = source_input_change
    data['ovp_event'] = ovp_event

    return frame_type, data


def decode_get_country_info_data_object(word):
    data = {
        'data_object_type': 'Country Code Data Object'
    }
    frame_type = 'ccdo'

    first_character = (word >> 24) & 0xF
    second_character = (word >> 16) & 0xF

    data['country_code'] = '{first}{second}'.format(
        first=chr(first_character), second=char(second_character))

    return frame_type, data


def decode_enter_usb_data_object(word):
    data = {
        'data_object_type': 'Enter USB'
    }
    frame_type = 'eudo'

    _usb_mode = (word >> 28) & 0x7
    _usb4_drd = (word >> 26) & 0x1
    _usb3_drd = (word >> 25) & 0x1
    _cable_speed = (word >> 21) & 0x7
    _cable_type = (word >> 21) & 0x7
    _cable_current = (word >> 17) & 0x3
    pcie_support = (word >> 16) & 0x1
    dp_support = (word >> 15) & 0x1
    tbt_support = (word >> 14) & 0x1
    host_present = (word >> 13) & 0x1

    data['usb_mode'] = usb_mode[_usb_mode]
    data['usb4_drd'] = usb4_drd[_usb4_drd]
    data['usb3_drd'] = usb3_drd[_usb3_drd]
    data['cable_speed'] = cable_speed[_cable_speed]
    data['cable_type'] = cable_type[_cable_type]
    data['cable_current'] = cable_current[_cable_current]
    data['pcie_support'] = pcie_support
    data['dp_support'] = dp_support
    data['tbt_support'] = tbt_support
    data['host_present'] = host_present

    return frame_type, data

action = {
    0x00: 'Reserved',
    0x01: 'Enter',
    0x02: 'Enter Acknowledged',
    0x03: 'Enter Succeeded',
    0x04: 'Enter failed',
    0x05: 'Exit',
}

data_failed = {
    0x00: 'Unknown cause',
    0x01: 'Cable not EPR capable',
    0x02: 'Source failed to become Vconn source',
    0x03: 'EPR Mode Capable bit not set in RDO',
    0x04: 'Source unable to enter EPR Mode at this time',
    0x05: 'EPR Mode Capable bit not set in PDO',
}

def decode_eprmode(word):
    data = {
        'data_db_type': 'EPR Mode DO'
    }
    frame_type = 'epr_mode_do'

    _action = (word >> 24) & 0xFF
    _data = (word >> 16) & 0xFF
    if action.get(_action, None) == None:
        data['action'] = str('Reserved')
    else:
        data['action'] = action[_action]
    if _action == 0x04:
        data['data'] = data_failed[_data]
    else:
        data['data'] = str(hex(_data))
        
    return frame_type, data

ecdb_type = {
    1: 'EPR_Get_Source_Cap',
    2: 'EPR_Get_Sink_Cap',
    3: 'EPR_KeepAlive',
    4: 'EPR_KeepAlive_Ack',
}

def decode_extended_control_msg(word):
    data = {
        'data_db_type': 'Extended Control DB'
    }
    frame_type = 'ecdb'
    data_ = (word >> 8) & 0xFF
    _type = word & 0xFF
    if ecdb_type.get(_type, None) == None:
        data['type'] = str('Reserved')
    else:
        data['type'] = ecdb_type[_type]
    data['data'] = str(hex(data_))

    return frame_type, data

def decode_extended_source_capabilities(word):
    data = {
        'data_db_type': 'Extended Source Capabilities DB'
    }
    frame_type = 'scedb'
    source_inputs_discription = []
    vid = word & 0xFFFF
    pid = (word >> 16) & 0xFFFF
    xid = (word >> 32) & 0xFFFFFFFF
    fw_ver = (word >> 64) & 0xFF
    hw_ver = (word >> 72) & 0xFF
    voltage_regulation = (word >> 80) & 0xFF
    loadstep = (voltage_regulation) & 0x3
    ioc = (voltage_regulation >> 2) & 0x1
    holdup_time = (word >> 88) & 0xFF
    compliance = (word >> 96) & 0xFF
    lps_compliant = (compliance) & 0x1
    ps1_compliant = (compliance >> 1) & 0x1
    ps2_compliant = (compliance >> 2) & 0x1
    touch_current = (word >> 104) & 0xFF
    low_touch_current_eps = touch_current & 0x1
    gnd_pin_support = (touch_current >> 1) & 0x1
    gnd_pin_intended_for_protective_earth = (touch_current >> 2) & 0x1
    peak_current1 = (word >> 112) & 0xFFFF
    peak_current2 = (word >> 128) & 0xFFFF
    peak_current3 = (word >> 144) & 0xFFFF
    touch_temp = (word >> 160) & 0xFF
    source_inputs = (word >> 168) & 0xFF
    ext_supply_preset = (word >> 168) & 0x1
    ext_supply_constrained = (word >> 169) & 0x1
    battery_preset = (word >> 170) & 0x1
    fixed_betteries_slots = (word >> 176) & 0xF
    hot_swappable_betteries_slots = (word >> 180) & 0xF
    spr_source_pdp = (word >> 184) & 0xFF
    epr_source_pdp = (word >> 192) & 0xFF
    data['vid'] = str(hex(vid))
    data['pid'] = str(hex(pid))
    data['xid'] = str(hex(xid))
    data['fw_version'] = fw_ver
    data['hw_version'] = hw_ver
    if loadstep == 0x0:
        loadstep = str('150mA/us')
    elif loadstep == 0x1:
        loadstep = str('500mA/us')
    else:
        loadstep = str('Reserved')
    if ioc == 0x0:
        ioc = str('25% Ioc')
    else:
        ioc = str('90% Ioc')
    data['voltage_regulation'] = f'{bin(voltage_regulation)},Load step:[{loadstep}],Ioc:[{ioc}]'
    if holdup_time == 0x00:
        data['holdup_time'] = str('feature not supported')
    else:
        data['holdup_time'] = f'{int(holdup_time)}ms'
    data['compliance'] = f'{bin(compliance)},LPS Compliant:[{lps_compliant}],PS1 Compliant:[{ps1_compliant}],PS2 Compliant:[{ps2_compliant}]'
    data['touch_current'] = f'{bin(touch_current)},Low touch current EPS:[{low_touch_current_eps}],Gnd Pin support:[{gnd_pin_support}],Gnd Pin Intended For Protective Earth:[{gnd_pin_intended_for_protective_earth}]'
    percent_overload1 = f'{int(peak_current1 & 0x1F) * 10}%'
    overload_period1 = f'{int((peak_current1 >> 5) & 0x3F) * 20}ms'
    duty_cycle1 = f'{int((peak_current1 >> 11) & 0xF) * 5}%'
    vbus_drop1 = (peak_current1 >> 15) & 0x1
    data['peak_current1'] = str(f'Percent overload:[{percent_overload1}],Overload period:[{overload_period1}],Duty cycle:[{duty_cycle1}],Vbus volt droop:[{vbus_drop1}]')
    percent_overload2 = f'{int(peak_current2 & 0x1F) * 10}%'
    overload_period2 = f'{int((peak_current2 >> 5) & 0x3F) * 20}ms'
    duty_cycle2 = f'{int((peak_current2 >> 11) & 0xF) * 5}%'
    vbus_drop2 = (peak_current2 >> 15) & 0x1
    data['peak_current2'] = str(f'Percent overload:[{percent_overload2}],Overload period:[{overload_period2}],Duty cycle:[{duty_cycle2}],Vbus volt droop:[{vbus_drop2}]')
    percent_overload3 = f'{int(peak_current3 & 0x1F) * 10}%'
    overload_period3 = f'{int((peak_current3 >> 5) & 0x3F) * 20}ms'
    duty_cycle3 = f'{int((peak_current3 >> 11) & 0xF) * 5}%'
    vbus_drop3 = (peak_current3 >> 15) & 0x1
    data['peak_current3'] = f'Percent overload:[{percent_overload3}],Overload period:[{overload_period3}],Duty cycle:[{duty_cycle3}],Vbus volt droop:[{vbus_drop3}]'
    if touch_temp == 0x0:
        data['touch_temp'] = str('IEC 60950-1')
    elif touch_temp == 0x1:
        data['touch_temp'] = str('IEC 62368-1 TS1')
    elif touch_temp == 0x2:
        data['touch_temp'] = str('IEC 62368-1 TS2')
    else:
        data['touch_temp'] = str('Reserved')
    if ext_supply_preset == 0x0:
        source_inputs_discription.append(str('No external supply'))
    elif ext_supply_preset == 0x1:
        source_inputs_discription.append(str('External supply preset'))
    if ext_supply_preset == 0x1 and ext_supply_constrained == 0x0:
        source_inputs_discription.append(str('External supply is constrained'))
    elif ext_supply_preset == 0x1 and ext_supply_constrained == 0x1:
        source_inputs_discription.append(str('External supply is unconstrained'))
    if battery_preset == 0x0:
        source_inputs_discription.append(str('No internal Battery'))
    elif battery_preset == 0x1:
        source_inputs_discription.append(str('Internal Battery present'))    
    data['source_inputs'] = f'{str(bin(source_inputs))},[{source_inputs_discription}]'
    data['num_of_batt_slots'] = f'Hot Swappable BATT slots: [{hot_swappable_betteries_slots}],Fixed BATT slots: [{fixed_betteries_slots}]'
    data['spr_source_pdp'] = f'{spr_source_pdp}W'
    data['epr_source_pdp'] = f'{epr_source_pdp}W'
    
    return frame_type, data
    
def decode_extended_sink_capabilities(word):
    data = {
        'data_db_type': 'Extended Sink Capabilities DB'
    }
    frame_type = 'skedb'
    sink_load_discription = []
    sink_mode_discription = []
    vid = word & 0xFFFF
    pid = (word >> 16) & 0xFFFF
    xid = (word >> 32) & 0xFFFFFFFF
    fw_ver = (word >> 64) & 0xFF
    hw_ver = (word >> 72) & 0xFF
    sledb_ver = (word >> 80) & 0xFF
    loadstep = (word >> 88) & 0xFF
    sink_load_characteristics = (word >> 96) & 0xFFFF
    compliance = (word >> 112) & 0xFF
    touch_temp = (word >> 120) & 0xFF
    battery_info = (word >> 128) & 0xFF
    fixed_betteries_slots = (battery_info) & 0xF
    hot_swappable_betteries_slots = (battery_info >> 4) & 0xF
    sink_modes = (word >> 136) & 0xFF
    pps_charging_supported = (sink_modes) & 0x1
    vbus_powered = (sink_modes >> 1) & 0x1
    mains_powered = (sink_modes >> 2) & 0x1
    battery_powered = (sink_modes >> 3) & 0x1
    battery_essentially_unlimited = (sink_modes >> 4) & 0x1
    avs_supported = (sink_modes >> 5) & 0x1
    sink_min_pdp = (word >> 144) & 0x7F
    sink_operational_pdp = (word >> 152) & 0x7F
    sink_max_pdp = (word >> 160) & 0x7F
    epr_sink_min_pdp = (word >> 168) & 0xFF
    epr_sink_operational_pdp = (word >> 176) & 0xFF
    epr_sink_max_pdp = (word >> 184) & 0xFF
    data['vid'] = str(hex(vid))
    data['pid'] = str(hex(pid))
    data['xid'] = str(hex(xid))
    data['fw_version'] = fw_ver
    data['hw_version'] = hw_ver
    if sledb_ver == 1:
        data['sledb_version'] = str('Version 1.0')
    else:
        data['sledb_version'] = f'{sledb_ver},Reserved'
    if loadstep == 0x0:
        data['load_step'] = str('150mA/us')
    elif loadstep == 0x1:
        data['load_step'] = str('500mA/us')
    else:
        loadstep = str('Reserved')
        data['load_step'] = f'{bin(loadstep)},Reserved'
    percent_overload = f'{((sink_load_characteristics) & 0x1F) * 10}%'
    overload_period = f'{((sink_load_characteristics >> 5) & 0x3F) * 20}ms'
    duty_cycle = f'{((sink_load_characteristics >> 11) & 0xF) * 5}%'
    vbus_droop = (sink_load_characteristics >> 15) & 0x1
    sink_load_discription.append(f'Percent overload: [{percent_overload}]')
    if (sink_load_characteristics & 0x1F) != 0x0:
        sink_load_discription.append(f'Overload period: [{overload_period}]')
        sink_load_discription.append(f'Duty cycle: [{duty_cycle}]')
        sink_load_discription.append(f'Can tolerate Vbus droop: [{vbus_droop}]')
    data['sink_load_characteristics'] = f'{sink_load_characteristics},[{sink_load_discription}]'
    lps_compliant = (compliance) & 0x1
    ps1_compliant = (compliance >> 1) & 0x1
    ps2_compliant = (compliance >> 2) & 0x1
    data['compliance'] = f'{bin(compliance)},LPS Compliant:[{lps_compliant}],PS1 Compliant:[{ps1_compliant}],PS2 Compliant:[{ps2_compliant}]'
    if touch_temp == 0x0:
        data['touch_temp'] = str('IEC 60950-1')
    elif touch_temp == 0x1:
        data['touch_temp'] = str('IEC 62368-1 TS1')
    elif touch_temp == 0x2:
        data['touch_temp'] = str('IEC 62368-1 TS2')
    else:
        data['touch_temp'] = str('Reserved')
    data['battery_info'] = f'Hot Swappable BATT slots: [{hot_swappable_betteries_slots}],Fixed BATT slots: [{fixed_betteries_slots}]'
    data['sink_modes'] = f'{hex(sink_modes)},PPS chargeing supported: [{pps_charging_supported}],Vbus powered: [{vbus_powered}],Mains powered: [{mains_powered}],Battery powered: [{battery_powered}],Battery essentially unlimited: [{battery_essentially_unlimited}],AVS supported: [{avs_supported}]'
    data['sink_min_pdp'] = f'{sink_min_pdp}W'
    data['sink_operational_pdp'] = f'{sink_operational_pdp}W'
    data['sink_max_pdp'] = f'{sink_max_pdp}W'
    data['epr_sink_min_pdp'] = f'{epr_sink_min_pdp}W'
    data['epr_sink_operational_pdp'] = f'{epr_sink_operational_pdp}W'
    data['epr_sink_max_pdp'] = f'{epr_sink_max_pdp}W'
    
    return frame_type, data
    
message_type = {
    0x01: 'GET_FW_ID(Response)',
    0x02: 'PDFU_INITIATE(Response)',
    0x03: 'PDFU_DATA(Response)',
    0x05: 'PDFU_VALIDATE(Response)',
    0x07: 'PDFU_DATA_PAUSE(Response)',
    0x7F: 'VENDOR_SPECIFIC(Response)',
    0x81: 'GET_FW_ID',
    0x82: 'PDFU_INITIATE',
    0x83: 'PDFU_DATA',
    0x84: 'PDFU_DATA_NR',
    0x85: 'PDFU_VALIDATE',
    0x86: 'PDFU_ABORT',
    0x87: 'PDFU_DATA_PAUSE',
    0xFF: 'VENDOR_SPECIFIC',
}
    
def decode_firmware_update_msg_header(word):
    data = {
        'data_db_type': 'Firmware Update Message Header'
    }
    frame_type = 'fw_update_msg_header'
    protocol_version = (word) & 0xFF
    _message_type = (word >> 8) & 0xFF
    if protocol_version == 0x1:
        data['protocol_version'] = str('Version 1.0')
    else:
        data['protocol_version'] = str('Reserved')
    if message_type.get(_message_type, None) == None:
        data['message_type'] = str('Reserved')
    else:
        data['message_type'] = message_type(_message_type)
    
    return frame_type, data
    
pdfu_status_info = {
    0x00: 'OK',
    0x01: 'errTarget',
    0x02: 'errFile',
    0x03: 'errWrite',
    0x04: 'errERASE',
    0x05: 'errCHECK_ERASED',
    0x06: 'errPROG',
    0x07: 'errVERIFY',
    0x08: 'errADDRESS',
    0x09: 'errNOTDONE',
    0x0A: 'errFIRMWARE',
    0x0D: 'errPOR',
    0x0E: 'errUNKNOWN',
    0x80: 'errUNEXPECTED_HARD_RESET',
    0x81: 'errUNEXPECTED_SOFT_RESET',
    0x82: 'errUNEXPECTED_REQUEST',
    0x83: 'errREJECT_PAUSE',
}

def decode_getfw_id_response(word):
    data = {
        'data_db_type': 'Get_FW_ID(Response) Payload'
    }
    frame_type = 'pdfu_getfw_id_response'
    _status = (word) & 0xFF
    vid = (word >> (8*1)) & 0xFFFF
    pid = (word >> (8*3)) & 0xFFFF
    hwversion = (word >> (8*5)) & 0xFF
    hwversion_minor = (hwversion) & 0xF
    hwversion_major = (hwversion >> 4) & 0xF
    siversion = (word >> (52)) & 0xF
    fwversion1 = (word >> (8*7)) & 0xFFFF
    fwversion2 = (word >> (8*9)) & 0xFFFF
    fwversion3 = (word >> (8*11)) & 0xFFFF
    fwversion4 = (word >> (8*13)) & 0xFFFF
    imagebank = (word >> (8*15)) & 0xFF
    flags1 = (word >> (8*16)) & 0xFF
    flags2 = (word >> (8*17)) & 0xFF
    flags3 = (word >> (8*18)) & 0xFF
    flags4 = (word >> (8*19)) & 0xFF
    data['status'] = pdfu_status_info[_status]
    data['vid'] = str(hex(vid))
    data['pid'] = str(hex(pid))
    data['hwversion_major'] = hwversion_major
    data['hwversion_minor'] = hwversion_minor
    data['siversion'] = siversion
    data['fwversion1'] = fwversion1
    data['fwversion2'] = fwversion2
    data['fwversion3'] = fwversion3
    data['fwversion4'] = fwversion4
    data['imagebank'] = str(hex(imagebank))
    data['flags1'] = str(bin(flags1))
    data['flags2'] = str(bin(flags2))
    data['flags3'] = str(bin(flags3))
    data['flags4'] = str(bin(flags4))
    
    return frame_type, data
    
def decode_pdfu_initiate_response(word):
    data = {
        'data_db_type': 'PDFU_INITIATE(Response) Payload'
    }
    frame_type = 'pdfu_initiate_response'
    _status = (word) & 0xFF
    waittime = (word >> (8*1)) & 0xFF
    maximagesize = (word >> (8*2)) & 0xFFFFFFFF
    max_fw_image_length = (maximagesize) & 0xFFFFF
    data['status'] = pdfu_status_info[_status]
    data['waittime'] = f'{waittime*10}ms'
    data['maximagesize'] = f'{max_fw_image_length}bytes'
    
    return frame_type, data
    
def decode_pdfu_data_response(word):
    data = {
        'data_db_type': 'PDFU_DATA(Response) Payload'
    }
    frame_type = 'pdfu_data_response'
    _status = (word) & 0xFF
    waittime = (word >> (8*1)) & 0xFF
    numdata_nr = (word >> (8*2)) & 0xFF
    datablock_num = (word >> (8*3)) & 0xFFFF
    data['status'] = pdfu_status_info[_status]
    data['waittime'] = f'{waittime*1}ms'
    data['numdata_nr'] = numdata_nr
    data['datablock_num'] = datablock_num
    
    return frame_type, data
    
def decode_pdfu_validate_response(word):
    data = {
        'data_db_type': 'PDFU_VALIDATE(Response) Payload'
    }
    frame_type = 'pdfu_validate_response'
    _status = (word) & 0xFF
    waittime = (word >> (8*1)) & 0xFF
    flags = (word >> (8*2)) & 0x1
    data['status'] = pdfu_status_info[_status]
    data['waittime'] = f'{waittime*1}ms'
    data['flags'] = flags
    
    return frame_type, data
   
def decode_pdfu_data_pause_response(word):
    data = {
        'data_db_type': 'PDFU_DATA_PAUSE(Response) Payload'
    }
    frame_type = 'pdfu_validate_response'
    _status = (word) & 0xFF
    data['status'] = pdfu_status_info[_status]
    
    return frame_type, data
    
def decode_vendor_specific_response(word):
    data = {
        'data_db_type': 'VENDOR_SPECIFIC(Response) Payload'
    }
    frame_type = 'pdfu_vendor_specific_response_payload1'
    _status = (word) & 0xFF
    vid = (word >> (8*1)) & 0xFFFF
    data['status'] = pdfu_status_info[_status]
    data['vid'] = hex(vid)
    
    return frame_type, data
    
message_type_security = {
    0x01: 'DIGESTS(Response)',
    0x02: 'CERTIFICATE(Response)',
    0x03: 'CHALLENGE_AUTH(Response)',
    0x7F: 'ERROR(Response)',
    0x81: 'GET_DIGESTS',
    0x82: 'GET_CERTIFICATE',
    0x83: 'CHALLENGE',
}
    
def decode_security_msg_header(word):
    data = {
        'data_db_type': 'Security Message Header'
    }
    frame_type = 'security_msg_header'
    protocol_version = (word) & 0xFF
    _message_type = (word >> (8*1)) & 0xFF
    param1 = (word >> (8*2)) & 0xFF
    param2 = (word >> (8*3)) & 0xFF
    if protocol_version == 0x10 and protocol_version == 0x01:
        data['protocol_version'] = str('Version 1.0')
    else:
        data['protocol_version'] = str('Reserved')
    if message_type_security.get(_message_type, None) == None:
        data['message_type'] = str('Reserved')
    else:
        data['message_type'] = message_type_security(_message_type)
    if data['message_type'] == 'GET_DIGESTS':
        data['param1'] = param1
        data['param2'] = str('Reserved')
    elif data['message_type'] == 'GET_CERTIFICATE':
        data['param1'] = param1
        data['param2'] = str('Reserved')
    elif data['message_type'] == 'DIGESTS(Response)':
        data['param1'] = str(hex(param1))
        data['param2'] = str(bin(param2))
    elif data['message_type'] == 'CERTIFICATE(Response)':
        data['param1'] = param1
        data['param2'] = str('Reserved')
    elif data['message_type'] == 'CHALLENGE_AUTH(Response)':
        data['param1'] = param1
        data['param2'] = str(bin(param2))
    else:
        data['param1'] = str('Reserved')
        data['param2'] = str('Reserved') 
    
    return frame_type, data
    
def decode_get_certificate(word):
    data = {
        'data_db_type': 'GET_CERTIFICATE Payload'
    }
    frame_type = 'get_certificate_request'
    offset = (word) & 0xFFFF
    length = (word >> (8*2)) & 0xFFFF
    data['offset'] = offset
    data['length'] = length
    
    return frame_type, data
    
def decode_challenge_auth_response_payload1(word):
    data = {
        'data_db_type': 'Challenge AUTH response Payload'
    }
    frame_type = 'challenge_auth_reponse_payload1'
    min_protocol_ver = (word) & 0xFF
    max_protocol_ver = (word >> (8*1)) & 0xFF
    capabilities = (word >> (8*2)) & 0xFF
    orgname = (word >> (8*3)) & 0xFF
    data['min_protocol_ver'] = min_protocol_ver
    data['max_protocol_ver'] = max_protocol_ver
    if capabilities == 0x1:
        data['capabilities'] = capabilities
    else:
        data['capabilities'] = str(f'{capabilities},Reserved')
    if orgname == 0x0:
        data['orgname'] = str('USB-IF')
    else:
        data['orgname'] = str(f'{orgname},Reserved')
    
    return frame_type, data
    
def decode_challenge_auth_response_payload2(word):
    data = {
        'data_db_type': 'Challenge AUTH response Payload'
    }
    frame_type = 'challenge_auth_reponse_payload2'
    certchainhash = (word) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF
    salt = (word >> (8*32)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF
    context_hash = (word) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF
    signature = (word) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF
    data['certchainhash'] = hex(certchainhash)
    data['salt'] = hex(salt)
    data['context_hash'] = hex(context_hash)
    data['signature'] = hex(signature)
    
    return frame_type, data
    
def decode_status(word, db_index):
    data = {
        'data_db_type': 'Status Data Block'
    }
    if db_index == 0:
        frame_type = 'SDB_0'
        internal_temp = (word) & 0xFF
        if internal_temp == 0:
            data['internal_temp'] = str('feature not supported')
        elif internal_temp == 1:
            data['internal_temp'] = str('temperture is less than 2℃')
        else:
            data['internal_temp'] = f'{internal_temp}2℃'
    if db_index == 1:
        frame_type = 'SDB_1'
        external_power_present = (word >> 1) & 0x1
        external_power_acdc = (word >> 2) & 0x1
        internal_power_from_battery = (word >> 3) & 0x1
        internal_power_from_non_battery = (word >> 4) & 0x1
        data['external_power_present'] = external_power_present
        if external_power_acdc == 0x0 and external_power_present == 1:
            data['external_power_acdc'] = str('DC')
        elif external_power_acdc == 0x1 and external_power_present == 1:
            data['external_power_acdc'] = str('AC')
        else:
            data['external_power_acdc'] = str('Reserved')
        data['internal_power_from_battery'] = internal_power_from_battery
        data['internal_power_from_non_battery'] = internal_power_from_non_battery
    if db_index == 2:
        frame_type = 'SDB_2'
        hot_swappable_batt = (word >> 4) & 0xF
        fixed_batt = (word) & 0xF
        data['hot_swappable_battery'] = hot_swappable_batt
        data['fixed_battery'] = fixed_batt
    if db_index == 3:
        frame_type = 'SDB_3'
        ocp = (word >> 1) & 0x1
        otp = (word >> 2) & 0x1
        ovp = (word >> 3) & 0x1
        cf_mode = (word >> 4) & 0x1
        data['ocp'] = ocp
        data['otp'] = otp
        data['ovp'] = ovp
        if cf_mode == 0x0:
            data['cf_mode'] = f'{cf_mode},CV mode'
        else:
            data['cf_mode'] = f'{cf_mode},CF mode'
    if db_index == 4:
        frame_type = 'SDB_4'
        temperture_status = (word >> 1) & 0x3
        if temperture_status == 0x0:
            data['temperture_status'] = f'{bin(temperture_status)},Not Supported'
        elif temperture_status == 0x1:
            data['temperture_status'] = f'{bin(temperture_status)},Normal'
        elif temperture_status == 0x2:
            data['temperture_status'] = f'{bin(temperture_status)},Warning'
        elif temperture_status == 0x3:
            data['temperture_status'] = f'{bin(temperture_status)},Over temperture'    
        else:
            data['temperture_status'] = str('Reserved')
    if db_index == 5:
        frame_type = 'SDB_5'
        power_status = (word) & 0xFF
        if power_status == 0x1:
            data['power_status'] = f'{hex(power_status)}, Power limited due to Cable supported current'
        elif power_status == 0x2:
            data['power_status'] = f'{hex(power_status)}, Power limited due to insufficient power available while sourcing other ports'
        elif power_status == 0x3:
            data['power_status'] = f'{hex(power_status)}, Power limited due to insufficient external power'
        elif power_status == 0x4:
            data['power_status'] = f'{hex(power_status)}, Power limited due to Event Flags in place'    
        elif power_status == 0x5:
            data['power_status'] = f'{hex(power_status)}, Power limited due to temperature'
        else:
            data['power_status'] = f'{hex(power_status)}, Reserved'
    if db_index == 6:
        frame_type = 'SDB_6'
        new_power_status = (word) & 0x7
        new_power_state_indicator = (word >> 3) & 0x7
        if new_power_status == 0x0:
            data['new_power_status'] = f'{hex(new_power_status)}, Status not supported'
        elif new_power_status == 0x1:
            data['new_power_status'] = f'{hex(new_power_status)}, S0'
        elif new_power_status == 0x2:
            data['new_power_status'] = f'{hex(new_power_status)}, Modern Standby'
        elif new_power_status == 0x3:
            data['new_power_status'] = f'{hex(new_power_status)}, S3'
        elif new_power_status == 0x4:
            data['new_power_status'] = f'{hex(new_power_status)}, S4'
        elif new_power_status == 0x5:
            data['new_power_status'] = f'{hex(new_power_status)}, S5(Off with battery, wake events supported)'
        elif new_power_status == 0x6:
            data['new_power_status'] = f'{hex(new_power_status)}, G3(Off with no battery, wake events not supported)'
        else:
            data['new_power_status'] = f'{hex(new_power_status)}, Reserved'
        if new_power_state_indicator == 0x0:
            data['new_power_state_indicator'] = f'{hex(new_power_state_indicator)}, Off LED'
        elif new_power_state_indicator == 0x1:
            data['new_power_state_indicator'] = f'{hex(new_power_state_indicator)}, On LED'
        elif new_power_state_indicator == 0x2:
            data['new_power_state_indicator'] = f'{hex(new_power_state_indicator)}, Blinking LED'
        elif new_power_state_indicator == 0x3:
            data['new_power_state_indicator'] = f'{hex(new_power_state_indicator)}, Breathing LED'
        else:
            data['new_power_state_indicator'] = f'{hex(new_power_status)}, Reserved'
            
    return frame_type, data
    
def decode_battery_cap(word):
    data = {
        'data_db_type': 'Get_Battery_Cap DB'
    }
    frame_type = 'GBCDB'
    batt_cap_ref = (word) & 0xFF
    if batt_cap_ref == 0 or batt_cap_ref == 1 or batt_cap_ref == 2 or batt_cap_ref == 3:
        data['batt_cap_ref'] = f'Fixed Batteries [{batt_cap_ref}]'
    elif batt_cap_ref == 4 or batt_cap_ref == 5 or batt_cap_ref == 6 or batt_cap_ref == 7:
        data['batt_cap_ref'] = f'Hot Swappable Batteries [{batt_cap_ref}]'
    else:
        data['internal_temp'] = f'Reserved [{batt_cap_ref}]'
            
    return frame_type, data
    
def decode_battery_status(word):
    data = {
        'data_db_type': 'Get_Battery_Status DB'
    }
    frame_type = 'GBSDB'
    batt_cap_ref = (word) & 0xFF
    if batt_cap_ref == 0 or batt_cap_ref == 1 or batt_cap_ref == 2 or batt_cap_ref == 3:
        data['batt_cap_ref'] = f'Fixed Batteries [{batt_cap_ref}]'
    elif batt_cap_ref == 4 or batt_cap_ref == 5 or batt_cap_ref == 6 or batt_cap_ref == 7:
        data['batt_cap_ref'] = f'Hot Swappable Batteries [{batt_cap_ref}]'
    else:
        data['internal_temp'] = f'Reserved [{batt_cap_ref}]'
            
    return frame_type, data
    
def decode_battery_capabilities(word):
    data = {
        'data_db_type': 'Battery_Capability DB'
    }
    frame_type = 'BCDB'
    vid = (word) & 0xFFFF
    pid = (word >> (8*2)) & 0xFFFF
    battery_design_capacity = (word >> (8*4)) & 0xFFFF
    battery_last_full_charge_capacity = (word >> (8*6)) & 0xFFFF
    battery_type = (word >> (8*8)) & 0xFFFF
    data['vid'] = hex(vid)
    data['pid'] = hex(pid)
    if battery_design_capacity == 0x0000:
        data['battery_design_capacity'] = f'{hex(battery_design_capacity)},Battery not present'
    elif battery_design_capacity == 0xFFFF:
        data['battery_design_capacity'] = f'{hex(battery_design_capacity)},design capacity unknown'
    else:
        data['battery_design_capacity'] = f'{(battery_design_capacity)*0.1}WH'
    if battery_last_full_charge_capacity == 0x0000:
        data['battery_last_full_charge_capacity'] = f'{hex(battery_last_full_charge_capacity)},Battery not present'
    elif battery_last_full_charge_capacity == 0xFFFF:
        data['battery_last_full_charge_capacity'] = f'{hex(battery_last_full_charge_capacity)},last full charge capacity unknown'
    else:
        data['battery_last_full_charge_capacity'] = f'{(battery_last_full_charge_capacity)*0.1}WH'
    if battery_type == 0x0:
        data['battery_type'] = f'{hex(battery_type)},Invalid Battery reference'
    else:
        data['battery_type'] = f'{hex(battery_type)},Reserved'
    
    return frame_type, data
    
def decode_get_manufacturer_info(word):
    data = {
        'data_db_type': 'Get_Manufacturer_Info DB'
    }
    frame_type = 'GMIDB'
    manufacturer_info_target = (word) & 0xFF
    manufacturer_info_ref = (word >> 8) & 0xFF
    if manufacturer_info_target == 0:
        data['manufacturer_info_target'] = f'{hex(manufacturer_info_target)},Port/Cable Plug'
        data['manufacturer_info_ref'] = f'{hex(manufacturer_info_ref)},Reserved'
    elif manufacturer_info_target == 1:
        data['manufacturer_info_target'] = f'{hex(manufacturer_info_target)},Battery'
        if manufacturer_info_ref == 0 or manufacturer_info_ref == 1 or manufacturer_info_ref == 2 or manufacturer_info_ref == 3:
            data['manufacturer_info_ref'] = f'Fixed Batteries [{manufacturer_info_ref}]'
        elif manufacturer_info_ref == 4 or manufacturer_info_ref == 5 or manufacturer_info_ref == 6 or manufacturer_info_ref == 7:
            data['manufacturer_info_ref'] = f'Hot Swappable Batteries [{manufacturer_info_ref}]'
    else:
        data['manufacturer_info_target'] = f'{hex(manufacturer_info_target)},Reserved'
        data['manufacturer_info_ref'] = f'{hex(manufacturer_info_ref)},Reserved'
    
    return frame_type, data
    
def decode_manufacturer_info(word, db_index):
    data = {
        'data_db_type': 'Manufacturer_Info DB'
    }
    frame_type = 'MIDB'
    manufacturer_string = chr((word >> (8*4)) & 0xFF)
    for i in range(5, db_index):
        manufacturer_string = manufacturer_string + chr((word >> (8*i)) & 0xFF)
    vid = (word) & 0xFFFF
    pid = (word >> (8*2)) & 0xFFFF
    data['vid'] = hex(vid)
    data['pid'] = hex(pid)
    data['manufacturer_string'] = manufacturer_string
    
    return frame_type, data
    
def decode_pps_status(word):
    data = {
        'data_db_type': 'PPS_Status DB'
    }
    frame_type = 'ppssdb'
    output_voltage = (word) & 0xFFFF
    output_current = (word >> (8*2)) & 0xFF
    real_time_flags = (word >> (8*3)) & 0xFF
    ptf = (real_time_flags >> 1) & 0x3
    omf = (real_time_flags >> 3) & 0x1
    if output_voltage == 0xFFFF:
        data['output_voltage'] = f'{hex(output_voltage)},Not supported'
    else:
        data['output_voltage'] = f'{(output_voltage)*20}mV'
    if output_current == 0xFF:
        data['output_current'] = f'{hex(output_current)},Not supported'
    else:
        data['output_current'] = f'{(output_current)*50}mA'
    if ptf == 0x0:
        data['ptf'] = f'[{hex(ptf)}],Not Supported'
    elif ptf == 0x1:
        data['ptf'] = f'[{hex(ptf)}],Normal'
    elif ptf == 0x2:
        data['ptf'] = f'[{hex(ptf)}],Warning'
    elif ptf == 0x3:
        data['ptf'] = f'[{hex(ptf)}],Over temperature'
    if omf == 0x0:
        data['omf'] = f'[{omf}],Constant Voltage mode'
    else:
        data['omf'] = f'[{omf}],Current Limit mode'
    
    return frame_type, data
    
def decode_country_codes(word):
    data = {
        'data_db_type': 'Country Codes DB'
    }
    frame_type = 'ccdb'
    length = (word) & 0xFF
    data['length'] = length
    country_code = []
    for index in range(2, 2*(length+1), 2):
        first_char = (word >> (8*index)) & 0xFF
        second_char = (word >> (8*(index+1))) & 0xFF
        country_code.append(f' Country Code[{index}]: [{char(first_char)}{char(second_char)}] ')
    data['country_code'] = country_code
    
    return frame_type, data
    
def decode_country_info(word, db_index):
    data = {
        'data_db_type': 'Country Info DB'
    }
    frame_type = 'cidb'
    first_char = (word) & 0xFF
    second_char = (word >> (8*1)) & 0xFF
    data['country_code'] = f'{char(first_char)}{char(second_char)}'
    country_specific_data = []
    for index in range(4, db_index):
        country_specific_char = (word >> (8*index)) & 0xFF
        country_specific_data.append(f'{char(country_specific_char)}')
    data['country_specific_data'] = country_specific_data
    
    return frame_type, data
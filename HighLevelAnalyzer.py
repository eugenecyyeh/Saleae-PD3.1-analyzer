from saleae.analyzers import HighLevelAnalyzer, AnalyzerFrame, StringSetting, NumberSetting, ChoicesSetting
from saleae.data import GraphTime, GraphTimeDelta

from MessageHandling import *

encoding_lookup = {
    0B0000: 0B11110,
    0B0001: 0B01001,
    0B0010: 0B10100,
    0B0011: 0B10101,
    0B0100: 0B01010,
    0B0101: 0B01011,
    0B0110: 0B01110,
    0B0111: 0B01111,
    0B1000: 0B10010,
    0B1001: 0B10011,
    0B1010: 0B10110,
    0B1011: 0B10111,
    0B1100: 0B11010,
    0B1101: 0B11011,
    0B1110: 0B11100,
    0B1111: 0B11101,
}

Preamble_LSB ={
    'Preamble': [0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1],
    'Preamble missing first of UI': [1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1],
}

addresses = {
    'SOP': [1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1],
    'SOP_prime': [1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0],
    'SOP_double_prime': [1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0],
    'Hard Reset': [0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1],
    'Cable Reset': [0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 0],
    'SOP_prime_debug': [1, 1, 0, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 0],
    'SOP_double_prime_debug': [1, 1, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 0, 0, 1],
}

EOP_LSB = {
    'EOP': [1,0,1,1,0],
}

data_commands = {
    0b00000: 'Reserved',
    0b00001: 'Source_Capabilities',
    0b00010: 'Request',
    0b00011: 'BIST',
    0b00100: 'Sink_Capabilities',
    0b00101: 'Battery_Status',
    0b00110: 'Alert',
    0b00111: 'Get_Country_Info',
    0b01000: 'Enter_USB',
    0b01001: 'EPR_Request',
    0b01010: 'EPR_Mode',
    0b01011: 'Source_Info',
    0b01100: 'Revision',
    0b01101: 'Reserved',
    0b01110: 'Reserved',
    0b01111: 'Vendor_Defined',
    0b10000: 'Reserved',
    0b10001: 'Reserved',
    0b10010: 'Reserved',
    0b10011: 'Reserved',
    0b10100: 'Reserved',
    0b10101: 'Reserved',
    0b10110: 'Reserved',
    0b10111: 'Reserved',
    0b11000: 'Reserved',
    0b11001: 'Reserved',
    0b11010: 'Reserved',
    0b11011: 'Reserved',
    0b11100: 'Reserved',
    0b11101: 'Reserved',
    0b11110: 'Reserved',
    0b11111: 'Reserved'
}

control_commands = {
    0b00000: 'Reserved',
    0b00001: 'GoodCRC',
    0b00010: 'GotoMin',
    0b00011: 'Accept',
    0b00100: 'Reject',
    0b00101: 'Ping',
    0b00110: 'PS_RDY',
    0b00111: 'Get_Source_Cap',
    0b01000: 'Get_Sink_Cap',
    0b01001: 'DR_Swap',
    0b01010: 'PR_Swap',
    0b01011: 'VCONN_Swap',
    0b01100: 'Wait',
    0b01101: 'Soft_Reset',
    0b01110: 'Data_Reset',
    0b01111: 'Data_Reset_Complete',
    0b10000: 'Not_Supported',
    0b10001: 'Get_Source_Cap_Extended',
    0b10010: 'Get_Status',
    0b10011: 'FR_Swap',
    0b10100: 'Get_PPS_Status',
    0b10101: 'Get_Country_Codes',
    0b10110: 'Get_Sink_Cap_extended',
    0b10111: 'Get_Source_Info',
    0b11000: 'Get_Revision',
    0b11001: 'Reserved',
    0b11010: 'Reserved',
    0b11011: 'Reserved',
    0b11100: 'Reserved',
    0b11101: 'Reserved',
    0b11110: 'Reserved',
    0b11111: 'Reserved',
}

extended_commands = {
    0b00000: 'Reserved',
    0b00001: 'Source_Capabilities_Extended',
    0b00010: 'Status',
    0b00011: 'Get_Battery_Cap',
    0b00100: 'Get_Battery_Status',
    0b00101: 'Battery_Capabilities',
    0b00110: 'Get_Manufacturer_Info',
    0b00111: 'Manufacturer_Info',
    0b01000: 'Security_Request',
    0b01001: 'Security_Response',
    0b01010: 'Firmware_Update_Request',
    0b01011: 'Firmware_Update_Response',
    0b01100: 'PPS_Status',
    0b01101: 'Country_Info',
    0b01110: 'Country_Codes',
    0b01111: 'Sink_Capabilities_Extended',
    0b10000: 'Extended_Control',
    0b10001: 'EPR_Source_Capabilities',
    0b10010: 'EPR_Sink_Capabilities',
    0b10011: 'Reserved',
    0b10100: 'Reserved',
    0b10101: 'Reserved',
    0b10110: 'Reserved',
    0b10111: 'Reserved',
    0b11000: 'Reserved', 
    0b11001: 'Reserved',
    0b11010: 'Reserved',
    0b11011: 'Reserved',
    0b11100: 'Reserved',
    0b11101: 'Reserved',
    0b11110: 'Vendor_Defined_Extended',
    0b11111: 'Reserved',
}

power_port_role = {
    0: 'Sink',
    1: 'Source'
}
cable_plug = {
    0: 'from DFP or UFP',
    1: 'from cable plug'
}

revision = {
    0b00: '1.0',
    0b01: '2.0',
    0b10: '3.0',
    0b11: 'Reserved'
}

port_data_role = {
    0: 'UFP',
    1: 'DFP'
}


class Word():
    start_time = None
    end_time = None
    data = None

    def __init__(self, start_time, end_time, data):
        self.start_time = start_time
        self.end_time = end_time
        self.data = data

class Hla(HighLevelAnalyzer):

    result_types = {
        'preamble': {'format': '{{data.preamble}}'},
        
        'address': {'format': '{{data.address}}'},

        'header': {'format': '[Message Header][{{data.command_code}}]--Message ID: [{{data.message_id}}]--Number of Objects: [{{data.number_of_objects}}]--Spec Rev: [{{data.spec_revision}}]'},

        'source_fixed_supply_pdo': {'format': '[{{data.data_object_type}}][{{data.raw}}] [{{data.pdo_type}}] [{{data.voltage_V}}/{{data.maximum_current_A}}] DRP: [{{data.dual_role_power}}]--USB Suspend Supported: [{{data.usb_suspend_supported}}]--USB Communications Supported: [{{data.usb_communications_capable}}]--DRD: [{{data.dual_role_data}}]--Unchecked Ext. Messages Supported: [{{data.unchecked_extended_messages_supported}}]--EPR Capable: [{{data.epr_mode_capable}}]--Peak Current=[{{data.peak_current}}]'},

        'source_variable_supply_pdo': {'format': '[{{data.data_object_type}}][{{data.raw}}] [{{data.pdo_type}}] Max_Voltage=[{{data.maximum_voltage_V}}]--Min_Voltage=[{{data.minimum_voltage_V}}]--Max_Current=[{{data.maximum_current_A}}]'},

        'source_battery_supply_pdo': {'format': '[{{data.data_object_type}}][{{data.raw}}] [{{data.pdo_type}}] Max_Voltage=[{{data.maximum_voltage_V}}]--Min_Voltage=[{{data.minimum_voltage_V}}]--Max_allowable_power=[{{data.maximum_allowable_power_W}}]'},

        'spr_source_programmable_supply_pdo': {'format': '[{{data.data_object_type}}][{{data.raw}}] [{{data.pdo_type}}] Max_Voltage=[{{data.maximum_voltage_V}}]--Min_voltage=[{{data.minimum_voltage_V}}]--Max_Current=[{{data.maximum_current_A}}]'},
        
        'epr_source_adjustable_voltage_supply_pdo': {'format': '[{{data.data_object_type}}][{{data.raw}}] [{{data.pdo_type}}] Max_Voltage=[{{data.maximum_voltage_V}}]--Min_voltage=[{{data.minimum_voltage_V}}]--PDP=[{{data.PDP}}]--Peak Current=[{{data.peak_current}}]'},

        'sink_fixed_supply_pdo': {'format': '[{{data.data_object_type}}][{{data.raw}}] [{{data.pdo_type}}] Voltage=[{{data.voltage_V}}]--Operational_Current=[{{data.operational_current_A}}]--DRP: [{{data.dual_role_power}}]--Higher Capability: [{{data.higher_capability}}]--Unconstrained Power: [{{data.unconstrained_power}}]--USB Communications Supported: [{{data.usb_communications_capable}}]--DRD: [{{data.dual_role_data}}]--FRS Required Current: [{{data.fast_role_swap_required_current}}]'},

        'sink_variable_supply_pdo': {'format': '[{{data.data_object_type}}][{{data.raw}}] [{{data.pdo_type}}] Max_Voltage=[{{data.maximum_voltage_V}}]--Min_Voltage=[{{data.minimum_voltage_V}}]--Max_Current=[{{data.maximum_current_A}}]'},

        'sink_battery_supply_pdo': {'format': '[{{data.data_object_type}}][{{data.raw}}] [{{data.pdo_type}}] Max_Voltage=[{{data.maximum_voltage_V}}]--Min_Voltage=[{{data.minimum_voltage_V}}]--Max_allowable_power=[{{data.maximum_allowable_W}}]'},

        'sink_programmable_supply_pdo': {'format': '[{{data.data_object_type}}][{{data.raw}}] [{{data.pdo_type}}] Max_Voltage=[{{data.maximum_voltage_V}}]--Min_voltage=[{{data.minimum_voltage_V}}]; Max_current=[{{data.maximum_current_A}}]'},

        'bist_bdo': {'format': '[{{data.data_object_type}}] [{{data.index}}] BIST Mode: {{data.bist_mode}}'},
        
        'bist_test_data': {'format': '[{{data.data_object_type}}] [{{data.index}}] [{{data.raw}}]'},

        'fixed_supply_rdo': {'format': 'Obj:[{{data.object_position}}] Oper_Current=[{{data.operating_current_A}}]--Max_Oper_Current=[{{data.maximum_operating_current_A}}]--Giveback Flag: [{{data.giveback_flag}}]--Capability Missmatch: [{{data.capability_mismatch}}]--Usb_communications_capable: [{{data.usb_communications_capable}}]--No_usb_suspend: [{{data.no_usb_suspend}}]--Unchunked_extended_messages_supported: [{{data.unchunked_extended_messages_supported}}]--ERP capable: [{{data.erp_mode_capable}}]'},
        
        'fixed_supply_rdo_giveback': {'format': 'Obj:[{{data.object_position}}] Oper_Current=[{{data.operating_current_A}}]--Min_Oper_Current=[{{data.minimum_operating_current_A}}]--Giveback Flag: [{{data.giveback_flag}}]--Capability Missmatch: [{{data.capability_mismatch}}]--Usb_communications_capable: [{{data.usb_communications_capable}}]--No_usb_suspend: [{{data.no_usb_suspend}}]--Unchunked_extended_messages_supported: [{{data.unchunked_extended_messages_supported}}]--ERP capable: [{{data.erp_mode_capable}}]'},

        'variable_supply_rdo': {'format': 'Obj:[{{data.object_position}}] Oper_current=[{{data.operating_current_A}}]--Max_oper_current=[{{data.maximum_operating_current_A}}]--Giveback Flag: [{{data.giveback_flag}}]--Capability Missmatch: [{{data.capability_mismatch}}]--Usb_communications_capable: [{{data.usb_communications_capable}}]--No_usb_suspend: [{{data.no_usb_suspend}}]--Unchunked_extended_messages_supported: [{{data.unchunked_extended_messages_supported}}]--ERP capable: [{{data.erp_mode_capable}}]'},
        
        'variable_supply_rdo_giveback': {'format': 'Obj:[{{data.object_position}}] Operating_current=[{{data.operating_current_A}}]--Min_operating_current=[{{data.minimum_operating_current_A}}]--Giveback Flag: [{{data.giveback_flag}}]--Capability Missmatch: [{{data.capability_mismatch}}]--Usb_communications_capable: [{{data.usb_communications_capable}}]--No_usb_suspend: [{{data.no_usb_suspend}}]--Unchunked_extended_messages_supported: [{{data.unchunked_extended_messages_supported}}]--ERP capable: [{{data.erp_mode_capable}}]'},

        'battery_rdo': {'format': 'Obj:[{{data.object_position}}] Operating_Power=[{{data.operating_power_W}}]--Max_Operating_Power=[{{data.maximum_operating_power_W}}]--Giveback_flag: [{{data.giveback_flag}}]--Capability_mismatch: [{{data.capability_mismatch}}]--Usb_communications_capable: [{{data.usb_communications_capable}}]--No_usb_suspend: [{{data.no_usb_suspend}}]--Unchunked_extended_messages_supported: [{{data.unchunked_extended_messages_supported}}]--ERP capable: [{{data.erp_mode_capable}}]'},
        
        'battery_rdo_giveback': {'format': 'Obj:[{{data.object_position}}] Operating_Power=[{{data.operating_power_W}}]--Min_Operating_Power=[{{data.minimum_operating_power_W}}]--Giveback_flag: [{{data.giveback_flag}}]--Capability_mismatch: [{{data.capability_mismatch}}]--Usb_communications_capable: [{{data.usb_communications_capable}}]--No_usb_suspend: [{{data.no_usb_suspend}}]--Unchunked_extended_messages_supported: [{{data.unchunked_extended_messages_supported}}]--ERP capable: [{{data.erp_mode_capable}}]'},

        'pps_rdo': {'format': 'Obj: [{{data.object_position}}] Output_Voltage=[{{data.output_voltage_V}}]--Operating_Current=[{{data.operating_current_A}}]--Capability_mismatch: [{{data.capability_mismatch}}]--Usb_communications_capable: [{{data.usb_communications_capable}}]--No_usb_suspend: [{{data.no_usb_suspend}}]--Unchunked_extended_messages_supported: [{{data.unchunked_extended_messages_supported}}]--ERP capable: [{{data.erp_mode_capable}}]'},
        
        'avs_rdo': {'format': 'Obj: [{{data.object_position}}] Output_Voltage=[{{data.output_voltage_V}}]--Operating_Current=[{{data.operating_current_A}}]--Capability_mismatch: [{{data.capability_mismatch}}]--Usb_communications_capable: [{{data.usb_communications_capable}}]--No_usb_suspend: [{{data.no_usb_suspend}}]--Unchunked_extended_messages_supported: [{{data.unchunked_extended_messages_supported}}]--ERP capable: [{{data.erp_mode_capable}}]'},

        #For PD3.1
        'structured_header_vdo_31': {'format': '[{{data.data_object_type}}][{{data.raw}}] [{{data.command}}]({{data.command_type}})--VDM_Type: [{{data.vdm_type}}]--SVID: [{{data.vendor_id}}]--VDM_VER_Major: [{{data.structured_vdm_version_major}}]--VDM_VER_Minor--[{{data.structured_vdm_version_minor}}]--OBJ_position: [{{data.object_position}}]'},

        'unstructured_header_vdo': {'format': '[{{data.data_object_type}}][{{data.raw}}] Vendor_id: [{{data.vendor_id}}]--Vdm_type: [{{data.vdm_type}}]'},

        'bsdo': {'format': '[{{data.data_object_type}}][{{data.raw}}] Battery Capacity: [{{data.battery_preset_Capacity_WH}}WH]--Invalid_battery_reference: [{{data.invalid_battery_reference}}]--Battery_present: [{{data.battery_present}}]--Battery_charging_status: [{{data.battery_charging_status}}]'},

        'ado': {'format': ']{{data.data_object_type}}] Fixed_batteries: [{{data.fixed_batteries}}]--hot_swappable_batteries: [{{data.hot_swappable_batteries}}]--Battery_status_change_event: [{{data.battery_status_change_event}}]--Ocp_event: [{{data.ocp_event}}]--Otp_event: [{{data.otp_event}}]--Operating_condition_change: [{{data.operating_condition_change}}]--Source_input_change: [{{data.source_input_change}}]--Ovp_event: [{{data.ovp_event}}]'},

        'ccdo': {'format': '[{{data.data_object_type}}] Country_code: [{{data.country_code}}]'},

        'eudo': {'format': '[{{data.data_object_type}}] Usb_mode:[{{data.usb_mode}}]--Usb4_drd:[{{data.usb4_drd}}]--Usb3_drd:[{{data.usb3_drd}}]--Cable_speed:[{{data.cable_speed}}]--Cable_type:[{{data.cable_type}}]--Cable_current:[{{data.cable_current}}]--Pcie_support:[{{data.pcie_support}}]--Dp_support:[{{data.dp_support}}]--TBT_support:[{{data.tbt_support}}]--Host_present:[{{data.host_present}}]'},

        'object': {'format': '[{{data.index}}] [{{data.data}}]'},

        'crc': {'format': 'CRC: {{data.crc}}'},

        'eop': {'format': '{{data.eop}}'},

        'error': { 'format': 'error: {{{data.error}}} [{{data.raw}}]' },
        
        'id_header_vdo': { 'format': '[{{data.data_object_type}}][{{data.raw}}] USB Capable as Host: [{{data.usb_communications_capable_as_usb_host}}]--USB capable as Device: [{{data.usb_communications_capable_as_usb_device}}]--Product Type UFP: [{{data.product_type_ufp}}]--Product Type DFP: [{{data.product_type_dfp}}]--Modal Operation Supported: [{{data.modal_operation_supported}}]--Connector Type: [{{data.connector_type}}]--USB vendor ID: [{{data.usb_vendor_id}}]'},
        
        'cert_stat_vdo': { 'format': '[{{data.data_object_type}}][{{data.raw}}]'},
        
        'product_vdo': { 'format': '[{{data.data_object_type}}][{{data.raw}}] USB Product ID: [{{data.usb_product_id}}]--bcdDevice: [{{data.bcddevice}}]'},
        
        'ufp_vdo1': { 'format': '[{{data.data_object_type}}][{{data.raw}}] [{{data.ufp_vdo1_ver}}] USB4 Device Capable:[{{data.usb4_capable}}]--USB3.2 Device Capable:[{{data.usb3_capable}}]--USB2 Device Capable(Billboard only):[{{data.usb2_capable_billboardonly}}]--USB2 Device Capable:[{{data.usb2_capable}}]--Connector Type:[{{data.ufp_vdo1_connector_type}}]--USB Highest Speed:[{{data.usb_highest_speed}}]--Support ALT Modes reconfigured the signals on USB2 except for TBT3:[{{data.supports_alt_modes_reconfigured_signals_on_usb2}}]--Support ALT Modes not reconfigured the signals on USB2:[{{data.supports_alt_modes_do_not_reconfigured_signals_on_usb2}}]--Support TBT3 ALT Mode:[{{data.support_tbt3_alt_mode}}]'},
        
        'ufp_vdo2': { 'format': '[{{data.data_object_type}}][{{data.raw}}] USB4 Min Power: [{{data.usb4_min_power}}W]--USB4 Max Power: [{{data.usb4_max_power}}W]--USB3 Min Power: [{{data.usb3_min_power}}W]--USB3 Max Power: [{{data.usb3_max_power}}W]'},
        
        'dfp_vdo': { 'format': '[{{data.data_object_type}}][{{data.raw}}] [{{data.dfp_vdo_ver}}] USB4 Host Capable: [{{data.usb4_host_capable}}]--USB3.2 Host Capable: [{{data.usb3_host_capable}}]--USB2 Host Capable: [{{data.usb2_host_capable}}]--Connector Type: [{{data.dfp_vdo_connector_type}}]--Port Number: [{{data.port_number}}]'},
        
        'ama_vdo': { 'format': '[{{data.data_object_type}}][{{data.raw}}] [{{data.vdo_version}}] HW Version: [{{data.hw_version}}]--FW Version: [{{data.fw_version}}]--Vconn Power: [{{data.vconn_power}}]--Vconn required: [{{data.vconn_required}}]--Vbus required: [{{data.vbus_required}}]--USB Highest Speed: [{{data.ama_usb_highest_speed}}]'},
        
        'vdp_vdo': { 'format': '[{{data.data_object_type}}][{{data.raw}}] [{{data.vdo_version}}] HW Version: [{{data.hw_version}}]--FW Version: [{{data.fw_version}}]--Max_Vbus_Voltage: [{{data.maximum_vbus_voltage}}]--Charge Through Current Support: [{{data.charge_through_current_support}}]--Vbus Impedance: [{{data.vbus_impedance}}mohm]--Ground Impedance: [{{data.ground_impedance}}mohm]--Charge Through Support: [{{data.charge_through_support}}]'},
        
        'activecable_vdo1': { 'format': '[{{data.data_object_type}}][{{data.raw}}] [{{data.vdo_version}}] HW Version: [{{data.hw_version}}]--FW Version: [{{data.fw_version}}]--Connector Type: [{{data.connector_type}}]--Cable Latency: [{{data.cable_latency}}]--Cable Termination Type: [{{data.cable_terminiation_type}}]--Max Vbus Voltage: [{{data.maximum_vbus_voltage}}]--SBU Supported: [{{data.sbu_supported}}]--SBU Type: [{{data.sbu_type}}]--Vbus Current Handling Capability: [{{data.vbus_current_handling_capability}}]--VBUS Through Cable: [{{data.vbus_through_cable}}]--SOP" Present: [{{data.sop_double_prime_controller_present}}]--USB Highest Speed: [{{data.usb_highest_speed}}]'},
        
        'activecable_vdo2': { 'format': '[{{data.data_object_type}}][{{data.raw}}] Maximum Operating Temperature: [{{data.maximum_operating_temperature}}]--Shutdown Temperature: {{data.shutdown_temperature}}]--U3/CLd Power: [{{data._u3cld_power}}]--U3toU0 transition mode: [{{data.u3tou0_transition_mode}}]--Physical connection: [{{data.physical_connection}}]--Active element: [{{data.active_element}}]--USB4 Supported: [{{data.usb4_supported}}]--USB2 Hub Hops Consumed: [{{data.usb2_hub_hops_consumed}}]--USB2 Supported: [{{data.usb2_supported}}]--USB3.2 Supported: [{{data.usb3_supported}}]--USB Lanes Supported: [{{data.usb_lanes_supported}}]--Optically Isolated Active Cable: [{{data.optically_isolated_active_cable}}]--USB Gen: [{{data.usb_gen}}'},
        
        'passivecable_vdo': { 'format': '[{{data.data_object_type}}][{{data.raw}}] [{{data.vdo_version}}] HW Version: [{{data.hw_version}}]--FW Version: [{{data.fw_version}}]--Connector Type: [{{data.connector_type}}]--Cable Latency: [{{data.cable_latency}}]--Cable Termination Type: [{{data.cable_terminiation_type}}]--Max Vbus Voltage: [{{data.maximum_vbus_voltage}}]--Vbus Current Handling Capability: [{{data.vbus_current_handling_capability}}]--USB Highest Speed: [{{data.usb_highest_speed}}]'},
        
        'dsvid_vdo': { 'format': '[{{data.data_object_type}}][{{data.raw}}] SVID{{data.svidn_number}}: [{{data.svidn}}]--SVID{{data.svidn1_number}}: [{{data.svidn1}}]'},
        
        'dp_mode': { 'format': '[{{data.data_object_type}}][{{data.raw}}] Mode[{{data.mode_index}}]--UFP_D pin assignment: [{{data.ufp_d_pin_assignment_supported}}]--DFP_D pinassignment: [{{data.dfp_d_pin_assignment_supported}}]--USBr2.0 signaling not used: [{{data.usb2_signaling_not_used}}]--[{{data.receptacle_indication}}]--[{{data.signaling_for_transport_of_dp_protocol}}]--Port capability: [{{data.port_capability}}]'},
        
        'dp_status': { 'format': '[{{data.data_object_type}}][{{data.raw}}]--HPD status: [{{data.hpd_state}}]--DFP/UFP connected: [{{data.dfp_ufp_connected}}]--[{{data.irq_hpd}}]--Exit DisplayPort mode request: [{{data.exit_dp_mode_request}}]--[{{data.usb_config_request}}]--[{{data.multifunction_preferred}}]--[{{data.enabled}}]--[{{data.power_low}}]'},
        
        'dp_configure': { 'format': '[{{data.data_object_type}}][{{data.raw}}]--Configure UFP_U Pin Assignment: [{{data.configure_ufp_pin_assignment}}]--[{{data.signaling_for_transport_of_dp_protocol}}]--[{{data.select_configuration}}]'},
        
        'tbt_mode_adapter': { 'format': '[{{data.data_object_type}}][{{data.raw}}]--[{{data.tbt_alt_mode}}]--[{{data.legacy_tbt_adapter}}]'},
        
        'tbt_mode_device': { 'format': '[{{data.data_object_type}}][{{data.raw}}]--[{{data.tbt_alt_mode}}]--[{{data.legacy_tbt_adapter}}]--Vpro Avaliable: [{{data.vpro_avaliable}}]'},
        
        'tbt_cable_mode': { 'format': '[{{data.data_object_type}}][{{data.raw}}]--[{{data.tbt_alt_mode}}]--Cable Speed: [{{data.cable_speed}}]--TBT Cable Gen: [{{data.tbt_cable_gen}}]--[{{data.cable_type}}]--[{{data.cable_active_passive}}]--[{{data.active_cable_plug_link_training}}]'},

        'tbt_enter_mode': { 'format': '[{{data.data_object_type}}][{{data.raw}}]--[{{data.tbt_alt_mode}}]--Cable Speed: [{{data.cable_speed}}]--TBT Cable Gen: [{{data.tbt_cable_gen}}]--[{{data.cable_type}}]--[{{data.cable_active_passive}}]--[{{data.active_cable_plug_link_training}}]--[{{data.dfp_legacy_tbt_adapter}}]--[{{data.vpro_dock_and_host}}]'},
        
        'tbt_attention': { 'format': '[{{data.data_object_type}}][{{data.raw}}]--Exit TBT Mode: [{{data.exit_tbt_mode_request}}]--USB2 Billboard Status: [{{data.usb2_billboard_status}}]--Legacy TBT mDP Cable Status: [{{data.legacy_tbt_mdp_cable_status}}]'},
        
        'epr_mode_do': { 'format': '[{{data.data_db_type}}][{{data.raw}}]--Action: [{{data.action}}]--Data: [{{data.data}}]'},
        
        'ext_header': { 'format': '[{{data.data_object_type}}][{{data.raw}}]--Chunked: [{{data.chunked}}]--Chunked Num: [{{data.chunked_number}}]--Req Chunk: [{{data.request_chunk}}]--Data Size: [{{data.data_size}}]'},
        
        'epr_mode_pdo_null': { 'format': '[{{data.data_object_type}}] NULL[{{data.raw}}]'},
        
        'epr_mode_chunk_request': { 'format': '(Request Chunk) NULL[{{data.raw}}]'},
        
        'epr_chunked_leftbytes': { 'format': '{{data.raw}}'},
        
        'null_rdo': { 'format': '[{{data.data_object_type}}] NULL[{{data.raw}}]'},
        
        'ecdb': { 'format': '[{{data.data_db_type}}][{{data.raw}}]--Type:[{{data.type}}]--Data:[{{data.data}}]'},
        
        'scedb': { 'format': '[{{data.data_db_type}}][{{data.raw}}]--VID: [{{data.vid}}]--PID: [{{data.pid}}]--XID: [{{data.xid}}]--FW ver: [{{data.fw_version}}]--HW ver: [{{data.hw_version}}]--Voltage Regulation: [{{data.voltage_regulation}}]--Holdup Time: [{{data.holdup_time}}]--Compliance: [{{data.compliance}}]--Touch Current: [{{data.touch_current}}]--Peak Current1: [{{data.peak_current1}}]--Peak Current2: [{{data.peak_current2}}]--Peak Current3: [{{data.peak_current3}}]--Touch Temp: [{{data.touch_temp}}]--Source Inputs: [{{data.source_inputs}}]--NUM of BATT slots: [{{data.num_of_batt_slots}}]--SPR Source PDP: [{{data.spr_source_pdp}}]--EPR Source PDP: [{{data.spr_source_pdp}}]'},
        
        'skedb': { 'format': '[{{data.data_db_type}}][{{data.raw}}]--VID: [{{data.vid}}]--PID: [{{data.pid}}]--XID: [{{data.xid}}]--FW ver: [{{data.fw_version}}]--HW ver: [{{data.hw_version}}]--SKEDB Ver: [{{data.sledb_version}}]--Load Step: [{{data.load_step}}]--Sink load charac: [{{data.sink_load_characteristics}}]--Compliance: [{{data.compliance}}]--Touch Temp: [{{data.touch_temp}}]--Battery info: [{{data.battery_info}}]--Sink Modes: [{{data.sink_modes}}]--Sink Min PDP: [{{data.sink_min_pdp}}]--Sink Operational PDP: [{{data.sink_operational_pdp}}]--Sink Max PDP: [{{data.sink_max_pdp}}]--EPR Sink Min PDP: [{{data.epr_sink_min_pdp}}]--EPR Sink Operational PDP: [{{data.epr_sink_operational_pdp}}]--EPR Sink Max PDP: [{{data.epr_sink_max_pdp}}]'},
        
        'fw_update_msg_header': { 'format': '[{{data.data_db_type}}][{{data.raw}}]--Protocol Version: [{{data.protocol_version}}]--MessageType: [{{data.message_type}}]'},
        
        'pdfu_null': {'format': 'Offset[{{data.offset}}] Payload: [{{data.raw}}]'},
        
        'pdfu_initiate_request': {'format': 'Offset[{{data.offset}}]--FW Version{{data.fw_version}}: [{{data.raw}}]'},
        
        'pdfu_datablock_index': {'format': 'Offset[{{data.offset}}]--Data Block Index: [{{data.datablock_index}}]'},
        
        'pdfu_datablock': {'format': 'Offset[{{data.offset}}]--Data Block: [{{data.datablock}}]'},
        
        'pdfu_vendor_specific_payload1': {'format': 'Offset[{{data.offset}}]--VID: [{{data.vid}}]'},
        
        'pdfu_vendor_specific_payload2': {'format': 'Offset[{{data.offset}}]--Vendor defined: [{{data.vendor_defined}}]'},
        
        'pdfu_getfw_id_response': {'format': '[{{data.data_db_type}}][{{data.raw}}]--Status: [{{data.status}}]--VID: [{{data.vid}}]--PID: [{{data.pid}}]--HW ver(Major): [{{data.hwversion_major}}]--HW ver(Minor): [{{data.hwversion_minor}}]--Si ver: [{{data.siversion}}]--FW ver1: [{{data.fwversion1}}]--FW ver2: [{{data.fwversion2}}]--FW ver3: [{{data.fwversion3}}]--FW ver4: [{{data.fwversion4}}]--ImageBank: [{{data.imagebank}}]--Flag1: [{{data.flags1}}]--Flag2: [{{data.flags2}}]--Flag3: [{{data.flags3}}]--Flag4: [{{data.flags4}}] Flags details refer PDFW spec V1.0'},
        
        'pdfu_initiate_response': {'format': '[{{data.data_db_type}}][{{data.raw}}]--Status: [{{data.status}}]--Wait time: [{{data.waittime}}]--MaxImage Size: [{{data.maximagesize}}]'},
        
        'pdfu_data_response': {'format': '[{{data.data_db_type}}][{{data.raw}}]--Status: [{{data.status}}]--Wait time: [{{data.waittime}}]--NumDataNR: [{{data.numdata_nr}}]--DataBlock Num: [{{data.datablock_num}}]'},
        
        'pdfu_validate_response': {'format': '[{{data.data_db_type}}][{{data.raw}}]--Status: [{{data.status}}]--Wait time: [{{data.waittime}}]--Flags: [{{data.flags}}]'},
        
        'pdfu_validate_response': {'format': '[{{data.data_db_type}}][{{data.raw}}]--Status: [{{data.status}}]'},
        
        'pdfu_vendor_specific_response_payload1': {'format': '[{{data.data_db_type}}][{{data.raw}}]--Status: [{{data.status}}]--VID: [{{data.vid}}]'},
        
        'pdfu_vendor_specific_response_payload2': {'format': 'Offset[{{data.offset}}]--Vendor defined: [{{data.vendor_defined}}]'},
        
        'security_msg_header': {'format': '[{{data.data_db_type}}][{{data.raw}}]--Protocol Version: [{{data.protocol_version}}]--MessageType: [{{data.message_type}}]--Param1: [{{data.param1}}]--Param2: [{{data.param2}}]'},
        
        'get_certificate_request': {'format': '[{{data.data_db_type}}][{{data.raw}}]--Offset: [{{data.offset}}]--Length: [{{data.length}}]'},
        
        'security_nonce': {'format': 'Offset: [{{data.offset}}]--Nonce: [{{data.nonce}}]'},
        
        'digest_response_playload': {'format': '[Digest Response Payload]--Digest[{{data.index}}]--Certificate Chain: [{{data.raw}}]'},
        
        'challenge_auth_reponse_payload1': {'format': '[Chllenge Auth Response Payload]--MinProtocolVer: [{{data.min_protocol_ver}}]--MaxProtocolVer: [{{data.max_protocol_ver}}]--Capabilities: [{{data.capabilities}}]--OrgName: [{{data.orgname}}]'},
        
        'challenge_auth_reponse_payload2': {'format': '[Chllenge Auth Response Payload]--CertChainHash: [{{data.certchainhash}}]--Salt: [{{data.salt}}]--Context Hash: [{{data.context_hash}}]--Signature: [{{data.signature}}]'},
        
        'challenge_auth_response_payload_certchainhash': {'format': '[Chllenge Auth Response Payload]--CertChainHash: [{{data.raw}}]'},
        
        'challenge_auth_response_payload_salt': {'format': '[Chllenge Auth Response Payload]--Salt: [{{data.raw}}]'},
        
        'challenge_auth_response_payload_contexthash': {'format': '[Chllenge Auth Response Payload]--Context Hash: [{{data.raw}}]'},
        
        'challenge_auth_response_payload_signature': {'format': '[Chllenge Auth Response Payload]--Siganature: [{{data.raw}}]'},
        
        'SDB_0': {'format': '[{{data.data_db_type}}][{{data.raw}}] Offset[0]--Internal Temp: [{{data.internal_temp}}]'},
        
        'SDB_1': {'format': '[{{data.data_db_type}}][{{data.raw}}] Offset[1]--External Power [{{data.external_power_present}}]--AC/DC [{{data.external_power_acdc}}]--Internal Power from Battery  [{{data.internal_power_from_battery}}]--Internal Power from non-Battery power source [{{data.internal_power_from_non_battery}}]'},
        
        'SDB_2': {'format': '[{{data.data_db_type}}][{{data.raw}}] Offset[2]--Hot Swappable Battery [{{data.hot_swappable_battery}}]--Fixed Battery [{{data.fixed_battery}}]'},
        
        'SDB_3': {'format': '[{{data.data_db_type}}][{{data.raw}}] Offset[3]--OCP [{{data.ocp}}]--OTP [{{data.otp}}]--OVP [{{data.ovp}}]--CF mode [{{data.cf_mode}}]'},
        
        'SDB_4': {'format': '[{{data.data_db_type}}][{{data.raw}}] Offset[4]--Temperature Status [{{data.temperture_status}}]'},
        
        'SDB_5': {'format': '[{{data.data_db_type}}][{{data.raw}}] Offset[5]--Power Status [{{data.power_status}}]'},
        
        'SDB_6': {'format': '[{{data.data_db_type}}][{{data.raw}}] Offset[6]--New Power State [{{data.new_power_status}}]--New power state indicator [{{data.new_power_state_indicator}}]'},
        
        'GBCDB': {'format': '[{{data.data_db_type}}][{{data.raw}}]--Battery Cap Ref: [{{data.batt_cap_ref}}]'},
        
        'GBSDB': {'format': '[{{data.data_db_type}}][{{data.raw}}]--Battery Cap Ref: [{{data.batt_cap_ref}}]'},
        
        'BCDB': {'format': '[{{data.data_db_type}}][{{data.raw}}]--VID: [{{data.vid}}]--PID: [{{data.pid}}]--Battery Design Capacity: [{{data.battery_design_capacity}}]--Battery Last Full Charge Capacity: [{{data.battery_last_full_charge_capacity}}]--Battery Type: [{{data.battery_type}}]'},
        
        'GMIDB': {'format': '[{{data.data_db_type}}][{{data.raw}}]--Manufacturer Info Target: [{{data.manufacturer_info_target}}]--Manufacturer Info Ref: [{{data.manufacturer_info_ref}}]'},
        
        'MIDB': {'format': '[{{data.data_db_type}}][{{data.raw}}]--VID: [{{data.vid}}]--PID: [{{data.pid}}]--Manufacturer String: [{{data.manufacturer_string}}]'},
        
        'ppssdb': {'format': '[{{data.data_db_type}}][{{data.raw}}]--Output Voltage: [{{data.output_voltage}}]--Output Current: [{{data.output_current}}]--Real Time Flags: PTF [{{data.ptf}}], OMF [{{data.omf}}]'},
        
        'ccdb': {'format': '[{{data.data_db_type}}][{{data.raw}}]--Length: [{{data.length}}]--Country Code: [{{data.country_code}}]'},
        
        'cidb': {'format': '[{{data.data_db_type}}][{{data.raw}}]--Country code: [{{data.country_code}}]--Country Specific Data: [{{data.country_specific_data}}]'},
        
    }

    def __init__(self):
        self.engine = None
        self.leftover_bits = []
        self.leftover_time=[]
        self.leftover_time_end=[]
        self.epr_source_capabilities_pdo_types = {}
        self.source_capabilities_pdo_types = {}

    def decode(self, frame: AnalyzerFrame):
        '''
        Process a frame from the input analyzer, and optionally return a single `AnalyzerFrame` or a list of `AnalyzerFrame`s.

        The type and data values in `frame` will depend on the input analyzer.
        '''
        if self.engine is None:
            self.engine = self.state_machine()
            self.engine.send(None)

        try:
            output_frame = self.engine.send(frame)
            if output_frame is not None:
                return output_frame
        except StopIteration:
            self.engine = None

    def state_machine(self):
        next = None
        self.leftover_bits.clear()
        self.leftover_time.clear()
        self.leftover_time_end.clear()
        while True:
            while len(self.leftover_bits) < 64:
                yield from self.get_bits(64)
                if len(self.leftover_bits) >= 64:   
                    z=63
                    x=0
                    while x < z:
                        if float(self.leftover_time[x + 1]-self.leftover_time[x]) >= 4.7e-06:
                            del self.leftover_bits[:x+1]
                            del self.leftover_time[:x+1]
                            del self.leftover_time_end[:x+1]
                            x=0
                            z=len(self.leftover_bits)-1
                        else:
                            x=x+1  
            #
            preamble_cmd = self.decode_preamble(self.leftover_bits)
            if preamble_cmd['preamble'] == 'Preamble missing first of UI':
                print(preamble_cmd['preamble'])
                next = yield AnalyzerFrame('preamble', self.leftover_time[0], self.leftover_time_end[62], preamble_cmd)
                self.leftover_bits = self.leftover_bits[63:]
                self.leftover_time = self.leftover_time[63:]
                self.leftover_time_end = self.leftover_time_end[63:]
                self.leftover_bits.append(next.data['data'])
                self.leftover_time.append(next.start_time)
                self.leftover_time_end.append(next.end_time)    
            elif preamble_cmd['preamble'] == 'Preamble':
                print(preamble_cmd['preamble'])
                next = yield AnalyzerFrame('preamble', self.leftover_time[0], self.leftover_time_end[63], preamble_cmd)
                self.leftover_bits = self.leftover_bits[64:]
                self.leftover_time = self.leftover_time[64:]
                self.leftover_time_end = self.leftover_time_end[64:]
                self.leftover_bits.append(next.data['data'])
                self.leftover_time.append(next.start_time)
                self.leftover_time_end.append(next.end_time)
            else:
                print(preamble_cmd['preamble'])
                import sys
                sys.exit()
            #
            yield from self.get_bits(20)
            address_cmd = self.decode_address(self.leftover_bits)
            print(address_cmd['address'])
            #if address_cmd['address'] == 'Missing the SOP' :
            #   import sys
            #   sys.exit()
            next = yield AnalyzerFrame('address', self.leftover_time[0], self.leftover_time_end[19], address_cmd)
            self.leftover_bits = self.leftover_bits[20:]
            self.leftover_time = self.leftover_time[20:]
            self.leftover_time_end = self.leftover_time_end[20:]
            self.leftover_bits.append(next.data['data'])
            self.leftover_time.append(next.start_time)
            self.leftover_time_end.append(next.end_time)
            if address_cmd['address'] == 'Hard Reset' :
               continue
            if address_cmd['address'] == 'Cable Reset' :
               continue
            #
            yield from self.get_bits(20)
            header_decoded = self.bits_to_bytes(self.leftover_bits, 2)
            header_int = int.from_bytes(header_decoded, "little")
            object_count = (header_int >> 12) & 0x07
            header_data = self.decode_header(header_int, address_cmd)
            header_data['raw'] = hex(header_int)
            print('Message Header',':',header_data)
            next = yield AnalyzerFrame('header', self.leftover_time[0], self.leftover_time_end[19], header_data)
            self.leftover_bits = self.leftover_bits[20:]
            self.leftover_time = self.leftover_time[20:]
            self.leftover_time_end = self.leftover_time_end[20:]
            self.leftover_bits.append(next.data['data'])
            self.leftover_time.append(next.start_time)
            self.leftover_time_end.append(next.end_time)
            if header_data['Extended'] == 1: #Extended message
                yield from self.get_bits(20)
                ext_header_decoded = self.bits_to_bytes(self.leftover_bits, 2)
                ext_header_int = int.from_bytes(ext_header_decoded, "little")
                ext_header_data = self.decode_ext_header(ext_header_int)
                ext_header_data['raw'] = hex(ext_header_int)
                chunked = ext_header_data['chunked']
                chunkednum = ext_header_data['chunked_number']
                reqchunk = ext_header_data['request_chunk']
                datasize = ext_header_data['data_size']
                print('Extended Message Header',':',ext_header_data)
                next = yield AnalyzerFrame('ext_header', self.leftover_time[0], self.leftover_time_end[19], ext_header_data)
                self.leftover_bits = self.leftover_bits[20:]
                self.leftover_time = self.leftover_time[20:]
                self.leftover_time_end = self.leftover_time_end[20:]
                self.leftover_bits.append(next.data['data'])
                self.leftover_time.append(next.start_time)
                self.leftover_time_end.append(next.end_time)
                data_db_data = {}
                if chunked == 0: 
                    getbytes_num = datasize
                    getbits_num = getbytes_num * 10

                if chunked == 1: 
                    if chunkednum >= 0 and reqchunk == 0:
                        if datasize <= 26:
                            getbytes_num = ((object_count*4)- 2)

                        else:
                            if ((chunkednum + 1)*26) < datasize:
                                getbytes_num = 26
                            if ((chunkednum + 1)*26) >= datasize:
                                getbytes_num = ((object_count*4)- 2)   
                    if chunkednum >= 1 and reqchunk == 1:
                        getbytes_num = ((object_count * 4) - 2)
                        getbits_num = getbytes_num * 10
                        yield from self.get_bits(getbits_num)
                        db_decoded = self.bits_to_bytes(self.leftover_bits, getbytes_num)
                        db_int = int.from_bytes(db_decoded, "little")
                        data_db_type = 'epr_mode_chunk_request'
                        data_db_data['raw'] = hex(db_int)
                        print(header_data['command_code'],':',data_db_data)
                        self.leftover_bits = self.leftover_bits[getbits_num:]
                        next = yield AnalyzerFrame(data_db_type, self.leftover_time[0], self.leftover_time_end[getbits_num - 1], data_db_data)
                        self.leftover_time = self.leftover_time[getbits_num:]
                        self.leftover_time_end = self.leftover_time_end[getbits_num:]
                        self.leftover_bits.append(next.data['data'])
                        self.leftover_time.append(next.start_time)
                        self.leftover_time_end.append(next.end_time)

                if header_data['command_code'] == 'EPR_Source_Capabilities':
                    if reqchunk == 0:                      
                        effect_object_count = getbytes_num//4
                        if chunkednum >= 1 and leftbits_num != []:
                            yield from self.get_bits(20)
                            leftbits_num.extend(self.leftover_bits)
                            epr_source_pdo_bits = leftbits_num[:40]
                            object_decoded = self.bits_to_bytes(epr_source_pdo_bits, 4)
                            object_int = int.from_bytes(object_decoded, "little")
                            frame_type, data_db_data = decode_source_power_data_object(
                                object_int, 7)
                            data_db_type = frame_type
                            data_db_data['raw'] = hex(object_int)
                            self.epr_source_capabilities_pdo_types[7] = data_db_data['pdo_type'] 
                            print(f'EPR_Source_Capabilities: {data_db_data}')
                            self.leftover_bits = self.leftover_bits[20:]
                            next = yield AnalyzerFrame(data_db_type, self.leftover_time[0], self.leftover_time_end[19], data_db_data)
                            self.leftover_time = self.leftover_time[20:]
                            self.leftover_time_end = self.leftover_time_end[20:]
                            self.leftover_bits.append(next.data['data'])
                            self.leftover_time.append(next.start_time)
                            self.leftover_time_end.append(next.end_time)
                            data_db_type = []
                            leftbits_num = []  
                        for object_index in range(1, effect_object_count + 1):
                            yield from self.get_bits(40)
                            epr_source_pdo_bits = self.leftover_bits[:40]
                            epr_object_decoded = self.bits_to_bytes(epr_source_pdo_bits, 4)
                            epr_object_int = int.from_bytes(epr_object_decoded, "little")
                            frame_type, data_object_data = decode_source_power_data_object(epr_object_int, (chunkednum*7 + object_index))
                            data_object_type = frame_type
                            data_object_data['index'] = object_index + (chunkednum*7)
                            data_object_data['raw'] = hex(epr_object_int)
                            self.epr_source_capabilities_pdo_types[object_index + (chunkednum*7)] = data_object_data['pdo_type'] 
                            print(f'EPR_Source_Capabilities: {data_object_data}')
                            self.leftover_bits = self.leftover_bits[40:]
                            next = yield AnalyzerFrame(data_object_type, self.leftover_time[0], self.leftover_time_end[39], data_object_data)
                            self.leftover_time = self.leftover_time[40:]
                            self.leftover_time_end = self.leftover_time_end[40:]
                            self.leftover_bits.append(next.data['data'])
                            self.leftover_time.append(next.start_time)
                            self.leftover_time_end.append(next.end_time)            
                        if  (getbytes_num % 4) != 0 and getbytes_num == 26 and chunked == 1:
                            leftbytes = getbytes_num % 4
                            yield from self.get_bits(leftbytes*10)
                            leftbits_num = self.leftover_bits[:(10*(leftbytes))]
                            leftbits_decoded = self.bits_to_bytes(leftbits_num, leftbytes)
                            leftbits_int = int.from_bytes(leftbits_decoded, "little")
                            data_db_data = {'raw': hex(leftbits_int)}
                            next = yield AnalyzerFrame('epr_chunked_leftbytes', self.leftover_time[0], self.leftover_time_end[(10*(leftbytes))-1], data_db_data)
                            self.leftover_bits = self.leftover_bits[(10*(leftbytes)):]
                            self.leftover_time = self.leftover_time[(10*(leftbytes)):]
                            self.leftover_time_end = self.leftover_time_end[(10*(leftbytes)):]
                            self.leftover_bits.append(next.data['data'])
                            self.leftover_time.append(next.start_time)
                            self.leftover_time_end.append(next.end_time)
                elif header_data['command_code'] == 'EPR_Sink_Capabilities':
                    if reqchunk == 0:                      
                        effect_object_count = getbytes_num//4
                        if chunkednum >= 1 and leftbits_num != []:
                            yield from self.get_bits(20)
                            leftbits_num.extend(self.leftover_bits)
                            epr_source_pdo_bits = leftbits_num[:40]
                            object_decoded = self.bits_to_bytes(epr_source_pdo_bits, 4)
                            object_int = int.from_bytes(object_decoded, "little")
                            frame_type, data_db_data = decode_sink_power_data_object(object_int, 7)
                            data_db_type = frame_type
                            data_db_data['raw'] = hex(object_int)
                            self.epr_source_capabilities_pdo_types[7] = data_db_data['pdo_type'] 
                            print(f'EPR_Sink_Capabilities: {data_db_data}')
                            self.leftover_bits = self.leftover_bits[20:]
                            next = yield AnalyzerFrame(data_db_type, self.leftover_time[0], self.leftover_time_end[19], data_db_data)
                            self.leftover_time = self.leftover_time[20:]
                            self.leftover_time_end = self.leftover_time_end[20:]
                            self.leftover_bits.append(next.data['data'])
                            self.leftover_time.append(next.start_time)
                            self.leftover_time_end.append(next.end_time)
                            data_db_type = []
                            leftbits_num = []  
                        for object_index in range(1, effect_object_count + 1):
                            yield from self.get_bits(40)
                            epr_source_pdo_bits = self.leftover_bits[:40]
                            epr_object_decoded = self.bits_to_bytes(epr_source_pdo_bits, 4)
                            epr_object_int = int.from_bytes(epr_object_decoded, "little")
                            frame_type, data_object_data = decode_sink_power_data_object(epr_object_int, (chunkednum*7 + object_index))
                            data_object_type = frame_type
                            data_object_data['index'] = object_index + (chunkednum*7)
                            data_object_data['raw'] = hex(epr_object_int)
                            self.epr_source_capabilities_pdo_types[object_index + (chunkednum*7)] = data_object_data['pdo_type'] 
                            print(f'EPR_Sink_Capabilities: {data_object_data}')
                            self.leftover_bits = self.leftover_bits[40:]
                            next = yield AnalyzerFrame(data_object_type, self.leftover_time[0], self.leftover_time_end[39], data_object_data)
                            self.leftover_time = self.leftover_time[40:]
                            self.leftover_time_end = self.leftover_time_end[40:]
                            self.leftover_bits.append(next.data['data'])
                            self.leftover_time.append(next.start_time)
                            self.leftover_time_end.append(next.end_time)            
                        if  (getbytes_num % 4) != 0 and getbytes_num == 26 and chunked == 1:
                            leftbytes = getbytes_num % 4
                            yield from self.get_bits(leftbytes*10)
                            leftbits_num = self.leftover_bits[:(10*(leftbytes))]
                            leftbits_decoded = self.bits_to_bytes(leftbits_num, leftbytes)
                            leftbits_int = int.from_bytes(leftbits_decoded, "little")
                            data_db_data = {'raw': hex(leftbits_int)}
                            next = yield AnalyzerFrame('epr_chunked_leftbytes', self.leftover_time[0], self.leftover_time_end[(10*(leftbytes))-1], data_db_data)
                            self.leftover_bits = self.leftover_bits[(10*(leftbytes)):]
                            self.leftover_time = self.leftover_time[(10*(leftbytes)):]
                            self.leftover_time_end = self.leftover_time_end[(10*(leftbytes)):]
                            self.leftover_bits.append(next.data['data'])
                            self.leftover_time.append(next.start_time)
                            self.leftover_time_end.append(next.end_time)
                elif header_data['command_code'] == 'Status':
                    for db_index in range(getbytes_num):
                        yield from self.get_bits(10)
                        db_bits = self.leftover_bits[:10]
                        db_decoded = self.bits_to_bytes(db_bits, 1)
                        db_int = int.from_bytes(db_decoded, "little")
                        frame_type, data_db_data = decode_status(db_int, db_index)
                        data_db_type = frame_type
                        data_db_data['raw'] = hex(db_int)
                        print(f'Status: Offset[{db_index}] {data_db_data}')
                        self.leftover_bits = self.leftover_bits[10:]
                        next = yield AnalyzerFrame(data_db_type, self.leftover_time[0], self.leftover_time_end[9], data_db_data)
                        self.leftover_time = self.leftover_time[10:]
                        self.leftover_time_end = self.leftover_time_end[10:]
                        self.leftover_bits.append(next.data['data'])
                        self.leftover_time.append(next.start_time)
                        self.leftover_time_end.append(next.end_time) 
                elif header_data['command_code'] == 'Get_Battery_Cap': 
                    yield from self.get_bits(getbits_num)
                    db_bits = self.leftover_bits[:getbits_num]
                    db_decoded = self.bits_to_bytes(db_bits, getbytes_num)
                    db_int = int.from_bytes(db_decoded, "little")
                    frame_type, data_db_data = decode_battery_cap(db_int)
                    data_db_type = frame_type
                    data_db_data['raw'] = hex(db_int)
                    print(f'Get_Battery_Cap: {data_db_data}')
                    self.leftover_bits = self.leftover_bits[getbits_num:]
                    next = yield AnalyzerFrame(data_db_type, self.leftover_time[0], self.leftover_time_end[getbits_num - 1], data_db_data)
                    self.leftover_time = self.leftover_time[getbits_num:]
                    self.leftover_time_end = self.leftover_time_end[getbits_num:]
                    self.leftover_bits.append(next.data['data'])
                    self.leftover_time.append(next.start_time)
                    self.leftover_time_end.append(next.end_time)
                elif header_data['command_code'] == 'Get_Battery_Status': 
                    yield from self.get_bits(getbits_num)
                    db_bits = self.leftover_bits[:getbits_num]
                    db_decoded = self.bits_to_bytes(db_bits, getbytes_num)
                    db_int = int.from_bytes(db_decoded, "little")
                    frame_type, data_db_data = decode_battery_status(db_int)
                    data_db_type = frame_type
                    data_db_data['raw'] = hex(db_int)
                    print(f'Get_Battery_Status: {data_db_data}')
                    self.leftover_bits = self.leftover_bits[getbits_num:]
                    next = yield AnalyzerFrame(data_db_type, self.leftover_time[0], self.leftover_time_end[getbits_num - 1], data_db_data)
                    self.leftover_time = self.leftover_time[getbits_num:]
                    self.leftover_time_end = self.leftover_time_end[getbits_num:]
                    self.leftover_bits.append(next.data['data'])
                    self.leftover_time.append(next.start_time)
                    self.leftover_time_end.append(next.end_time)
                elif header_data['command_code'] == 'Battery_Capabilities': 
                    yield from self.get_bits(getbits_num)
                    db_bits = self.leftover_bits[:getbits_num]
                    db_decoded = self.bits_to_bytes(db_bits, getbytes_num)
                    db_int = int.from_bytes(db_decoded, "little")
                    frame_type, data_db_data = decode_battery_capabilities(db_int)
                    data_db_type = frame_type
                    data_db_data['raw'] = hex(db_int)
                    print(f'Battery_Capabilities: {data_db_data}')
                    self.leftover_bits = self.leftover_bits[getbits_num:]
                    next = yield AnalyzerFrame(data_db_type, self.leftover_time[0], self.leftover_time_end[getbits_num - 1], data_db_data)
                    self.leftover_time = self.leftover_time[getbits_num:]
                    self.leftover_time_end = self.leftover_time_end[getbits_num:]
                    self.leftover_bits.append(next.data['data'])
                    self.leftover_time.append(next.start_time)
                    self.leftover_time_end.append(next.end_time) 
                elif header_data['command_code'] == 'Get_Manufacturer_Info': 
                    yield from self.get_bits(getbits_num)
                    db_bits = self.leftover_bits[:getbits_num]
                    db_decoded = self.bits_to_bytes(db_bits, getbytes_num)
                    db_int = int.from_bytes(db_decoded, "little")
                    frame_type, data_db_data = decode_get_manufacturer_info(db_int)
                    data_db_type = frame_type
                    data_db_data['raw'] = hex(db_int)
                    print(f'Get_Manufacturer_Info: {data_db_data}')
                    self.leftover_bits = self.leftover_bits[getbits_num:]
                    next = yield AnalyzerFrame(data_db_type, self.leftover_time[0], self.leftover_time_end[getbits_num - 1], data_db_data)
                    self.leftover_time = self.leftover_time[getbits_num:]
                    self.leftover_time_end = self.leftover_time_end[getbits_num:]
                    self.leftover_bits.append(next.data['data'])
                    self.leftover_time.append(next.start_time)
                    self.leftover_time_end.append(next.end_time) 
                elif header_data['command_code'] == 'Manufacturer_Info':
                    yield from self.get_bits(getbits_num)
                    db_bits = self.leftover_bits[:getbits_num]
                    db_decoded = self.bits_to_bytes(db_bits, getbytes_num)
                    db_int = int.from_bytes(db_decoded, "little")
                    frame_type, data_db_data = decode_manufacturer_info(db_int, getbytes_num)
                    data_db_type = frame_type
                    data_db_data['raw'] = hex(db_int)
                    print(f'Get_Manufacturer_Info: {data_db_data}')
                    self.leftover_bits = self.leftover_bits[getbits_num:]
                    next = yield AnalyzerFrame(data_db_type, self.leftover_time[0], self.leftover_time_end[getbits_num - 1], data_db_data)
                    self.leftover_time = self.leftover_time[getbits_num:]
                    self.leftover_time_end = self.leftover_time_end[getbits_num:]
                    self.leftover_bits.append(next.data['data'])
                    self.leftover_time.append(next.start_time)
                    self.leftover_time_end.append(next.end_time)           
                elif header_data['command_code'] == 'Extended_Control':
                    yield from self.get_bits(getbits_num)
                    db_bits = self.leftover_bits[:getbits_num]
                    db_decoded = self.bits_to_bytes(db_bits, getbytes_num)
                    db_int = int.from_bytes(db_decoded, "little")
                    frame_type, data_db_data = decode_extended_control_msg(db_int)
                    data_db_type = frame_type
                    data_db_data['raw'] = hex(db_int)
                    print(f'Extended_Control: {data_db_data}')
                    self.leftover_bits = self.leftover_bits[getbits_num:]
                    next = yield AnalyzerFrame(data_db_type, self.leftover_time[0], self.leftover_time_end[getbits_num - 1], data_db_data)
                    self.leftover_time = self.leftover_time[getbits_num:]
                    self.leftover_time_end = self.leftover_time_end[getbits_num:]
                    self.leftover_bits.append(next.data['data'])
                    self.leftover_time.append(next.start_time)
                    self.leftover_time_end.append(next.end_time)
                elif header_data['command_code'] == 'Source_Capabilities_Extended':
                    yield from self.get_bits(getbits_num)
                    db_bits = self.leftover_bits[:getbits_num]
                    db_decoded = self.bits_to_bytes(db_bits, getbytes_num)
                    db_int = int.from_bytes(db_decoded, "little")
                    frame_type, data_db_data = decode_extended_source_capabilities(db_int)
                    data_db_type = frame_type
                    data_db_data['raw'] = hex(db_int)
                    print(header_data['command_code'],':',data_db_data)
                    self.leftover_bits = self.leftover_bits[getbits_num:]
                    next = yield AnalyzerFrame(data_db_type, self.leftover_time[0], self.leftover_time_end[getbits_num - 1], data_db_data)
                    self.leftover_time = self.leftover_time[getbits_num:]
                    self.leftover_time_end = self.leftover_time_end[getbits_num:]
                    self.leftover_bits.append(next.data['data'])
                    self.leftover_time.append(next.start_time)
                    self.leftover_time_end.append(next.end_time)
                elif header_data['command_code'] == 'Sink_Capabilities_Extended':
                    yield from self.get_bits(getbits_num)
                    db_bits = self.leftover_bits[:getbits_num]
                    db_decoded = self.bits_to_bytes(db_bits, getbytes_num)
                    db_int = int.from_bytes(db_decoded, "little")
                    frame_type, data_db_data = decode_extended_sink_capabilities(db_int)
                    data_db_type = frame_type
                    data_db_data['raw'] = hex(db_int)
                    print(header_data['command_code'],':',data_db_data)
                    self.leftover_bits = self.leftover_bits[getbits_num:]
                    next = yield AnalyzerFrame(data_db_type, self.leftover_time[0], self.leftover_time_end[getbits_num - 1], data_db_data)
                    self.leftover_time = self.leftover_time[getbits_num:]
                    self.leftover_time_end = self.leftover_time_end[getbits_num:]
                    self.leftover_bits.append(next.data['data'])
                    self.leftover_time.append(next.start_time)
                    self.leftover_time_end.append(next.end_time)
                elif header_data['command_code'] == 'Firmware_Update_Request':
                    if reqchunk == 0 and chunkednum == 0:                      
                        yield from self.get_bits(20)
                        db_bits = self.leftover_bits[:20]
                        db_decoded = self.bits_to_bytes(db_bits, 2)
                        db_int = int.from_bytes(db_decoded, "little")
                        frame_type, data_db_data = decode_firmware_update_msg_header(db_int)
                        data_db_type = frame_type
                        data_db_data['raw'] = hex(db_int)
                        print(header_data['command_code'],':',data_db_data)
                        self.leftover_bits = self.leftover_bits[20:]
                        next = yield AnalyzerFrame(data_db_type, self.leftover_time[0], self.leftover_time_end[19], data_db_data)
                        self.leftover_time = self.leftover_time[20:]
                        self.leftover_time_end = self.leftover_time_end[20:]
                        self.leftover_bits.append(next.data['data'])
                        self.leftover_time.append(next.start_time)
                        self.leftover_time_end.append(next.end_time)
                        if data_db_data['message_type'] == 'GET_FW_ID':
                            print('GET_FW_ID: No Payload')
                        if data_db_data['message_type'] == 'PDFU_INITIATE':
                            db_array = []
                            x=1
                            for db_index in range(2, getbytes_num, 2):
                                yield from self.get_bits(20)
                                db_bits = self.leftover_bits[:20]
                                db_decoded = self.bits_to_bytes(db_bits, 2)
                                db_int = int.from_bytes(db_decoded, "little")
                                data_db_type = 'pdfu_initiate_request'
                                data_db_data['offset'] = db_index
                                data_db_data['fw_version'] = x
                                data_db_data['raw'] = db_int
                                db_array.append(db_int)
                                self.leftover_bits = self.leftover_bits[10:]
                                next = yield AnalyzerFrame(data_db_type, self.leftover_time[0], self.leftover_time_end[9], data_db_data)
                                self.leftover_time = self.leftover_time[10:]
                                self.leftover_time_end = self.leftover_time_end[10:]
                                self.leftover_bits.append(next.data['data'])
                                self.leftover_time.append(next.start_time)
                                self.leftover_time_end.append(next.end_time)
                                x=x+1
                            print(f'PDFU_INITIATE Payload:--FW Ver1: [{db_array[0]}]--FW Ver2: [{db_array[1]}]----FW Ver3: [{db_array[2]}]--FW Ver4: [{db_array[3]}]')
                        if data_db_data['message_type'] == 'PDFU_DATA':
                            db_array = []
                            yield from self.get_bits(20)
                            db_bits = self.leftover_bits[:20]
                            db_decoded = self.bits_to_bytes(db_bits, 2)
                            db_int = int.from_bytes(db_decoded, "little")
                            data_db_type = 'pdfu_datablock_index'
                            data_db_data['offset'] = str('2')
                            data_db_data['datablock_index'] = db_int
                            data_db_index = db_int
                            self.leftover_bits = self.leftover_bits[20:]
                            next = yield AnalyzerFrame(data_db_type, self.leftover_time[0], self.leftover_time_end[19], data_db_data)
                            self.leftover_time = self.leftover_time[20:]
                            self.leftover_time_end = self.leftover_time_end[20:]
                            self.leftover_bits.append(next.data['data'])
                            self.leftover_time.append(next.start_time)
                            self.leftover_time_end.append(next.end_time)
                            for db_index in range(4, getbytes_num):
                                yield from self.get_bits(10)
                                db_bits = self.leftover_bits[:10]
                                db_decoded = self.bits_to_bytes(db_bits, 1)
                                db_int = int.from_bytes(db_decoded, "little")
                                data_db_type = 'pdfu_datablock'
                                data_db_data['offset'] = db_index
                                data_db_data['datablock'] = hex(db_int)
                                db_array.append(hex(db_int))
                                self.leftover_bits = self.leftover_bits[10:]
                                next = yield AnalyzerFrame(data_db_type, self.leftover_time[0], self.leftover_time_end[9], data_db_data)
                                self.leftover_time = self.leftover_time[10:]
                                self.leftover_time_end = self.leftover_time_end[10:]
                                self.leftover_bits.append(next.data['data'])
                                self.leftover_time.append(next.start_time)
                                self.leftover_time_end.append(next.end_time)
                            print(f'PDFU_DATA Payload:--DataBlock Index: [{data_db_index}], Datablock: [{db_array}]')
                            message_type = 'PDFU_DATA'
                        if data_db_data['message_type'] == 'PDFU_DATA_NR':
                            db_array = []
                            yield from self.get_bits(20)
                            db_bits = self.leftover_bits[:20]
                            db_decoded = self.bits_to_bytes(db_bits, 2)
                            db_int = int.from_bytes(db_decoded, "little")
                            data_db_type = 'pdfu_datablock_index'
                            data_db_data['offset'] = str('2')
                            data_db_data['datablock_index'] = db_int
                            data_db_index = db_int
                            self.leftover_bits = self.leftover_bits[20:]
                            next = yield AnalyzerFrame(data_db_type, self.leftover_time[0], self.leftover_time_end[19], data_db_data)
                            self.leftover_time = self.leftover_time[20:]
                            self.leftover_time_end = self.leftover_time_end[20:]
                            self.leftover_bits.append(next.data['data'])
                            self.leftover_time.append(next.start_time)
                            self.leftover_time_end.append(next.end_time)
                            for db_index in range(4, getbytes_num):
                                yield from self.get_bits(10)
                                db_bits = self.leftover_bits[:10]
                                db_decoded = self.bits_to_bytes(db_bits, 1)
                                db_int = int.from_bytes(db_decoded, "little")
                                data_db_type = 'pdfu_datablock'
                                data_db_data['offset'] = db_index
                                data_db_data['datablock'] = hex(db_int)
                                db_array.append(hex(db_int))
                                self.leftover_bits = self.leftover_bits[10:]
                                next = yield AnalyzerFrame(data_db_type, self.leftover_time[0], self.leftover_time_end[9], data_db_data)
                                self.leftover_time = self.leftover_time[10:]
                                self.leftover_time_end = self.leftover_time_end[10:]
                                self.leftover_bits.append(next.data['data'])
                                self.leftover_time.append(next.start_time)
                                self.leftover_time_end.append(next.end_time)
                            print(f'PDFU_DATA_NR Payload:--DataBlock Index: [{data_db_index}], Datablock: [{db_array}]')
                            message_type = 'PDFU_DATA_NR'
                        if data_db_data['message_type'] == 'PDFU_VALIDATE':
                            print('PDFU_VALIDATE: No Payload')
                        if data_db_data['message_type'] == 'PDFU_ABORT':
                            print('PDFU_ABORT: No Payload')    
                        if data_db_data['message_type'] == 'PDFU_DATA_PAUSE':
                            print('PDFU_DATA_PAUSE: No Payload')    
                        if data_db_data['message_type'] == 'VENDOR_SPECIFIC':
                            db_array = []
                            yield from self.get_bits(20)
                            db_bits = self.leftover_bits[:20]
                            db_decoded = self.bits_to_bytes(db_bits, 2)
                            db_int = int.from_bytes(db_decoded, "little")
                            data_db_type = 'pdfu_vendor_specific_payload1'
                            data_db_data['offset'] = str('2')
                            data_db_data['vid'] = hex(db_int)
                            data_db_vid = hex(db_int)
                            self.leftover_bits = self.leftover_bits[20:]
                            next = yield AnalyzerFrame(data_db_type, self.leftover_time[0], self.leftover_time_end[19], data_db_data)
                            self.leftover_time = self.leftover_time[20:]
                            self.leftover_time_end = self.leftover_time_end[20:]
                            self.leftover_bits.append(next.data['data'])
                            self.leftover_time.append(next.start_time)
                            self.leftover_time_end.append(next.end_time)
                            for db_index in range(4, getbytes_num):
                                yield from self.get_bits(10)
                                db_bits = self.leftover_bits[:10]
                                db_decoded = self.bits_to_bytes(db_bits, 1)
                                db_int = int.from_bytes(db_decoded, "little")
                                data_db_type = 'pdfu_vendor_specific_payload2'
                                data_db_data['offset'] = db_index
                                data_db_data['vendor_defined'] = hex(db_int)
                                db_array.append(hex(db_int))
                                self.leftover_bits = self.leftover_bits[10:]
                                next = yield AnalyzerFrame(data_db_type, self.leftover_time[0], self.leftover_time_end[9], data_db_data)
                                self.leftover_time = self.leftover_time[10:]
                                self.leftover_time_end = self.leftover_time_end[10:]
                                self.leftover_bits.append(next.data['data'])
                                self.leftover_time.append(next.start_time)
                                self.leftover_time_end.append(next.end_time)
                            print(f'VENDOR_SPECIFIC Payload:--VID: [{data_db_vid}], Vendor defined: [{db_array}]')
                            message_type = 'VENDOR_SPECIFIC'
                    if reqchunk == 0 and chunkednum >= 1: 
                        if message_type == 'PDFU_DATA' or message_type == 'PDFU_DATA_NR':
                            for db_index in range(getbytes_num):
                                yield from self.get_bits(10)
                                db_bits = self.leftover_bits[:10]
                                db_decoded = self.bits_to_bytes(db_bits, 1)
                                db_int = int.from_bytes(db_decoded, "little")
                                data_db_type = 'pdfu_datablock'
                                data_db_data['offset'] = (chunkednum*26) + db_index
                                data_db_data['datablock'] = hex(db_int)
                                db_array.append(hex(db_int))
                                self.leftover_bits = self.leftover_bits[10:]
                                next = yield AnalyzerFrame(data_db_type, self.leftover_time[0], self.leftover_time_end[9], data_db_data)
                                self.leftover_time = self.leftover_time[10:]
                                self.leftover_time_end = self.leftover_time_end[10:]
                                self.leftover_bits.append(next.data['data'])
                                self.leftover_time.append(next.start_time)
                                self.leftover_time_end.append(next.end_time) 
                            print(f'Datablock: [{db_array}]')
                        if message_type == 'VENDOR_SPECIFIC': 
                            for db_index in range(getbytes_num):
                                yield from self.get_bits(10)
                                db_bits = self.leftover_bits[:10]
                                db_decoded = self.bits_to_bytes(db_bits, 1)
                                db_int = int.from_bytes(db_decoded, "little")
                                data_db_type = 'pdfu_vendor_specific_payload2'
                                data_db_data['offset'] = (chunkednum*26) + db_index
                                data_db_data['vendor_defined'] = hex(db_int)
                                db_array.append(hex(db_int))
                                self.leftover_bits = self.leftover_bits[10:]
                                next = yield AnalyzerFrame(data_db_type, self.leftover_time[0], self.leftover_time_end[9], data_db_data)
                                self.leftover_time = self.leftover_time[10:]
                                self.leftover_time_end = self.leftover_time_end[10:]
                                self.leftover_bits.append(next.data['data'])
                                self.leftover_time.append(next.start_time)
                                self.leftover_time_end.append(next.end_time) 
                            print(f'Vendor defined: [{db_array}]')
                elif header_data['command_code'] == 'Firmware_Update_Response':
                    if reqchunk == 0 and chunkednum == 0:                      
                        yield from self.get_bits(20)
                        db_bits = self.leftover_bits[:20]
                        db_decoded = self.bits_to_bytes(db_bits, 2)
                        db_int = int.from_bytes(db_decoded, "little")
                        frame_type, data_db_data = decode_firmware_update_msg_header(db_int)
                        data_db_type = frame_type
                        data_db_data['raw'] = hex(db_int)
                        print(header_data['command_code'],':',data_db_data)
                        self.leftover_bits = self.leftover_bits[20:]
                        next = yield AnalyzerFrame(data_db_type, self.leftover_time[0], self.leftover_time_end[19], data_db_data)
                        self.leftover_time = self.leftover_time[20:]
                        self.leftover_time_end = self.leftover_time_end[20:]
                        self.leftover_bits.append(next.data['data'])
                        self.leftover_time.append(next.start_time)
                        self.leftover_time_end.append(next.end_time)
                        getbytes_num = getbytes_num - 2
                        getbits_num = getbits_num - 20
                        if data_db_data['message_type'] == 'GET_FW_ID(Response)':
                            yield from self.get_bits(getbits_num)
                            db_bits = self.leftover_bits[:getbits_num]
                            db_decoded = self.bits_to_bytes(db_bits, getbytes_num)
                            db_int = int.from_bytes(db_decoded, "little")
                            frame_type, data_db_data = decode_getfw_id_response(db_int)
                            data_db_type = frame_type
                            data_db_data['raw'] = hex(db_int)
                            print(data_db_data['message_type'],' Payload: ', data_db_data)
                            self.leftover_bits = self.leftover_bits[getbits_num:]
                            next = yield AnalyzerFrame(data_db_type, self.leftover_time[0], self.leftover_time_end[getbits_num - 1], data_db_data)
                            self.leftover_time = self.leftover_time[getbits_num:]
                            self.leftover_time_end = self.leftover_time_end[getbits_num:]
                            self.leftover_bits.append(next.data['data'])
                            self.leftover_time.append(next.start_time)
                            self.leftover_time_end.append(next.end_time)
                        if data_db_data['message_type'] == 'PDFU_INITIATE(Response)':
                            yield from self.get_bits(getbits_num)
                            db_bits = self.leftover_bits[:getbits_num]
                            db_decoded = self.bits_to_bytes(db_bits, getbytes_num)
                            db_int = int.from_bytes(db_decoded, "little")
                            frame_type, data_db_data = decode_pdfu_initiate_response(db_int)
                            data_db_type = frame_type
                            data_db_data['raw'] = hex(db_int)
                            print(data_db_data['message_type'],' Payload: ', data_db_data)
                            self.leftover_bits = self.leftover_bits[getbits_num:]
                            next = yield AnalyzerFrame(data_db_type, self.leftover_time[0], self.leftover_time_end[getbits_num - 1], data_db_data)
                            self.leftover_time = self.leftover_time[getbits_num:]
                            self.leftover_time_end = self.leftover_time_end[getbits_num:]
                            self.leftover_bits.append(next.data['data'])
                            self.leftover_time.append(next.start_time)
                            self.leftover_time_end.append(next.end_time)
                        if data_db_data['message_type'] == 'PDFU_DATA(Response)':
                            yield from self.get_bits(getbits_num)
                            db_bits = self.leftover_bits[:getbits_num]
                            db_decoded = self.bits_to_bytes(db_bits, getbytes_num)
                            db_int = int.from_bytes(db_decoded, "little")
                            frame_type, data_db_data = decode_pdfu_data_response(db_int)
                            data_db_type = frame_type
                            data_db_data['raw'] = hex(db_int)
                            print(data_db_data['message_type'],' Payload: ',data_db_data)
                            self.leftover_bits = self.leftover_bits[getbits_num:]
                            next = yield AnalyzerFrame(data_db_type, self.leftover_time[0], self.leftover_time_end[getbits_num - 1], data_db_data)
                            self.leftover_time = self.leftover_time[getbits_num:]
                            self.leftover_time_end = self.leftover_time_end[getbits_num:]
                            self.leftover_bits.append(next.data['data'])
                            self.leftover_time.append(next.start_time)
                            self.leftover_time_end.append(next.end_time)
                        if data_db_data['message_type'] == 'PDFU_VALIDATE(Response)':
                            yield from self.get_bits(getbits_num)
                            db_bits = self.leftover_bits[:getbits_num]
                            db_decoded = self.bits_to_bytes(db_bits, getbytes_num)
                            db_int = int.from_bytes(db_decoded, "little")
                            frame_type, data_db_data = decode_pdfu_validate_response(db_int)
                            data_db_type = frame_type
                            data_db_data['raw'] = hex(db_int)
                            print(data_db_data['message_type'],' Payload: ',data_db_data)
                            self.leftover_bits = self.leftover_bits[getbits_num:]
                            next = yield AnalyzerFrame(data_db_type, self.leftover_time[0], self.leftover_time_end[getbits_num - 1], data_db_data)
                            self.leftover_time = self.leftover_time[getbits_num:]
                            self.leftover_time_end = self.leftover_time_end[getbits_num:]
                            self.leftover_bits.append(next.data['data'])
                            self.leftover_time.append(next.start_time)
                            self.leftover_time_end.append(next.end_time)    
                        if data_db_data['message_type'] == 'PDFU_DATA_PAUSE(Response)':
                            yield from self.get_bits(getbits_num)
                            db_bits = self.leftover_bits[:getbits_num]
                            db_decoded = self.bits_to_bytes(db_bits, getbytes_num)
                            db_int = int.from_bytes(db_decoded, "little")
                            frame_type, data_db_data = decode_pdfu_data_pause_response(db_int)
                            data_db_type = frame_type
                            data_db_data['raw'] = hex(db_int)
                            print(data_db_data['message_type'],' Payload: ',data_db_data)
                            self.leftover_bits = self.leftover_bits[getbits_num:]
                            next = yield AnalyzerFrame(data_db_type, self.leftover_time[0], self.leftover_time_end[getbits_num - 1], data_db_data)
                            self.leftover_time = self.leftover_time[getbits_num:]
                            self.leftover_time_end = self.leftover_time_end[getbits_num:]
                            self.leftover_bits.append(next.data['data'])
                            self.leftover_time.append(next.start_time)
                            self.leftover_time_end.append(next.end_time)   
                        if data_db_data['message_type'] == 'VENDOR_SPECIFIC(Response)':
                            db_array = []
                            yield from self.get_bits(30)
                            db_bits = self.leftover_bits[:30]
                            db_decoded = self.bits_to_bytes(db_bits, 3)
                            db_int = int.from_bytes(db_decoded, "little")
                            frame_type, data_db_data = decode_vendor_specific_response(db_int)
                            data_db_type = frame_type
                            data_db_data['raw'] = hex(db_int)
                            vendor_specific_response_status = data_db_data['status']
                            vendor_specific_response_vid = data_db_data['vid']
                            self.leftover_bits = self.leftover_bits[30:]
                            next = yield AnalyzerFrame(data_db_type, self.leftover_time[0], self.leftover_time_end[29], data_db_data)
                            self.leftover_time = self.leftover_time[30:]
                            self.leftover_time_end = self.leftover_time_end[30:]
                            self.leftover_bits.append(next.data['data'])
                            self.leftover_time.append(next.start_time)
                            self.leftover_time_end.append(next.end_time)
                            for db_index in range(5, getbytes_num):
                                yield from self.get_bits(10)
                                db_bits = self.leftover_bits[:10]
                                db_decoded = self.bits_to_bytes(db_bits, 1)
                                db_int = int.from_bytes(db_decoded, "little")
                                data_db_type = 'pdfu_vendor_specific_response_payload2'
                                data_db_data['offset'] = db_index
                                data_db_data['vendor_defined'] = hex(db_int)
                                db_array.append(hex(db_int))
                                self.leftover_bits = self.leftover_bits[10:]
                                next = yield AnalyzerFrame(data_db_type, self.leftover_time[0], self.leftover_time_end[9], data_db_data)
                                self.leftover_time = self.leftover_time[10:]
                                self.leftover_time_end = self.leftover_time_end[10:]
                                self.leftover_bits.append(next.data['data'])
                                self.leftover_time.append(next.start_time)
                                self.leftover_time_end.append(next.end_time)
                            print(f'VENDOR_SPECIFIC(Response) Payload:--Status: [{vendor_specific_response_status}]--VID: [{vendor_specific_response_vid}]--Vendor defined: {db_array}')
                            message_type = 'VENDOR_SPECIFIC(Response)'
                    if reqchunk == 0 and chunkednum >= 1 and message_type == 'VENDOR_SPECIFIC(Response)': 
                        for db_index in range(getbytes_num):
                            yield from self.get_bits(10)
                            db_bits = self.leftover_bits[:10]
                            db_decoded = self.bits_to_bytes(db_bits, 1)
                            db_int = int.from_bytes(db_decoded, "little")
                            data_db_type = 'pdfu_vendor_specific_response_payload2'
                            data_db_data['offset'] = (chunkednum*26) + db_index
                            data_db_data['vendor_defined'] = hex(db_int)
                            db_array.append(hex(db_int))
                            self.leftover_bits = self.leftover_bits[10:]
                            next = yield AnalyzerFrame(data_db_type, self.leftover_time[0], self.leftover_time_end[9], data_db_data)
                            self.leftover_time = self.leftover_time[10:]
                            self.leftover_time_end = self.leftover_time_end[10:]
                            self.leftover_bits.append(next.data['data'])
                            self.leftover_time.append(next.start_time)
                            self.leftover_time_end.append(next.end_time)
                        print(f'Vendor defined: [{db_array}]')
                elif header_data['command_code'] == 'Security_Request':
                    if reqchunk == 0 and chunkednum == 0:
                        yield from self.get_bits(40)
                        db_bits = self.leftover_bits[:40]
                        db_decoded = self.bits_to_bytes(db_bits, 4)
                        db_int = int.from_bytes(db_decoded, "little")
                        frame_type, data_db_data = decode_security_msg_header(db_int)
                        data_db_type = frame_type
                        data_db_data['raw'] = hex(db_int)
                        print(header_data['command_code'],':',data_db_data)
                        self.leftover_bits = self.leftover_bits[40:]
                        next = yield AnalyzerFrame(data_db_type, self.leftover_time[0], self.leftover_time_end[39], data_db_data)
                        self.leftover_time = self.leftover_time[40:]
                        self.leftover_time_end = self.leftover_time_end[40:]
                        self.leftover_bits.append(next.data['data'])
                        self.leftover_time.append(next.start_time)
                        self.leftover_time_end.append(next.end_time)
                        if data_db_data['message_type'] == 'GET_DIGESTS':
                            print('GET_DIGESTS: No Payload')
                        if data_db_data['message_type'] == 'GET_CERTIFICATE':
                            yield from self.get_bits(40)
                            db_bits = self.leftover_bits[:40]
                            db_decoded = self.bits_to_bytes(db_bits, 4)
                            db_int = int.from_bytes(db_decoded, "little")
                            frame_type, data_db_data = decode_get_certificate(db_int)
                            data_db_type = frame_type
                            data_db_data['raw'] = hex(db_int)
                            print('GET_CERTIFICATE Payload:',data_db_data)
                            self.leftover_bits = self.leftover_bits[40:]
                            next = yield AnalyzerFrame(data_db_type, self.leftover_time[0], self.leftover_time_end[39], data_db_data)
                            self.leftover_time = self.leftover_time[40:]
                            self.leftover_time_end = self.leftover_time_end[40:]
                            self.leftover_bits.append(next.data['data'])
                            self.leftover_time.append(next.start_time)
                            self.leftover_time_end.append(next.end_time)
                        if data_db_data['message_type'] == 'CHALLENGE':
                            db_array = []
                            for db_index in range(4, getbytes_num):
                                yield from self.get_bits(10)
                                db_bits = self.leftover_bits[:10]
                                db_decoded = self.bits_to_bytes(db_bits, 1)
                                db_int = int.from_bytes(db_decoded, "little")
                                data_db_type = 'security_nonce'
                                data_db_data['offset'] = db_index
                                data_db_data['nonce'] = hex(db_int)
                                db_array.append(hex(db_int))
                                self.leftover_bits = self.leftover_bits[10:]
                                next = yield AnalyzerFrame(data_db_type, self.leftover_time[0], self.leftover_time_end[9], data_db_data)
                                self.leftover_time = self.leftover_time[10:]
                                self.leftover_time_end = self.leftover_time_end[10:]
                                self.leftover_bits.append(next.data['data'])
                                self.leftover_time.append(next.start_time)
                                self.leftover_time_end.append(next.end_time)
                            print(f'CHALLENGE Payload:--Nonce: [{db_array}]')
                            message_type = 'CHALLENGE'
                    if reqchunk == 0 and chunkednum >= 1 and message_type == 'CHALLENGE': 
                        for db_index in range(getbytes_num):
                            yield from self.get_bits(10)
                            db_bits = self.leftover_bits[:10]
                            db_decoded = self.bits_to_bytes(db_bits, 1)
                            db_int = int.from_bytes(db_decoded, "little")
                            data_db_type = 'security_nonce'
                            data_db_data['offset'] = (chunkednum*26) + db_index
                            data_db_data['nonce'] = hex(db_int)
                            db_array.append(hex(db_int))
                            self.leftover_bits = self.leftover_bits[10:]
                            next = yield AnalyzerFrame(data_db_type, self.leftover_time[0], self.leftover_time_end[9], data_db_data)
                            self.leftover_time = self.leftover_time[10:]
                            self.leftover_time_end = self.leftover_time_end[10:]
                            self.leftover_bits.append(next.data['data'])
                            self.leftover_time.append(next.start_time)
                            self.leftover_time_end.append(next.end_time)
                        print(f'CHALLENGE Payload:--Nonce: [{db_array}]')
                elif header_data['command_code'] == 'Security_Response':
                    #db_array = []
                    if reqchunk == 0 and chunkednum == 0: 
                        #db_array = []
                        yield from self.get_bits(40)
                        db_bits = self.leftover_bits[:40]
                        db_decoded = self.bits_to_bytes(db_bits, 4)
                        db_int = int.from_bytes(db_decoded, "little")
                        frame_type, data_db_data = decode_security_msg_header(db_int)
                        data_db_type = frame_type
                        data_db_data['raw'] = hex(db_int)
                        print(header_data['command_code'],':',data_db_data)
                        self.leftover_bits = self.leftover_bits[40:]
                        next = yield AnalyzerFrame(data_db_type, self.leftover_time[0], self.leftover_time_end[39], data_db_data)
                        self.leftover_time = self.leftover_time[40:]
                        self.leftover_time_end = self.leftover_time_end[40:]
                        self.leftover_bits.append(next.data['data'])
                        self.leftover_time.append(next.start_time)
                        self.leftover_time_end.append(next.end_time)
                        getbytes_num = getbytes_num - 4
                        getbits_num = getbytes_num * 10
                        if data_db_data['message_type'] == 'DIGESTS(Response)':
                            if chunked == 0:
                                digest_num = getbytes_num / 32
                                for digest_index in range(digest_num):
                                    yield from self.get_bits(320)
                                    db_bits = self.leftover_bits[:320]
                                    db_decoded = self.bits_to_bytes(db_bits, 32)
                                    db_int = int.from_bytes(db_decoded, "little")
                                    data_db_type = 'digest_response_playload'
                                    data_db_data['index'] = digest_index
                                    data_db_data['raw'] = hex(db_int)
                                    print(f'DIGESTS(Response) Payload: Digest[{digest_index}] Certificate Chain: [{hex(db_int)}]')
                                    self.leftover_bits = self.leftover_bits[320:]
                                    next = yield AnalyzerFrame(data_object_type, self.leftover_time[0], self.leftover_time_end[319], data_object_data)
                                    self.leftover_time = self.leftover_time[320:]
                                    self.leftover_time_end = self.leftover_time_end[320:]
                                    self.leftover_bits.append(next.data['data'])
                                    self.leftover_time.append(next.start_time)
                                    self.leftover_time_end.append(next.end_time)
                            if chunked == 1:
                                if reqchunk == 0 and chunkednum == 0: 
                                    yield from self.get_bits(getbits_num)
                                    leftbits_num.extend(self.leftover_bits)
                                    x = 0
                                    db_bits = leftbits_num
                                    db_decoded = self.bits_to_bytes(db_bits, getbytes_num)
                                    db_int = int.from_bytes(db_decoded, "little")
                                    data_db_type = 'digest_response_playload'
                                    data_db_data['index'] = x
                                    data_db_data['raw'] = hex(db_int)
                                    print(f'DIGESTS(Response) Payload: Digest[{x}] Certificate Chain: [{hex(db_int)}]')
                                    self.leftover_bits = self.leftover_bits[getbits_num:]
                                    next = yield AnalyzerFrame(data_object_type, self.leftover_time[0], self.leftover_time_end[getbits_num - 1], data_object_data)
                                    self.leftover_time = self.leftover_time[getbits_num:]
                                    self.leftover_time_end = self.leftover_time_end[getbits_num:]
                                    self.leftover_bits.append(next.data['data'])
                                    self.leftover_time.append(next.start_time)
                                    self.leftover_time_end.append(next.end_time)    
                                message_type = 'DIGESTS(Response)'
                        if data_db_data['message_type'] == 'CERTIFICATE(Response)':
                            for db_index in range(4, getbytes_num):
                                yield from self.get_bits(10)
                                db_bits = self.leftover_bits[:10]
                                db_decoded = self.bits_to_bytes(db_bits, 1)
                                db_int = int.from_bytes(db_decoded, "little")
                                data_db_type = 'certificate_response_playload'
                                data_db_data['offset'] = db_index
                                data_db_data['raw'] = hex(db_int)
                                print(f'CERTIFICATE(Response) Payload:--Offset[{db_index}], Datablock: [{hex(db_int)}]')
                                #db_array.append(hex(db_int))
                                self.leftover_bits = self.leftover_bits[10:]
                                next = yield AnalyzerFrame(data_db_type, self.leftover_time[0], self.leftover_time_end[9], data_db_data)
                                self.leftover_time = self.leftover_time[10:]
                                self.leftover_time_end = self.leftover_time_end[10:]
                                self.leftover_bits.append(next.data['data'])
                                self.leftover_time.append(next.start_time)
                                self.leftover_time_end.append(next.end_time)
                            message_type = 'CERTIFICATE(Response)'
                        if data_db_data['message_type'] == 'CHALLENGE_AUTH(Response)':
                            yield from self.get_bits(40)
                            db_bits = self.leftover_bits[:40]
                            db_decoded = self.bits_to_bytes(db_bits, 4)
                            db_int = int.from_bytes(db_decoded, "little")
                            frame_type, data_db_data = decode_challenge_auth_response_payload1(db_int)
                            data_db_type = frame_type
                            data_db_data['raw'] = hex(security_digest_int)
                            print(data_db_data['message_type'],' :',data_db_data)
                            self.leftover_bits = self.leftover_bits[40:]
                            next = yield AnalyzerFrame(data_object_type, self.leftover_time[0], self.leftover_time_end[39], data_object_data)
                            self.leftover_time = self.leftover_time[40:]
                            self.leftover_time_end = self.leftover_time_end[40:]
                            self.leftover_bits.append(next.data['data'])
                            self.leftover_time.append(next.start_time)
                            self.leftover_time_end.append(next.end_time)  
                            getbytes_num = getbytes_num - 4
                            getbits_num = getbytes_num * 10
                            if chunked == 0:
                                for db_index in range(getbytes_num):
                                    yield from self.get_bits(getbits_num)
                                    db_bits = self.leftover_bits[:getbits_num]
                                    db_decoded = self.bits_to_bytes(db_bits, getbytes_num)
                                    db_int = int.from_bytes(db_decoded, "little")
                                    frame_type, data_db_data = decode_challenge_auth_response_payload2(db_int)
                                    data_db_type = frame_type
                                    data_db_data['raw'] = hex(db_int)
                                    print(data_db_data['message_type'],' :',data_db_data)
                                    self.leftover_bits = self.leftover_bits[getbits_num:]
                                    next = yield AnalyzerFrame(data_object_type, self.leftover_time[0], self.leftover_time_end[getbits_num - 1], data_object_data)
                                    self.leftover_time = self.leftover_time[getbits_num:]
                                    self.leftover_time_end = self.leftover_time_end[getbits_num:]
                                    self.leftover_bits.append(next.data['data'])
                                    self.leftover_time.append(next.start_time)
                                    self.leftover_time_end.append(next.end_time)
                            if chunked == 1:
                                if reqchunk == 0 and chunkednum == 0: 
                                    yield from self.get_bits(getbits_num)
                                    leftbits_num.extend(self.leftover_bits)
                                    db_bits = leftbits_num
                                    db_decoded = self.bits_to_bytes(db_bits, getbytes_num)
                                    db_int = int.from_bytes(db_decoded, "little")
                                    data_db_type = 'challenge_auth_response_payload_certchainhash'
                                    data_db_data['raw'] = hex(db_int)
                                    print(f'Challenge AUTH response Payload: CertChainHash: [{hex(db_int)}]')
                                    self.leftover_bits = self.leftover_bits[getbits_num:]
                                    next = yield AnalyzerFrame(data_object_type, self.leftover_time[0], self.leftover_time_end[getbits_num - 1], data_object_data)
                                    self.leftover_time = self.leftover_time[getbits_num:]
                                    self.leftover_time_end = self.leftover_time_end[getbits_num:]
                                    self.leftover_bits.append(next.data['data'])
                                    self.leftover_time.append(next.start_time)
                                    self.leftover_time_end.append(next.end_time)    
                                message_type = 'CHALLENGE_AUTH(Response)'
                                challenge_auth_index = 0
                    if reqchunk == 0 and chunkednum >= 1 and message_type == 'DIGESTS(Response)':
                        if (320 - len(leftbits_num)) > 260:
                            y = 260
                        else:
                            y = 320 - len(leftbits_num)
                        yield from self.get_bits(getbits_num)
                        leftbits_num.extend(self.leftover_bits[:y])
                        if len(leftbits_num) == 320:
                            leftbits_num_decoded = self.bits_to_bytes(leftbits_num, 32)
                            leftbits_num_int = int.from_bytes(leftbits_num_decoded, "little")
                            db_bits = self.leftover_bits[:y]
                            db_decoded = self.bits_to_bytes(db_bits, (y/10))
                            db_int = int.from_bytes(db_decoded, "little")
                            data_db_type = 'digest_response_playload'
                            data_db_data['index'] = x
                            data_db_data['raw'] = hex(db_int)
                            print(f'DIGESTS(Response) Payload: Digest[{x}] Certificate Chain: [{hex(leftbits_num_int)}]')
                            self.leftover_bits = self.leftover_bits[y:]
                            #leftbits_num = []
                            leftbits_num = self.leftover_bits
                            next = yield AnalyzerFrame(data_db_type, self.leftover_time[0], self.leftover_time_end[y - 1], data_db_data)
                            self.leftover_time = self.leftover_time[y:]
                            self.leftover_time_end = self.leftover_time_end[y:]
                            self.leftover_bits.append(next.data['data'])
                            self.leftover_time.append(next.start_time)
                            self.leftover_time_end.append(next.end_time) 
                            x = x + 1
                        else:
                            leftbits_num_decoded = self.bits_to_bytes(leftbits_num, (len(leftbits_num)/10))
                            leftbits_num_int = int.from_bytes(leftbits_num_decoded, "little")
                            db_bits = self.leftover_bits[:y]
                            db_decoded = self.bits_to_bytes(db_bits, 26)
                            db_int = int.from_bytes(db_decoded, "little")
                            data_db_type = 'digest_response_playload'
                            data_db_data['index'] = x
                            data_db_data['raw'] = hex(db_int)
                            print(f'DIGESTS(Response) Payload: Digest[{x}] Certificate Chain: [{hex(leftbits_num_int)}]')
                            self.leftover_bits = self.leftover_bits[y:]
                            next = yield AnalyzerFrame(data_db_type, self.leftover_time[0], self.leftover_time_end[y - 1], data_db_data)
                            self.leftover_time = self.leftover_time[y:]
                            self.leftover_time_end = self.leftover_time_end[y:]
                            self.leftover_bits.append(next.data['data'])
                            self.leftover_time.append(next.start_time)
                            self.leftover_time_end.append(next.end_time)
                    if reqchunk == 0 and chunkednum >= 1 and message_type == 'CERTIFICATE(Response)':
                        for db_index in range(getbytes_num):
                            yield from self.get_bits(10)
                            db_bits = self.leftover_bits[:10]
                            db_decoded = self.bits_to_bytes(db_bits, 1)
                            db_int = int.from_bytes(db_decoded, "little")
                            data_db_type = 'certificate_response_playload'
                            data_db_data['offset'] = (chunkednum*26) + db_index
                            data_db_data['raw'] = hex(db_int)
                            print(f'CERTIFICATE(Response) Payload:--Offset[{(chunkednum*26) + db_index}], Datablock: [{hex(db_int)}]')
                            #db_array.append(hex(db_int))
                            self.leftover_bits = self.leftover_bits[10:]
                            next = yield AnalyzerFrame(data_db_type, self.leftover_time[0], self.leftover_time_end[9], data_db_data)
                            self.leftover_time = self.leftover_time[10:]
                            self.leftover_time_end = self.leftover_time_end[10:]
                            self.leftover_bits.append(next.data['data'])
                            self.leftover_time.append(next.start_time)
                            self.leftover_time_end.append(next.end_time) 
                    if reqchunk == 0 and chunkednum >= 1 and message_type == 'CHALLENGE_AUTH(Response)':
                        if challenge_auth_index == 0:
                            if (320 - len(leftbits_num)) > 260:
                                y = 260
                            else:
                                y = 320 - len(leftbits_num)
                            yield from self.get_bits(getbits_num)
                            leftbits_num.extend(self.leftover_bits[:y])
                            if len(leftbits_num) == 320:
                                leftbits_num_decoded = self.bits_to_bytes(leftbits_num, 32)
                                leftbits_num_int = int.from_bytes(leftbits_num_decoded, "little")
                                db_bits = self.leftover_bits[:y]
                                db_decoded = self.bits_to_bytes(db_bits, (y/10))
                                db_int = int.from_bytes(db_decoded, "little")
                                data_db_type = 'challenge_auth_response_payload_certchainhash'
                                data_db_data['raw'] = hex(db_int)
                                print(f'Challenge AUTH response Payload: CertChainHash: [{hex(leftbits_num_int)}]')
                                self.leftover_bits = self.leftover_bits[y:]
                                #leftbits_num = []
                                leftbits_num = self.leftover_bits
                                next = yield AnalyzerFrame(data_db_type, self.leftover_time[0], self.leftover_time_end[y - 1], data_db_data)
                                self.leftover_time = self.leftover_time[y:]
                                self.leftover_time_end = self.leftover_time_end[y:]
                                self.leftover_bits.append(next.data['data'])
                                self.leftover_time.append(next.start_time)
                                self.leftover_time_end.append(next.end_time) 
                                challenge_auth_index = challenge_auth_index + 1
                            else:
                                leftbits_num_decoded = self.bits_to_bytes(leftbits_num, (len(leftbits_num)/10))
                                leftbits_num_int = int.from_bytes(leftbits_num_decoded, "little")
                                security_digest_bits = self.leftover_bits[:y]
                                security_digest_decoded = self.bits_to_bytes(security_digest_bits, 26)
                                security_digest_int = int.from_bytes(security_digest_decoded, "little")
                                data_db_type = 'challenge_auth_response_payload_certchainhash'
                                data_db_data['raw'] = hex(security_digest_int)
                                print(f'Challenge AUTH response Payload: Certificate Chain: [{hex(leftbits_num_int)}]')
                                self.leftover_bits = self.leftover_bits[y:]
                                next = yield AnalyzerFrame(data_db_type, self.leftover_time[0], self.leftover_time_end[y - 1], data_db_data)
                                self.leftover_time = self.leftover_time[y:]
                                self.leftover_time_end = self.leftover_time_end[y:]
                                self.leftover_bits.append(next.data['data'])
                                self.leftover_time.append(next.start_time)
                                self.leftover_time_end.append(next.end_time)
                        if challenge_auth_index == 1:
                            if (320 - len(leftbits_num)) > 260:
                                y = 260
                            else:
                                y = 320 - len(leftbits_num)
                            yield from self.get_bits(getbits_num)
                            leftbits_num.extend(self.leftover_bits[:y])
                            if len(leftbits_num) == 320:
                                leftbits_num_decoded = self.bits_to_bytes(leftbits_num, 32)
                                leftbits_num_int = int.from_bytes(leftbits_num_decoded, "little")
                                db_bits = self.leftover_bits[:y]
                                db_decoded = self.bits_to_bytes(db_bits, (y/10))
                                db_int = int.from_bytes(db_decoded, "little")
                                data_db_type = 'challenge_auth_response_payload_salt'
                                data_db_data['raw'] = hex(db_int)
                                print(f'Challenge AUTH response Payload: Salt: [{hex(leftbits_num_int)}]')
                                self.leftover_bits = self.leftover_bits[y:]
                                #leftbits_num = []
                                leftbits_num = self.leftover_bits
                                next = yield AnalyzerFrame(data_db_type, self.leftover_time[0], self.leftover_time_end[y - 1], data_db_data)
                                self.leftover_time = self.leftover_time[y:]
                                self.leftover_time_end = self.leftover_time_end[y:]
                                self.leftover_bits.append(next.data['data'])
                                self.leftover_time.append(next.start_time)
                                self.leftover_time_end.append(next.end_time) 
                                challenge_auth_index = challenge_auth_index + 1
                            else:
                                leftbits_num_decoded = self.bits_to_bytes(leftbits_num, (len(leftbits_num)/10))
                                leftbits_num_int = int.from_bytes(leftbits_num_decoded, "little")
                                db_bits = self.leftover_bits[:y]
                                db_decoded = self.bits_to_bytes(db_bits, 26)
                                db_int = int.from_bytes(db_decoded, "little")
                                data_db_type = 'challenge_auth_response_payload_salt'
                                data_db_data['raw'] = hex(db_int)
                                print(f'Challenge AUTH response Payload: Salt: [{hex(leftbits_num_int)}]')
                                self.leftover_bits = self.leftover_bits[y:]
                                next = yield AnalyzerFrame(data_db_type, self.leftover_time[0], self.leftover_time_end[y - 1], data_db_data)
                                self.leftover_time = self.leftover_time[y:]
                                self.leftover_time_end = self.leftover_time_end[y:]
                                self.leftover_bits.append(next.data['data'])
                                self.leftover_time.append(next.start_time)
                                self.leftover_time_end.append(next.end_time)
                        if challenge_auth_index == 2:
                            if (320 - len(leftbits_num)) > 260:
                                y = 260
                            else:
                                y = 320 - len(leftbits_num)
                            yield from self.get_bits(getbits_num)
                            leftbits_num.extend(self.leftover_bits[:y])
                            if len(leftbits_num) == 320:
                                leftbits_num_decoded = self.bits_to_bytes(leftbits_num, 32)
                                leftbits_num_int = int.from_bytes(leftbits_num_decoded, "little")
                                db_bits = self.leftover_bits[:y]
                                db_decoded = self.bits_to_bytes(db_bits, (y/10))
                                db_int = int.from_bytes(db_decoded, "little")
                                data_db_type = 'challenge_auth_response_payload_contexthash'
                                data_db_data['raw'] = hex(db_int)
                                print(f'Challenge AUTH response Payload: Context Hash: [{hex(leftbits_num_int)}]')
                                self.leftover_bits = self.leftover_bits[y:]
                                #leftbits_num = []
                                leftbits_num = self.leftover_bits
                                next = yield AnalyzerFrame(data_db_type, self.leftover_time[0], self.leftover_time_end[y - 1], data_db_data)
                                self.leftover_time = self.leftover_time[y:]
                                self.leftover_time_end = self.leftover_time_end[y:]
                                self.leftover_bits.append(next.data['data'])
                                self.leftover_time.append(next.start_time)
                                self.leftover_time_end.append(next.end_time) 
                                challenge_auth_index = challenge_auth_index + 1            
                            else:
                                leftbits_num_decoded = self.bits_to_bytes(leftbits_num, (len(leftbits_num)/10))
                                leftbits_num_int = int.from_bytes(leftbits_num_decoded, "little")
                                db_bits = self.leftover_bits[:y]
                                db_decoded = self.bits_to_bytes(db_bits, 26)
                                db_int = int.from_bytes(db_decoded, "little")
                                data_db_type = 'challenge_auth_response_payload_contexthash'
                                data_db_data['raw'] = hex(db_int)
                                print(f'Challenge AUTH response Payload: Salt: [{hex(leftbits_num_int)}]')
                                self.leftover_bits = self.leftover_bits[y:]
                                next = yield AnalyzerFrame(data_db_type, self.leftover_time[0], self.leftover_time_end[y - 1], data_db_data)
                                self.leftover_time = self.leftover_time[y:]
                                self.leftover_time_end = self.leftover_time_end[y:]
                                self.leftover_bits.append(next.data['data'])
                                self.leftover_time.append(next.start_time)
                                self.leftover_time_end.append(next.end_time)
                        if challenge_auth_index == 3:
                            if (640 - len(leftbits_num)) > 260:
                                y = 260
                            else:
                                y = 640 - len(leftbits_num)
                            yield from self.get_bits(getbits_num)
                            leftbits_num.extend(self.leftover_bits[:y])
                            if len(leftbits_num) == 640:
                                leftbits_num_decoded = self.bits_to_bytes(leftbits_num, 64)
                                leftbits_num_int = int.from_bytes(leftbits_num_decoded, "little")
                                db_bits = self.leftover_bits[:y]
                                db_decoded = self.bits_to_bytes(db_bits, (y/10))
                                db_int = int.from_bytes(db_decoded, "little")
                                data_db_type = 'challenge_auth_response_payload_signature'
                                data_db_data['raw'] = hex(db_int)
                                print(f'Challenge AUTH response Payload: Context Hash: [{hex(leftbits_num_int)}]')
                                self.leftover_bits = self.leftover_bits[y:]
                                #leftbits_num = []
                                leftbits_num = self.leftover_bits
                                next = yield AnalyzerFrame(data_db_type, self.leftover_time[0], self.leftover_time_end[y - 1], data_db_data)
                                self.leftover_time = self.leftover_time[y:]
                                self.leftover_time_end = self.leftover_time_end[y:]
                                self.leftover_bits.append(next.data['data'])
                                self.leftover_time.append(next.start_time)
                                self.leftover_time_end.append(next.end_time) 
                                challenge_auth_index = challenge_auth_index + 1
                            else:
                                leftbits_num_decoded = self.bits_to_bytes(leftbits_num, (len(leftbits_num)/10))
                                leftbits_num_int = int.from_bytes(leftbits_num_decoded, "little")
                                db_bits = self.leftover_bits[:y]
                                db_decoded = self.bits_to_bytes(db_bits, 26)
                                db_int = int.from_bytes(db_decoded, "little")
                                data_db_type = 'challenge_auth_response_payload_signature'
                                data_db_data['raw'] = hex(db_int)
                                print(f'Challenge AUTH response Payload: Salt: [{hex(leftbits_num_int)}]')
                                self.leftover_bits = self.leftover_bits[y:]
                                next = yield AnalyzerFrame(data_db_type, self.leftover_time[0], self.leftover_time_end[y - 1], data_db_data)
                                self.leftover_time = self.leftover_time[y:]
                                self.leftover_time_end = self.leftover_time_end[y:]
                                self.leftover_bits.append(next.data['data'])
                                self.leftover_time.append(next.start_time)
                                self.leftover_time_end.append(next.end_time)
                elif header_data['command_code'] == 'PPS_Status':                
                    yield from self.get_bits(getbits_num)
                    db_bits = self.leftover_bits[:getbits_num]
                    db_decoded = self.bits_to_bytes(db_bits, getbytes_num)
                    db_int = int.from_bytes(db_decoded, "little")
                    frame_type, data_db_data = decode_pps_status(db_int)
                    data_db_type = frame_type
                    data_db_data['raw'] = hex(db_int)
                    print(f'PPS_Status: {data_db_data}')
                    self.leftover_bits = self.leftover_bits[getbits_num:]
                    next = yield AnalyzerFrame(data_db_type, self.leftover_time[0], self.leftover_time_end[getbits_num - 1], data_db_data)
                    self.leftover_time = self.leftover_time[getbits_num:]
                    self.leftover_time_end = self.leftover_time_end[getbits_num:]
                    self.leftover_bits.append(next.data['data'])
                    self.leftover_time.append(next.start_time)
                    self.leftover_time_end.append(next.end_time)
                elif header_data['command_code'] == 'Country_Codes':                
                    yield from self.get_bits(getbits_num)
                    db_bits = self.leftover_bits[:getbits_num]
                    db_decoded = self.bits_to_bytes(db_bits, getbytes_num)
                    db_int = int.from_bytes(db_decoded, "little")
                    frame_type, data_db_data = decode_country_codes(db_int)
                    data_db_type = frame_type
                    data_db_data['raw'] = hex(db_int)
                    print(f'Country_Codes: {data_db_data}')
                    self.leftover_bits = self.leftover_bits[getbits_num:]
                    next = yield AnalyzerFrame(data_db_type, self.leftover_time[0], self.leftover_time_end[getbits_num - 1], data_db_data)
                    self.leftover_time = self.leftover_time[getbits_num:]
                    self.leftover_time_end = self.leftover_time_end[getbits_num:]
                    self.leftover_bits.append(next.data['data'])
                    self.leftover_time.append(next.start_time)
                    self.leftover_time_end.append(next.end_time)
                elif header_data['command_code'] == 'Country_Info':                
                    yield from self.get_bits(getbits_num)
                    db_bits = self.leftover_bits[:getbits_num]
                    db_decoded = self.bits_to_bytes(db_bits, getbytes_num)
                    db_int = int.from_bytes(db_decoded, "little")
                    frame_type, data_db_data = decode_country_info(db_int, getbytes_num)
                    data_db_type = frame_type
                    data_db_data['raw'] = hex(db_int)
                    print(f'Country_Info: {data_db_data}')
                    self.leftover_bits = self.leftover_bits[getbits_num:]
                    next = yield AnalyzerFrame(data_db_type, self.leftover_time[0], self.leftover_time_end[getbits_num - 1], data_db_data)
                    self.leftover_time = self.leftover_time[getbits_num:]
                    self.leftover_time_end = self.leftover_time_end[getbits_num:]
                    self.leftover_bits.append(next.data['data'])
                    self.leftover_time.append(next.start_time)
                    self.leftover_time_end.append(next.end_time)
                elif header_data['command_code'] == 'Vendor_Defined_Extended':  
                    if reqchunk == 0 and chunkednum == 0:
                        db_array = []
                        yield from self.get_bits(40)
                        db_bits = self.leftover_bits[:40]
                        db_decoded = self.bits_to_bytes(db_bits, 4)
                        db_int = int.from_bytes(db_decoded, "little")
                        frame_type, data_db_data = decode_vendor_header_data_object_31(db_int)
                        data_db_type = frame_type
                        data_db_data['raw'] = hex(db_int)
                        print(f'Vendor_Defined_Extended: VDM Header: {data_db_data}')
                        self.leftover_bits = self.leftover_bits[40:]
                        next = yield AnalyzerFrame(data_db_type, self.leftover_time[0], self.leftover_time_end[39], data_db_data)
                        self.leftover_time = self.leftover_time[40:]
                        self.leftover_time_end = self.leftover_time_end[40:]
                        self.leftover_bits.append(next.data['data'])
                        self.leftover_time.append(next.start_time)
                        self.leftover_time_end.append(next.end_time)
                        for db_index in range(4, getbytes_num):
                            db_bits = self.leftover_bits[:10]
                            db_decoded = self.bits_to_bytes(db_bits, 1)
                            db_int = int.from_bytes(db_decoded, "little")
                            data_db_type = 'pdfu_datablock'
                            data_db_data['offset'] = db_index
                            data_db_data['datablock'] = hex(db_int)
                            db_array.append(hex(db_int))
                            self.leftover_bits = self.leftover_bits[10:]
                            next = yield AnalyzerFrame(data_db_type, self.leftover_time[0], self.leftover_time_end[9], data_db_data)
                            self.leftover_time = self.leftover_time[10:]
                            self.leftover_time_end = self.leftover_time_end[10:]
                            self.leftover_bits.append(next.data['data'])
                            self.leftover_time.append(next.start_time)
                            self.leftover_time_end.append(next.end_time)
                        print(f'Vendor_Defined_Extended: Datablock: [{db_array}]')
                    if reqchunk == 0 and chunkednum >= 1: 
                        for db_index in range(getbytes_num):
                            yield from self.get_bits(10)
                            db_bits = self.leftover_bits[:10]
                            db_decoded = self.bits_to_bytes(db_bits, 1)
                            db_int = int.from_bytes(db_decoded, "little")
                            data_db_type = 'pdfu_datablock'
                            data_db_data['offset'] = (chunkednum*26) + db_index
                            data_db_data['datablock'] = hex(db_int)
                            db_array.append(hex(db_int))
                            self.leftover_bits = self.leftover_bits[10:]
                            next = yield AnalyzerFrame(data_db_type, self.leftover_time[0], self.leftover_time_end[9], data_db_data)
                            self.leftover_time = self.leftover_time[10:]
                            self.leftover_time_end = self.leftover_time_end[10:]
                            self.leftover_bits.append(next.data['data'])
                            self.leftover_time.append(next.start_time)
                            self.leftover_time_end.append(next.end_time)
                        print(f'Vendor_Defined_Extended: Datablock: [{db_array}]')
                        
                else:
                    if reqchunk == 0:                   
                        for db_index in range(chunkednum * 26, ((chunkednum * 26) + getbytes_num)):
                            yield from self.get_bits(10)
                            db_bits = self.leftover_bits[:10]
                            db_decoded = self.bits_to_bytes(db_bits, 1)
                            db_int = int.from_bytes(object_decoded, "little")
                            data_db_type = 'Unknown Data Block'
                            data_db_data['index'] = db_index
                            data_db_data['raw'] = hex(object_int) 
                            print('Unknown Data Block',':',data_db_data)
                            self.leftover_bits = self.leftover_bits[10:]
                            next = yield AnalyzerFrame(data_db_type, self.leftover_time[0], self.leftover_time_end[9], data_db_data)
                            self.leftover_time = self.leftover_time[10:]
                            self.leftover_time_end = self.leftover_time_end[10:]
                            self.leftover_bits.append(next.data['data'])
                            self.leftover_time.append(next.start_time)
                            self.leftover_time_end.append(next.end_time)            
                
            else:
                VDO_header_command = []
                VDO_header_command_type = []
                product_type_ufp = []
                product_type_dfp = []
                unchecked_ext_source_support = 0
                unchecked_ext_sink_support = 0
                n = 0
                SVID = []
                for object_index in range(1, object_count+1):
                    yield from self.get_bits(40)
                    object_decoded = self.bits_to_bytes(self.leftover_bits, 4)
                    object_int = int.from_bytes(object_decoded, "little")
                    data_object_data = {
                        'index': object_index, 'data': hex(object_int)}
                    data_object_type = 'object'

                    if header_data['command_code'] == 'Source_Capabilities':
                        frame_type, data_object_data = decode_source_power_data_object(
                            object_int, object_index)
                        data_object_type = frame_type
                        data_object_data['index'] = object_index
                        data_object_data['raw'] = hex(object_int)
                        self.source_capabilities_pdo_types[object_index] = data_object_data['pdo_type']
                    if header_data['command_code'] == 'Request':
                        object_position = (object_int >> 28) & 0x7
                        if len(self.source_capabilities_pdo_types) >= object_position:
                            source_capabilities_pdo_type = self.source_capabilities_pdo_types[object_position]
                            frame_type, data_object_data = decode_request_data_object(
                                object_int, source_capabilities_pdo_type)
                            data_object_type = frame_type
                            #data_object_data['index'] = object_index
                            data_object_data['raw'] = hex(object_int)
                        else:
                            data_object_type = 'error'
                            data_object_data = { 'error': '"Request" for object position "{}" did not exist in "Source_Capabilities"', 'raw': hex(object_int) }
                    if header_data['command_code'] == 'EPR_Request':
                        if object_index == 1:
                            object_position = (object_int >> 28) & 0xF
                            if len(self.epr_source_capabilities_pdo_types) >= object_position:
                                epr_source_capabilities_pdo_type = self.epr_source_capabilities_pdo_types[object_position]
                                frame_type, data_object_data = decode_request_data_object(
                                    object_int, epr_source_capabilities_pdo_type)
                                data_object_type = frame_type
                                #data_object_data['index'] = object_index
                                data_object_data['raw'] = hex(object_int)
                            else:
                                data_object_type = 'error'
                                data_object_data = { 'error': '"Request" for object position "{}" did not exist in "Source_Capabilities"', 'raw': hex(object_int) }
                        if object_index == 2:
                            frame_type, data_object_data = decode_source_power_data_object(
                                object_int, object_position)
                            data_object_type = frame_type
                            data_object_data['index'] = object_position
                            data_object_data['raw'] = hex(object_int)  
                    if header_data['command_code'] == 'BIST':
                        frame_type, data_object_data = decode_bist_data_object(
                            object_int, object_index)
                        data_object_type = frame_type
                        data_object_data['index'] = object_index
                        data_object_data['raw'] = hex(object_int)
                    if header_data['command_code'] == 'Sink_Capabilities':
                        frame_type, data_object_data = decode_sink_power_data_object(
                            object_int, object_index)
                        data_object_type = frame_type
                        data_object_data['index'] = object_index
                        data_object_data['raw'] = hex(object_int)
                    if header_data['command_code'] == 'Battery_Status':
                        frame_type, data_object_data = decode_battery_status_data_object(
                            object_int)
                        data_object_type = frame_type
                        data_object_data['index'] = object_index
                        data_object_data['raw'] = hex(object_int)
                    if header_data['command_code'] == 'Alert':
                        frame_type, data_object_data = decode_alert_data_object(
                            object_int)
                        data_object_type = frame_type
                        data_object_data['index'] = object_index
                        data_object_data['raw'] = hex(object_int)
                    if header_data['command_code'] == 'Get_Country_Info':
                        frame_type, data_object_data = decode_get_country_info_data_object(
                            object_int)
                        data_object_type = frame_type
                        data_object_data['index'] = object_index
                        data_object_data['raw'] = hex(object_int)
                    if header_data['command_code'] == 'Enter_USB':
                        frame_type, data_object_data = decode_enter_usb_data_object(
                            object_int)
                        data_object_type = frame_type
                        data_object_data['index'] = object_index
                        data_object_data['raw'] = hex(object_int)
                    if header_data['command_code'] == 'Vendor_Defined' and object_index == 1:
                        #frame_type, data_object_data = decode_vendor_header_data_object(object_int)
                        #For PD3.1
                        frame_type, data_object_data = decode_vendor_header_data_object_31(object_int)
                        data_object_type = frame_type
                        data_object_data['index'] = object_index
                        data_object_data['raw'] = hex(object_int)
                        VDO_header_command = data_object_data['command']
                        VDO_header_command_type = data_object_data['command_type']
                        SVID = data_object_data['vendor_id']
                    if VDO_header_command == 'Discover Identity' and VDO_header_command_type == 'ACK':
                        if object_index == 2:
                            frame_type, data_object_data = decode_id_header_data_object(
                                object_int, address_cmd['address'])
                            #frame_type, data_object_data = decode_id_header_data_object_3.1(
                            #    object_int, address_cmd)
                            data_object_type = frame_type
                            data_object_data['index'] = object_index
                            data_object_data['raw'] = hex(object_int)
                            product_type_ufp = data_object_data['product_type_ufp']
                            product_type_dfp = data_object_data['product_type_dfp']
                        if object_index == 3:
                            frame_type, data_object_data = decode_cert_stat_vdo(
                                object_int)
                            data_object_type = frame_type
                            data_object_data['index'] = object_index
                            data_object_data['raw'] = hex(object_int)
                        if object_index == 4:
                            frame_type, data_object_data = decode_product_vdo(
                                object_int)
                            data_object_type = frame_type
                            data_object_data['index'] = object_index
                            data_object_data['raw'] = hex(object_int)
                        if object_index == 5:
                            if product_type_ufp == 'PDUSB Hub' or product_type_ufp == 'PDUSB Peripheral':
                                frame_type, data_object_data = decode_ufp_vdo1(
                                    object_int)
                                data_object_type = frame_type
                                data_object_data['index'] = object_index
                                data_object_data['raw'] = hex(object_int)
                            if product_type_ufp == 'Alternate Mode Adapter':
                                frame_type, data_object_data = decode_ama_vdo(
                                    object_int)
                                data_object_type = frame_type
                                data_object_data['index'] = object_index
                                data_object_data['raw'] = hex(object_int)
                            if product_type_ufp == 'VCONN-Powered USB Device':
                                frame_type, data_object_data = decode_vdp_vdo(
                                    object_int)
                                data_object_type = frame_type
                                data_object_data['index'] = object_index
                                data_object_data['raw'] = hex(object_int)
                            if product_type_ufp == 'Active Cable':
                                frame_type, data_object_data = decode_activecable_vdo1(
                                    object_int)
                                data_object_type = frame_type
                                data_object_data['index'] = object_index
                                data_object_data['raw'] = hex(object_int)
                            if product_type_ufp == 'Passive Cable':
                                frame_type, data_object_data = decode_passivecable_vdo(
                                    object_int)
                                data_object_type = frame_type
                                data_object_data['index'] = object_index
                                data_object_data['raw'] = hex(object_int)
                        if object_index == 6:
                            if product_type_ufp == 'PDUSB Hub' or product_type_ufp == 'PDUSB Peripheral':
                                frame_type, data_object_data = decode_ufp_vdo2(
                                    object_int)
                                data_object_type = frame_type
                                data_object_data['index'] = object_index
                                data_object_data['raw'] = hex(object_int)
                            if product_type_ufp == 'Active Cable':
                                frame_type, data_object_data = decode_activecable_vdo2(
                                    object_int)
                                data_object_type = frame_type
                                data_object_data['index'] = object_index
                                data_object_data['raw'] = hex(object_int)
                        if object_index == 7:
                            if product_type_dfp == 'PDUSB Hub' or product_type_dfp == 'PDUSB Host' or product_type_dfp == 'Power Brick':
                                frame_type, data_object_data = decode_dfp_vdo(
                                    object_int)
                                data_object_type = frame_type
                                data_object_data['index'] = object_index
                                data_object_data['raw'] = hex(object_int)
                    if VDO_header_command == 'Discover SVIDs' and VDO_header_command_type == 'ACK':    
                        frame_type, data_object_data, n = decode_dsvid_vdo(
                            object_int, n)
                        data_object_type = frame_type
                        #data_object_data['index'] = object_index
                        data_object_data['raw'] = hex(object_int) 
                    if VDO_header_command == 'Discover Modes' and VDO_header_command_type == 'ACK' and SVID == '0xff01' and object_index == 2 :    
                        frame_type, data_object_data, n = decode_dp_mode(
                            object_int, n)
                        data_object_type = frame_type
                        data_object_data['mode_index'] = n
                        data_object_data['raw'] = hex(object_int)   
                    if VDO_header_command == 'DisplayPort Status update' and SVID == '0xff01' and object_index == 2 :    
                        frame_type, data_object_data = decode_dp_status(
                            object_int)
                        data_object_type = frame_type
                        data_object_data['raw'] = hex(object_int)
                    if VDO_header_command == 'DisplayPort Configure' and SVID == '0xff01' and object_index == 2 :    
                        frame_type, data_object_data = decode_dp_configure(
                            object_int)
                        data_object_type = frame_type
                        data_object_data['raw'] = hex(object_int)
                    if VDO_header_command == 'Attention' and VDO_header_command_type == 'REQ' and SVID == '0xff01' and object_index == 2 :
                        frame_type, data_object_data = decode_dp_status(
                            object_int)
                        data_object_type = frame_type
                        data_object_data['raw'] = hex(object_int)
                    if VDO_header_command == 'Discover Modes' and VDO_header_command_type == 'ACK' and SVID == '0x8087' and object_index == 2 :    
                        frame_type, data_object_data = decode_tbt_mode(
                            object_int, address_cmd)
                        data_object_type = frame_type
                        data_object_data['raw'] = hex(object_int)
                    if VDO_header_command == 'Enter Mode' and VDO_header_command_type == 'REQ' and SVID == '0x8087' and object_index == 2 :    
                        frame_type, data_object_data = decode_tbt_enter_mode(
                            object_int)
                        data_object_type = frame_type
                        data_object_data['raw'] = hex(object_int)
                    if VDO_header_command == 'Attention' and VDO_header_command_type == 'REQ' and SVID == '0x8087' and object_index == 2 :    
                        frame_type, data_object_data = decode_tbt_attention(
                            object_int)
                        data_object_type = frame_type
                        data_object_data['raw'] = hex(object_int)
                    if header_data['command_code'] == 'EPR_Mode' and object_index == 1 :
                        frame_type, data_object_data = decode_eprmode(
                            object_int)
                        data_object_type = frame_type
                        data_object_data['raw'] = hex(object_int)

                    print(header_data['command_code'],':', data_object_data)
                    next = yield AnalyzerFrame(data_object_type, self.leftover_time[0], self.leftover_time_end[39], data_object_data)
                    self.leftover_bits = self.leftover_bits[40:]
                    self.leftover_time = self.leftover_time[40:]
                    self.leftover_time_end = self.leftover_time_end[40:]
                    self.leftover_bits.append(next.data['data'])
                    self.leftover_time.append(next.start_time)
                    self.leftover_time_end.append(next.end_time)
            #
            yield from self.get_bits(40)
            crc_decoded = self.bits_to_bytes(self.leftover_bits, 4)
            crc_int = int.from_bytes(crc_decoded, "little")
            print('crc {crc}'.format(crc=hex(crc_int)))
            next = yield AnalyzerFrame('crc', self.leftover_time[0], self.leftover_time_end[39], {'crc': hex(crc_int)})
            self.leftover_bits = self.leftover_bits[40:]
            self.leftover_time = self.leftover_time[40:]
            self.leftover_time_end = self.leftover_time_end[40:]
            self.leftover_bits.append(next.data['data'])
            self.leftover_time.append(next.start_time)
            self.leftover_time_end.append(next.end_time)
            #
            #
            yield from self.get_bits(5)
            eop_cmd = self.decode_eop(self.leftover_bits)
            print(eop_cmd['eop'])
            #if eop_cmd['eop'] == 'Missing the EOP' :
            #   import sys
            #   sys.exit()
            next = yield AnalyzerFrame('eop', self.leftover_time[0], self.leftover_time_end[4], eop_cmd)
            self.leftover_bits = self.leftover_bits[5:]
            self.leftover_time = self.leftover_time[5:]
            self.leftover_time_end = self.leftover_time_end[5:]
            self.leftover_bits.append(next.data['data'])
            self.leftover_time.append(next.start_time)
            self.leftover_time_end.append(next.end_time)


    def get_bits_preamble(self, preamble_start, preamble_end, num_bits):
        bits_needed = int(num_bits - len(self.leftover_bits))
        #print('bits_needed',bits_needed)
        word_start = None
        word_end = None
        raw_bits = []
        raw_bits = self.leftover_bits
        if bits_needed == 0:
            word_start = preamble_start
            word_end = preamble_end
            return Word(word_start, word_end, raw_bits)
        else:
            for x in range(bits_needed):
                frame = yield
                raw_bits.append(frame.data['data'])
                preamble_start.append(frame.start_time)
                preamble_end.append(frame.end_time)

            word_start = preamble_start
            word_end = preamble_end
            return Word(word_start, word_end, raw_bits)

    def get_bits(self, num_bits):
        bits_needed = int(num_bits - len(self.leftover_bits))
        #print('bits_needed',bits_needed)
        if bits_needed == 0:

            return Word(self.leftover_time, self.leftover_time_end, self.leftover_bits)
        else:       
            for x in range(bits_needed):
                frame = yield
                #print(frame.data)
                self.leftover_bits.append(frame.data['data'])
                self.leftover_time.append(frame.start_time)
                self.leftover_time_end.append(frame.end_time)
            return Word(self.leftover_time, self.leftover_time_end, self.leftover_bits)

    def bits_to_bytes(self, new_bits, num_bytes):
        decoded = bytearray(num_bytes)
        # leftovers is an array in time order. everything is LSB first (bytes and bits) in USB pd anyway.
        # get everything into a huge array of bits
        for i in range(num_bytes):
            # convert 10 bits to 8 bits, save in decoded.
            fiver = new_bits[:5]
            nibble = self.decode5bits(fiver)
            new_bits = new_bits[5:]
            decoded[i] = nibble
            nibble = self.decode5bits(new_bits[:5])
            new_bits = new_bits[5:]
            decoded[i] |= nibble << 4
        return decoded

    def decode5bits(self, bit_array):
        raw_word = 0
        for i in range(5):
            raw_word = raw_word | (bit_array[i] << i)
        new_word = -1
        for entry in encoding_lookup:
            if encoding_lookup[entry] == raw_word:
                new_word = entry
                break
        if new_word == -1:
            new_word = 0
        return new_word

    def decode_preamble(self, bits):
        for preamble in Preamble_LSB:
            #load address from addresses
            raw_preamble = Preamble_LSB[preamble]
            match = True
            data={'preamble': 'Missing the Preamble',
            }         
            if bits[0]==0:
                for i in range(64):
                    if bits[i] != raw_preamble[i]:
                        match = False
                if match == True:
                    data={'preamble': preamble,
                    }
                    return data                 
            elif bits[0]==1:
                for i in range(63):
                    if bits[i] != raw_preamble[i]:
                        match = False
                if match == True:
                    data={'preamble': preamble,
                    }
                    return data
        return data

    def decode_address(self, bits):
        for address in addresses:
            #load address from addresses
            raw_address = addresses[address]
            #print(raw_address)
            fiddle_sop = []
            #convert addresses to LSB first
            for word in range(4):
                #print(word)
                for bit in range(5):
                    fiddle_sop.append(raw_address[word * 5 + 4 - bit])
                    #print(fiddle_sop)
            match = True
            data = {'address': 'Missing the SOP',
            }                      
            for i in range(20):
                if bits[i] != fiddle_sop[i]:
                    match = False
            if match == True:
                data = {'address': address,
                }
                return data
        return data                      

    def decode_header(self, header, sop_type):
        extended = (header >> 15) & 0x01
        number_of_objects = (header >> 12) & 0x07
        message_id = (header >> 9) & 0x07
        _spec_revision = (header >> 6) & 0x03
        spec_revision = revision[_spec_revision]
        command_code = header & 0x1F
        if extended == 0x1:
            command_code = extended_commands[command_code]
        else:
            if number_of_objects == 0: #Message is defined as a Control Message
                if command_code in control_commands:
                    command_code = control_commands[command_code]
            else:
                if command_code in data_commands:
                    command_code = data_commands[command_code]

        data = {
            'Extended': extended,
            'command_code': str(command_code),
            'number_of_objects': number_of_objects,
            'message_id': message_id,
            'spec_revision': str(spec_revision),
        }

        if sop_type == 'SOP':
            _power_port_role = (header >> 8) & 0x01
            _port_data_role = (header >> 5) & 0x01
            data['power_port_role'] = power_port_role[_power_port_role]
            data['port_data_role'] = port_data_role[_port_data_role]
        else:
            _cable_plug = (header >> 8) & 0x01
            data['cable_plug'] = cable_plug[_cable_plug]
        return data

    def decode_eop(self, bits):
        for EOP in EOP_LSB:
            #load address from addresses
            raw_eop = EOP_LSB[EOP]
            match = True
            data = {'eop': 'Missing the EOP',
            }      
            for i in range(5):
                if bits[i] != raw_eop[i]:
                    match = False
            if match == True:
                data = {'eop': EOP,
                }
                return data
        return data
        
    def decode_ext_header(self, header):
        data = {
            'data_object_type': 'Extended Message Header'
        }
        chunked = (header >> 15) & 0x1
        chunked_number = (header >> 11) & 0xF
        request_chunk = (header >> 10) & 0x1
        data_size = header & 0x1FF
        data['chunked'] = chunked
        data['chunked_number'] = chunked_number
        data['request_chunk'] = request_chunk
        data['data_size'] = data_size
        
        return data
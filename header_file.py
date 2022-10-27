import enum

from sqlalchemy import false, true

class FrozenClass(object):
    __isfrozen = False
    def __setattr__(self, key, value):
        if self.__isfrozen and not hasattr(self, key):
            raise TypeError( "%r is a frozen class" % self )
        object.__setattr__(self, key, value)

    def _freeze(self):
        self.__isfrozen = True

class score_board(FrozenClass):
    __imsi_detach_indication = 0
    __location_update_request = 0
    __authentication_request = 0
    __location_accept = 0
    __pattern_points = 0
    __attach_accept = 0
    __attach_complete = 0
    __auth_and_cipher = 0
    __ciphering_mode_command = 0
    __rrc_connection_request = 0
    __rrc_connection_setup = 0
    __rrc_security_mode_command = 0 
    __rrc_connection_reconfiguration = 0
    def __init__(self) -> None:
        self._freeze() # no new attributes after this point.

    def set_imsi_detach_indication(self, imsi_detach_indication):
        score_board.__imsi_detach_indication = imsi_detach_indication
    
    def get_imsi_detach_indication(self):
        return score_board.__imsi_detach_indication
    
    def set_location_update_request(self, location_update_request):
        score_board.__location_update_request = location_update_request
    
    def get_location_update_request(self):
        return score_board.__location_update_request

    def set_location_accept(self, location_accept):
        score_board.__location_accept = location_accept
    
    def get_location_accept(self):
        return score_board.__location_accept

    def set_authentication_request(self, authentication_request):
        score_board.__authentication_request = authentication_request
    
    def get_authentication_request(self):
        return score_board.__authentication_request

    def set_attach_accept(self, attach_accept):
        score_board.__attach_accept = attach_accept
    
    def get_attach_accept(self):
        return score_board.__attach_accept

    def set_attach_complete(self, attach_complete):
        score_board.__attach_complete = attach_complete
    
    def get_attach_complete(self):
        return score_board.__attach_complete

    def set_auth_and_cipher(sefl, auth_and_cipher):
        score_board.__auth_and_cipher = auth_and_cipher
    
    def get_auth_and_cipher(self):
        return score_board.__auth_and_cipher

    def set_pattern_points(self, pattern_points):
        score_board.__pattern_points = pattern_points

    def get_pattern_points(self):
        return score_board.__pattern_points
    
    def set_cipher_mode_command(self, cipher_mode_command):
        score_board.__ciphering_mode_command = cipher_mode_command

    def get_ciphering_mode_command(self):
        return score_board.__ciphering_mode_command
    
    def set_rrc_connection_request(self, rrc_connection_request):
        score_board.__rrc_connection_request = rrc_connection_request

    def get_rrc_connection_request(self):
        return score_board.__rrc_connection_request
    
    def set_rrc_connection_setup(self, rrc_coonection_setup):
        score_board.__rrc_connection_setup = rrc_coonection_setup
    
    def get_rrc_connection_setup(self):
        return score_board.__rrc_connection_setup

    def set_rrc_security_mode_command(self, rrc_security_mode_command):
        score_board.__rrc_security_mode_command = rrc_security_mode_command

    def get_rrc_security_mode_command(self):
        return score_board.__rrc_security_mode_command    

    def set_rrc_connection_reconfiguration(self, rrc_connection_reconfiguration):
        score_board.__rrc_connection_reconfiguration = rrc_connection_reconfiguration
    
    def get_rrc_coonection_reconfiguration(self):
        return score_board.__rrc_connection_reconfiguration

    def get_overall_score(self):
        return (score_board.__imsi_detach_indication + score_board.__location_update_request + score_board.__authentication_request 
                + score_board.__pattern_points + score_board.__location_accept + score_board.__attach_accept + score_board.__attach_complete
                + score_board.__auth_and_cipher + score_board.__ciphering_mode_command + score_board.__rrc_connection_reconfiguration 
                + score_board.__rrc_connection_request + score_board.__rrc_connection_setup + score_board.__rrc_security_mode_command)

    def clear_points(self):
        score_board.__authentication_request = 0
        score_board.__imsi_detach_indication = 0
        score_board.__location_update_request = 0
        score_board.__pattern_points = 0
        score_board.__location_accept = 0
        score_board.__attach_accept = 0
        score_board.__attach_complete = 0
        score_board.__auth_and_cipher = 0
        score_board.__ciphering_mode_command = 0
        score_board.__rrc_security_mode_command = 0
        score_board.__rrc_connection_reconfiguration = 0
        score_board.__rrc_connection_request = 0
        score_board.__rrc_connection_setup = 0

class pattern_check(FrozenClass):
    __checker = 0
    __bit_mask = 127
    __bit_mask_lte = 31
    def __init__(self) -> None:
        self._freeze
    
    def set_checker(self, bit_index):
        pattern_check.__checker |= (1 << bit_index)

    def clear_bit(bit_index):
        pattern_check.__checker &= ~(1 << bit_index)

    def clear_checker(self):
        pattern_check.__checker = 0

    def get_checker(self):
        return pattern_check.__checker

    def check_bits(self):
        tmp = pattern_check.__checker & pattern_check.__bit_mask
        if(tmp == pattern_check.__checker):
            return True
        else:
            return False

    def check_bits_lte(self):
        tmp = pattern_check.__checker & pattern_check.__bit_mask_lte
        if(tmp == pattern_check.__bit_mask_lte):
            return true
        else:
            return false

class general_info(FrozenClass):
    __sip3_last_seen = None
    __cell_identity = None
    __location_update_request_last_seen = None
    __imsi = None
    __tmsi_mm = None
    __tmsi_gmm = None
    __imsi_catched = False
    __cell_id_on_attach = 0
    __rrc_request = False
    def __init__(self) -> None:
        self._freeze
    
    def set_imsi_catched(self, catch):
        general_info.__imsi_catched = catch

    def get_imsi_catched(self):
        return general_info.__imsi_catched

    def set_cell_id_on_attach(self, id):
        general_info.__cell_id_on_attach = id

    def get_cell_id_on_attach(self):
        return general_info.__cell_id_on_attach

    def set_sip3_last_seen(self, sip3_packet_num):
        general_info.__sip3_last_seen = sip3_packet_num
    
    def get_sip3_last_seen(self):
        return general_info.__sip3_last_seen
    
    def set_cell_identity(self, cell_id):
        general_info.__cell_identity = cell_id
    
    def get_cell_identity(self):
        return general_info.__cell_identity

    def set_location_update_req_last_seen(self, flag):
        general_info.__location_update_request_last_seen = flag
    
    def get_location_update_req_last_seen(self):
        return general_info.__location_update_request_last_seen

    def set_imsi(self, imsi):
        general_info.__imsi = imsi
    
    def get_imsi(self):
        return general_info.__imsi

    def set_tmsi_mm(self, tmsi_mm):
        general_info.__tmsi_mm = tmsi_mm

    def get_tmsi_mm(self):
        return general_info.__tmsi_mm

    def set_tmsi_gmm(self, tmsi_gmm):
        general_info.__tmsi_gmm = tmsi_gmm

    def get_tmsi_gmm(self):
        general_info.__tmsi_gmm

    def set_rrc_request(self, rrc_setup):
        general_info.__rrc_request = rrc_setup
    
    def get_rrc_request(self):
        return general_info.__rrc_request

    def clear_vars(self):
        general_info.__cell_identity = None
        general_info.__location_update_request_last_seen = None
        general_info.__sip3_last_seen = None
        general_info.__imsi = None
        general_info.__tmsi_gmm = None
        general_info.__tmsi_mm = None
        general_info.__imsi_catched = False
        general_info.__rrc_request = False

#change to all capital
class MM_TYPE_MSG(enum.Enum):
    IMSI_Detach_Indication = "0x1"
    Location_Updating_Accept = "0x2"
    Location_Updating_Reject = "0x4"
    Location_Updating_Request = "0x8"
    Authentication_Request = "0x12"
    Authentication_Response = "0x14"
    Identify_Request = "0x18"
    Identify_Response = "0x19"
    CM_SERVICE_REQUEST = "0x24"
    MM_Information = "0x32"

class GMM_TYPE_MSG(enum.Enum):
    Attach_Request = "0x1"
    Attach_Accept = "0x2"
    Attach_Complete = "0x3"
    Detach_Request = "0x5"
    Routing_Area_Update_Complete = "0xa"
    Routing_Area_Update_Accept = "0x9"
    Authentication_And_Ciphering_Request = "0x12"
    Authentication_And_Ciphering_Response = "0x13"
    Identity_Request = "0x15"
    Identity_Response = "0x16"
    GMM_Information = "0x21"

class RR_TYPE_MSG(enum.Enum):
    System_Information_Type_13 = "0x0"
    System_Information_Type_5ter = "0x6"
    System_Information_Type_2quater = "0x7"
    Channel_Release = "0xd"
    Measurement_Report = "0x15"
    Classmark_Change = "0x16"
    System_Information_Type_1 = "0x19"
    System_Information_Type_2 = "0x1a"
    System_Information_Type_3 = "0x1b"
    System_Information_Type_4 = "0x1c"
    System_Information_Type_5 = "0x1d"
    System_Information_Type_6 = "0x1e"
    Paging_Request_Type_1 = "0x21"
    Paging_Request_Type_2 = "0x22"
    Ciphering_Mode_Complete = "0x32"
    GPRS_Suspension_Request = "0x34"
    Ciphering_Mode_Command = "0x35"
    Immediate_Assignment = "0x3f"

class RRC_MESSAGE(enum.Enum):
    RRCConnectionRequest = "1"
    RRCConnectionSetup = "3"
    RRCConnectionReconfiguration = "4"
    RRCConnectionReleaseLte = "5"
    RRCSecurityModeCommand = "6"
    RRCUeCapabilityEnquiry = "7"
    RRCUeInformationRrequestR9 = "9"
    #MeasurementReport = "8" todo double check if this is valid
    RRCConnectionReleaseUmts = "15"
    RRCConnectionReleaseComplete = "17"
    RRCConnectionSetupComplete = "18"
    #UplinkDirectTransfer = "27" todo double check if this is valid

class EMM_TYPE_MSG(enum.Enum):
    Authentication_Request = "0x52"
    Security_Mode_Command = "0x5d"
    Identity_Request = "0x55"
    Tracking_Area_Update_Reject = "0x4b"

class SCORE_BOARD(enum.IntEnum):
    Points_IMSI_Detach_Indication_TMSI = 10
    Points_IMSI_Detach_Indication_IMSI = -10
    Points_Identify_Request_IMSI = -5 #probably this is invalid. Identify req is always imsi.
    Points_Identify_Request_TIMSI = 5 #probably this is invalid. Identify req is always imsi.
    Points_Location_Updating_Request_IMSI = -10
    Points_Location_Updating_Request_TMSI = 10 
    Points_Location_Reject = -10 
    Points_Location_Accept = 10
    Points_Authentication_Request = 10
    Points_Authentication_Request_not_asking = -10 #check if it's asking (imsi catcher)
    Points_Attach_Complete = 10
    Points_Attach_Accept = 10
    Points_Pattern = 50
    Points_Authentication_And_Ciphering_Request = 10
    Points_Ciphering_Mode_Command = 10
    Points_RRC_Connection_Request = 10
    Points_RRC_Connection_Setup = 10
    Points_RRC_Security_Mode_Command = 10
    Points_RRC_Connection_Reconfguration = 10
    Legit_Operator = 90
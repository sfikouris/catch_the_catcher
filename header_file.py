from cmath import nan
import enum
from telnetlib import AUTHENTICATION

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

    def get_overall_score(self):
        return (score_board.__imsi_detach_indication + score_board.__location_update_request + score_board.__authentication_request 
                + score_board.__pattern_points + score_board.__location_accept + score_board.__attach_accept + score_board.__attach_complete
                + score_board.__auth_and_cipher)

    def clear_points(self):
        score_board.__authentication_request = 0
        score_board.__imsi_detach_indication = 0
        score_board.__location_update_request = 0
        score_board.__pattern_points = 0
        score_board.__location_accept = 0
        score_board.__attach_accept = 0
        score_board.__attach_complete = 0
        score_board.__auth_and_cipher = 0

class pattern_check(FrozenClass):
    __checker = 0
    __bit_mask = 31
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
        if(tmp == pattern_check.__bit_mask):
            return True
        else:
            return False

class general_info(FrozenClass):
    __sip3_last_seen = nan
    __cell_identity = nan
    __location_update_request_last_seen = False
    def __init__(self) -> None:
        self._freeze
    
    def set_sip3_last_seen(self, sip3_packet_num):
        general_info.__sip3_last_seen = sip3_packet_num
    
    def get_sip3_last_seen(self):
        return general_info.__sip3_last_seen
    
    def set_cell_identity(self, cell_id):
        general_info.__cell_identity = cell_id
    
    def get_cell_identity(self):
        return general_info.__cell_identity

    def set_location_update_req_last_seen(self):
        general_info.__location_update_request_last_seen = True
    
    def get_location_update_req_last_seen(self):
        return general_info.__location_update_request_last_seen

    def clear_vars(self):
        general_info.__cell_identity = nan
        general_info.__location_update_request_last_seen = False
        general_info.__sip3_last_seen = nan

#change to all capital
class GSM_MSG_MM_TYPE(enum.Enum):
    IMSI_Detach_Indication = "0x1"
    Location_Updating_Accept = "0x2"
    Location_Updating_Reject = "0x4"
    Location_Updating_Request = "0x8"
    Authentication_Request = "0x12"
    Authentication_Response = "0x14"
    Identify_Request = "0x18"
    Identify_Response = "0x19"
    MM_Information = "0x32"

class GSM_MSG_GMM_TYPE(enum.Enum):
    ATTACH_REQUEST = "0x1"
    ATTACH_ACCEPT = "0x2"
    ATTACH_COMPLETE = "0x3"
    DETACH_REQUEST = "0x5"
    AUTHENTICATION_AND_CIPHERING_REQUEST = "0x12"
    AUTHENTICATION_AND_CIPHERING_RESPONSE = "0x13"
    GMM_INFROMATION = "0x21"

class GSM_MSG_RR_TYPE(enum.Enum):
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
    GPRS_Suspension_Request = "0x34"
    Ciphering_Mode_Command = "0x35"
    Immediate_Assignment = "0x3f"



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
    Points_GSM_Pattern = 50
    Points_Authentication_And_Ciphering_Request = 10
    Legit_Operator = 110

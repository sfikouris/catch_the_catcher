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
    def __init__(self) -> None:
        self.__imsi_detach_indication = 0
        self.__location_update_request = 0
        self.__authentication_request = 0
        self._freeze() # no new attributes after this point.

    def set_imsi_detach_indication(self, imsi_detach_indication):
        self.__imsi_detach_indication = imsi_detach_indication
    
    def get_imsi_detach_indication(self):
        return self.__imsi_detach_indication
    
    def set_location_update_request(self, location_update_request):
        self.__location_update_request = location_update_request
    
    def get_location_update_request(self):
        return self.__location_update_request

    def set_authentication_request(self, authentication_request):
        self.__authentication_request = authentication_request
    
    def get_authentication_request(self):
        return self.__authentication_request
    def overall_score(self):
        return (self.__imsi_detach_indication + self.__location_update_request
                + self.__authentication_request)

#change to all capital
class GSM_MSG_MM_TYPE(enum.Enum):
    IMSI_Detach_Indication = "0x1"
    Location_Updating_Accept = "0x2"
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


class SCORE_BOARD(enum.Enum):
    Points_IMSI_Detach_Indication_TMSI = 10
    Points_IMSI_Detach_Indication_IMSI = -10
    Points_Identify_Request_IMSI = -5 #probably this is invalid. Identify req is always imsi.
    Points_Identify_Request_TIMSI = 5 #probably this is invalid. Identify req is always imsi.
    Points_Location_Updating_Request_IMSI = -10
    Points_Location_Updating_Request_TIMSI = 10 
    Points_Authentication_Request = 10
    Points_Authentication_Request_not_asking = -10 #check if it's asking (imsi catcher)
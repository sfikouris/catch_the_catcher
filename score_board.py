import enum

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
        self._freeze() # no new attributes after this point.

    def set_imsi_detach_indication(self, imsi_detach_indication):
        self.__imsi_detach_indication = imsi_detach_indication
    
    def get_imsi_detach_indication(self):
        return self.__imsi_detach_indication
    
    def set_location_update_request(self, location_update_request):
        self.__location_update_request = location_update_request
    
    def get_location_update_request(self):
        return self.__location_update_request

    def overall_score(self):
        return self.__imsi_detach_indication + self.__location_update_request

class GSM_MSG_MM_TYPE(enum.Enum):
    IMSI_Detach_Indication = "0x00000001"
    Identify_Request = "0x00000018"
    Identify_Response = "0x00000019"
    Location_Updating_Request = "0x00000008"
    Location_Updating_Accept = "0x00000002"
    Authentication_Request = "0x00000012"
    Authentication_Response = "0x00000014"
    MM_Information = "0x00000032"

class SCORE_BOARD(enum.Enum):
    Points_IMSI_Detach_Indication_TMSI = 10
    Points_IMSI_Detach_Indication_IMSI = -10
    Points_Identify_Request_IMSI = -5 #probably this is invalid. Identify req is always imsi.
    Points_Identify_Request_TIMSI = 5 #probably this is invalid. Identify req is always imsi.
    Points_Location_Updating_Request_IMSI = -10
    Points_Location_Updating_Request_TIMSI = 10 
    Points_Authentication_Request = 10
    Points_Authentication_Request_not_asking = -10 #check if it's asking (imsi catcher)
import enum

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

def handle_gsm_mm_packet(packet):
    if packet.msg_mm_type == GSM_MSG_MM_TYPE.IMSI_Detach_Indication.value:
        print("IMSI Detach Indication received")
        #print(packet.gsm_a.tmsi)
    elif packet.msg_mm_type == GSM_MSG_MM_TYPE.Identify_Request.value:
        print("Identify Request received")
    elif packet.msg_mm_type == GSM_MSG_MM_TYPE.Identify_Response.value:
        print("Identify Response received")
    elif packet.msg_mm_type == GSM_MSG_MM_TYPE.Location_Updating_Request.value:
        print("Location Updating Request received")
    elif packet.msg_mm_type == GSM_MSG_MM_TYPE.Location_Updating_Accept.value:
        print("Location Updating Accept received")        
    elif packet.msg_mm_type == GSM_MSG_MM_TYPE.Authentication_Request.value:
        print("Authentication Request received")    
    elif packet.msg_mm_type == GSM_MSG_MM_TYPE.Authentication_Response.value:
        print("Authentication Response received")
    elif packet.msg_mm_type == GSM_MSG_MM_TYPE.MM_Information.value:
        print("MM_Information received")
    else:
        print("Unknown mm type ", packet.msg_mm_type)    
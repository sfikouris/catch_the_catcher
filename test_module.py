import enum

class GSM_MSG_MM_TYPE(enum.Enum):
    IMSI_Detach_Indication = "0x00000001"
    Identify_Request = "0x00000018"
    Identify_Response = "0x00000019"
    Location_Updating_Request = "0x00000008"
    Location_Updating_Accept = "0x00000002"
    Authentication_Request = "0x00000012"
    Authentication_Response = "0x00000014"

def check_gsm_msg_mm_type(gsm_msg):
    if gsm_msg == GSM_MSG_MM_TYPE.IMSI_Detach_Indication.value:
        print("IMSI Detach Indication received")
    elif gsm_msg == GSM_MSG_MM_TYPE.Identify_Request.value:
        print("Identify Request received")
    elif gsm_msg == GSM_MSG_MM_TYPE.Identify_Response.value:
        print("Identify Response received")
    elif gsm_msg == GSM_MSG_MM_TYPE.Location_Updating_Request.value:
        print("Location Updating Request received")
    elif gsm_msg == GSM_MSG_MM_TYPE.Location_Updating_Accept.value:
        print("Location Updating Accept received")        
    elif gsm_msg == GSM_MSG_MM_TYPE.Authentication_Request.value:
        print("Authentication Request received")    
    elif gsm_msg == GSM_MSG_MM_TYPE.Authentication_Response.value:
        print("Authentication Response received")
    else:
        print("Unknown mm type ", gsm_msg)    
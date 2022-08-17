
import score_board

'''
Create a bitmask in each if else. eg 00000
imsi detach arrive 10000
imsi location update 10100

then check if the bitmask is 1 and then goes back to zero but with the bitmask not equal to 
11111, then something is wrong. follow the pattern of wireshark to fill the bitmask. 
'''
def handle_gsm_mm_packet(packet):
    int_value = int(packet.msg_mm_type,16)
    hex_value = hex(int_value)
    if hex_value == score_board.GSM_MSG_MM_TYPE.IMSI_Detach_Indication.value:
        print("IMSI Detach Indication received")
        if(hasattr(packet, 'gsm_a_tmsi')):
            print("TMSI", packet.gsm_a_tmsi)

    elif hex_value == score_board.GSM_MSG_MM_TYPE.Identify_Request.value:
        print("Identify Request received")
        if(hasattr(packet, 'gsm_a_tmsi')):
            print("TMSI", packet.gsm_a_tmsi)

    elif hex_value == score_board.GSM_MSG_MM_TYPE.Identify_Response.value:
        print("Identify Response received")
        if(hasattr(packet, 'gsm_a_tmsi')):
            print("TMSI", packet.gsm_a_tmsi)

    elif hex_value == score_board.GSM_MSG_MM_TYPE.Location_Updating_Request.value:
        print("Location Updating Request received")
        if(hasattr(packet, 'gsm_a_tmsi')):
            print("TMSI", packet.gsm_a_tmsi)

    elif hex_value == score_board.GSM_MSG_MM_TYPE.Location_Updating_Accept.value:
        print("Location Updating Accept received")        
        if(hasattr(packet, 'gsm_a_tmsi')):
            print("TMSI", packet.gsm_a_tmsi)

    elif hex_value == score_board.GSM_MSG_MM_TYPE.Authentication_Request.value:
        print("Authentication Request received")    
        if(hasattr(packet, 'gsm_a_tmsi')):
            print("TMSI", packet.gsm_a_tmsi)

    elif hex_value == score_board.GSM_MSG_MM_TYPE.Authentication_Response.value:
        print("Authentication Response received")
        if(hasattr(packet, 'gsm_a_tmsi')):
            print("TMSI", packet.gsm_a_tmsi)

    elif hex_value == score_board.GSM_MSG_MM_TYPE.MM_Information.value:
        print("MM_Information received")
        if(hasattr(packet, 'gsm_a_tmsi')):
            print("TMSI", packet.gsm_a_tmsi)

    else:
        print("Unknown mm type ", packet.msg_mm_type)    

score = score_board.score_board()
score.set_imsi_detach_indication(10)
score.set_location_update_request(20)
score.set_authentication_request(30)
print(score.overall_score())
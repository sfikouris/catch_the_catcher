
import header_file

'''
Create a bitmask in each if else. eg 00000
imsi detach arrive 10000
imsi location update 10100

then check if the bitmask is 1 and then goes back to zero but with the bitmask not equal to 
11111, then something is wrong. follow the pattern of wireshark to fill the bitmask. 


ERRORS: POINT IS NOT GOING TO WORK. NEED TO BE OUTSIDE OF INIT
ON RETURN CHECK FOR CURRENT VALUE and see what u will do .
'''
def handle_gsm_mm_packet(packet):
    gsm_attachment_procedure_bits = header_file.pattern_check()
    score = header_file.score_board()
    int_value_mm = 0
    int_value_gmm = 0
    hex_value_mm = 0
    hex_value_gmm = 0
    
    if(hasattr(packet, 'msg_mm_type')):
        int_value_mm = int(packet.msg_mm_type, 16)
        hex_value_mm = hex(int_value_mm)

    elif(hasattr(packet, 'msg_gmm_type')):
        int_value_gmm = int(packet.msg_gmm_type)
        hex_value_gmm = hex(int_value_gmm)

    if hex_value_mm == header_file.GSM_MSG_MM_TYPE.IMSI_Detach_Indication.value:
        print("IMSI Detach Indication received")
        if(hasattr(packet, 'gsm_a_tmsi')):
            print("\t TMSI :", packet.gsm_a_tmsi)

    elif hex_value_mm == header_file.GSM_MSG_MM_TYPE.Identify_Request.value:
        print("Identify Request received")
        if(hasattr(packet, 'gsm_a_tmsi')):
            print("\t TMSI :", packet.gsm_a_tmsi)
        gsm_attachment_procedure_bits.set_checker(1)
        #probably need to check about IMSI and IMEI separate 

    elif hex_value_mm == header_file.GSM_MSG_MM_TYPE.Identify_Response.value:
        print("Identify Response received")
        if(hasattr(packet, 'gsm_a_tmsi')):
            print("\t TMSI :", packet.gsm_a_tmsi)

    elif hex_value_mm == header_file.GSM_MSG_MM_TYPE.Location_Updating_Request.value:
        print("Location Updating Request received")
        if(hasattr(packet, 'gsm_a_tmsi')):
            print("\t TMSI :", packet.gsm_a_tmsi)
    
        checker = gsm_attachment_procedure_bits.get_checker()
        if(checker == 0):
            gsm_attachment_procedure_bits.set_checker(0)
        else:
            current_point = score.get_overall_score()
            retrun_flag = not gsm_attachment_procedure_bits.check_bits()
            gsm_attachment_procedure_bits.clear_checker()
            score.clear_points()
            gsm_attachment_procedure_bits.set_checker(0)
            if(retrun_flag):
                return current_point



    elif hex_value_mm == header_file.GSM_MSG_MM_TYPE.Location_Updating_Accept.value:
        print("Location Updating Accept received")        
        if(hasattr(packet, 'gsm_a_tmsi')):
            print("\t TMSI :", packet.gsm_a_tmsi)

    elif hex_value_mm == header_file.GSM_MSG_MM_TYPE.Authentication_Request.value:
        print("Authentication Request received")    
        if(hasattr(packet, 'gsm_a_tmsi')):
            print("\t TMSI :", packet.gsm_a_tmsi)
        gsm_attachment_procedure_bits.set_checker(2)

    elif hex_value_mm == header_file.GSM_MSG_MM_TYPE.Authentication_Response.value:
        print("Authentication Response received")
        if(hasattr(packet, 'gsm_a_tmsi')):
            print("\t TMSI :", packet.gsm_a_tmsi)

    elif hex_value_mm == header_file.GSM_MSG_MM_TYPE.MM_Information.value:
        print("MM_Information received")
        if(hasattr(packet, 'gsm_a_tmsi')):
            print("\t TMSI :", packet.gsm_a_tmsi)

    elif hex_value_gmm == header_file.GSM_MSG_GMM_TYPE.ATTACH_REQUEST.value:
        print("Attach_Request received")
        if(hasattr(packet, 'gsm_a_tmsi')):
            print("\t TMSI :", packet.gsm_a_tmsi)   

    elif hex_value_gmm == header_file.GSM_MSG_GMM_TYPE.ATTACH_COMPLETE.value:
        print("Attach_Complete received")
        if(hasattr(packet, 'gsm_a_tmsi')):
            print("\t TMSI :", packet.gsm_a_tmsi)   

    elif hex_value_gmm == header_file.GSM_MSG_GMM_TYPE.ATTACH_ACCEPT.value:
        print("Attach_Accept received")
        if(hasattr(packet, 'gsm_a_tmsi')):
            print("\t TMSI :", packet.gsm_a_tmsi)   
        gsm_attachment_procedure_bits.set_checker(4)
        #if completed then foul score.

    elif hex_value_gmm == header_file.GSM_MSG_GMM_TYPE.DETACH_REQUEST.value:
        print("Detach_Request received")
        if(hasattr(packet, 'gsm_a_tmsi')):
            print("\t TMSI :", packet.gsm_a_tmsi)   

    elif hex_value_gmm == header_file.GSM_MSG_GMM_TYPE.AUTHENTICATION_AND_CIPHERING_RESPONSE.value:
        print("Authentication_And_Ciphering_Response received")
        if(hasattr(packet, 'gsm_a_tmsi')):
            print("\t TMSI :", packet.gsm_a_tmsi)   

    elif hex_value_gmm == header_file.GSM_MSG_GMM_TYPE.AUTHENTICATION_AND_CIPHERING_REQUEST.value:
        print("Authentication_And_Ciphering_Request received")
        if(hasattr(packet, 'gsm_a_tmsi')):
            print("\t TMSI :", packet.gsm_a_tmsi)
        gsm_attachment_procedure_bits.set_checker(3)  

    elif hex_value_gmm == header_file.GSM_MSG_GMM_TYPE.GMM_INFROMATION.value:
        print("GMM_Information received")
        if(hasattr(packet, 'gsm_a_tmsi')):
            print("\t TMSI :", packet.gsm_a_tmsi)
    #On an IMSI CATCHER a release msg should be send. There I must check the bit_checker to see if it kick me out before the completment of the attachment.
    else:
        if(hasattr(packet, 'msg_mm_type')):
            print("Unknown mm type ", packet.msg_mm_type)
        elif hasattr(packet, 'msg_gmm_type'):
            print("Unknown gmm type ", packet.msg_gmm_type)
        else:
            print("Unknown msg type")


score = header_file.score_board()
score.set_imsi_detach_indication(10)
score.set_location_update_request(20)
score.set_authentication_request(30)
print(score.get_overall_score())
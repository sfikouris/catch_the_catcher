
import header_file
import logging
import sys

logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
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
        logging.debug("IMSI Detach Indication received")
        score.clear_points()
        gsm_attachment_procedure_bits.clear_checker()
        if(hasattr(packet, 'gsm_a_tmsi')):
            logging.debug("\t TMSI : %s", packet.gsm_a_tmsi)

    elif hex_value_mm == header_file.GSM_MSG_MM_TYPE.Identify_Request.value:
        logging.debug("Identify Request received")
        gsm_attachment_procedure_bits.set_checker(1)
        #probably need to check about IMSI and IMEI separate 

    elif hex_value_mm == header_file.GSM_MSG_MM_TYPE.Identify_Response.value:
        logging.debug("Identify Response received")
        if(hasattr(packet, 'gsm_a_tmsi')):
            logging.debug("\t TMSI : %s", packet.gsm_a_tmsi)
        elif(hasattr(packet, 'e212_imsi')):
            logging.debug("\t IMSI Available : %s", packet.e212_imsi) #check if field imsi is correct

    elif hex_value_mm == header_file.GSM_MSG_MM_TYPE.Location_Updating_Request.value:
        logging.debug("Location Updating Request received")

        retrun_flag = False
        checker = gsm_attachment_procedure_bits.get_checker()
        if(checker == 0):
            gsm_attachment_procedure_bits.set_checker(0)
        else:
            current_point = score.get_overall_score()
            retrun_flag = not gsm_attachment_procedure_bits.check_bits()
            gsm_attachment_procedure_bits.clear_checker()
            score.clear_points()
            gsm_attachment_procedure_bits.set_checker(0)
            logging.debug("MAX RETURN POINTS : %d", current_point)
            #no need to return pattern bits because at attachment complete I will do it.
        if(hasattr(packet, 'gsm_a_tmsi')):
            logging.debug("\t TMSI Available : %s", packet.gsm_a_tmsi)
            score.set_location_update_request(header_file.SCORE_BOARD.Points_Location_Updating_Request_TMSI)
        elif(hasattr(packet, 'e212_imsi')):
            logging.debug("\t IMSI Available : %s", packet.e212_imsi) #check if field imsi is correct
            score.set_location_update_request(header_file.SCORE_BOARD.Points_Location_Updating_Request_IMSI)

        if(retrun_flag):
            #return if pattern bits are not full.
            logging.debug("RETURN POINTS : %d", current_point)
            return current_point

    elif hex_value_mm == header_file.GSM_MSG_MM_TYPE.Location_Updating_Accept.value:
        logging.debug("Location Updating Accept received")        
        if(hasattr(packet, 'gsm_a_tmsi')):
            logging.debug("\t TMSI : %s", packet.gsm_a_tmsi)
        score.set_location_accept(header_file.SCORE_BOARD.Points_Location_Accept.value)

    elif hex_value_mm == header_file.GSM_MSG_MM_TYPE.Location_Updating_Reject.value:
        logging.debug("Location Updating Reject")
        score.set_location_accept(header_file.SCORE_BOARD.Points_Location_Reject.value)
        return score.get_overall_score()

    elif hex_value_mm == header_file.GSM_MSG_MM_TYPE.Authentication_Request.value:
        logging.debug("Authentication Request received")    
        if(hasattr(packet, 'gsm_a_tmsi')):
            logging.debug("\t TMSI : %s", packet.gsm_a_tmsi)
        gsm_attachment_procedure_bits.set_checker(2)
        score.set_authentication_request(header_file.SCORE_BOARD.Points_Authentication_Request.value)

    elif hex_value_mm == header_file.GSM_MSG_MM_TYPE.Authentication_Response.value:
        logging.debug("Authentication Response received")
        if(hasattr(packet, 'gsm_a_tmsi')):
            logging.debug("\t TMSI : %s", packet.gsm_a_tmsi)

    elif hex_value_mm == header_file.GSM_MSG_MM_TYPE.MM_Information.value:
        logging.debug("MM_Information received")
        if(hasattr(packet, 'gsm_a_tmsi')):
            logging.debug("\t TMSI : %s", packet.gsm_a_tmsi)

    elif hex_value_gmm == header_file.GSM_MSG_GMM_TYPE.ATTACH_REQUEST.value:
        logging.debug("Attach_Request received")
        if(hasattr(packet, 'gsm_a_tmsi')):
            logging.debug("\t TMSI : %s", packet.gsm_a_tmsi)   

    elif hex_value_gmm == header_file.GSM_MSG_GMM_TYPE.ATTACH_COMPLETE.value:
        logging.debug("Attach_Complete received")
        score.set_attach_complete(header_file.SCORE_BOARD.Points_Attach_Complete.value)        

    elif hex_value_gmm == header_file.GSM_MSG_GMM_TYPE.ATTACH_ACCEPT.value:
        logging.debug("Attach_Accept received")
        if(hasattr(packet, 'gsm_a_tmsi')):
            logging.debug("\t TMSI : %s", packet.gsm_a_tmsi)   
            gsm_attachment_procedure_bits.set_checker(4)
            score.set_attach_accept(header_file.SCORE_BOARD.Points_Attach_Accept.value)
            if gsm_attachment_procedure_bits.check_bits():
                score.set_pattern_points(header_file.SCORE_BOARD.Points_GSM_Pattern.value)
            return score.get_overall_score()       

        #if completed then foul score.

    elif hex_value_gmm == header_file.GSM_MSG_GMM_TYPE.DETACH_REQUEST.value:
        logging.debug("Detach_Request received")
        if(hasattr(packet, 'gsm_a_tmsi')):
            logging.debug("\t TMSI : %s", packet.gsm_a_tmsi)   
            score.clear_points()
            gsm_attachment_procedure_bits.clear_checker()

    elif hex_value_gmm == header_file.GSM_MSG_GMM_TYPE.AUTHENTICATION_AND_CIPHERING_RESPONSE.value:
        logging.debug("Authentication_And_Ciphering_Response received")

    elif hex_value_gmm == header_file.GSM_MSG_GMM_TYPE.AUTHENTICATION_AND_CIPHERING_REQUEST.value:
        logging.debug("Authentication_And_Ciphering_Request received")
        score.set_auth_and_cipher(header_file.SCORE_BOARD.Points_Authentication_And_Ciphering_Request.value)
        gsm_attachment_procedure_bits.set_checker(3)  

    elif hex_value_gmm == header_file.GSM_MSG_GMM_TYPE.GMM_INFROMATION.value:
        logging.debug("GMM_Information received")
        if(hasattr(packet, 'gsm_a_tmsi')):
            logging.debug("\t TMSI : %s", packet.gsm_a_tmsi)
    #On an IMSI CATCHER a release msg should be send. There I must check the bit_checker to see if it kick me out before the completment of the attachment.
    else:
        if(hasattr(packet, 'msg_mm_type')):
            logging.debug("Unknown mm type %s", packet.msg_mm_type)
        elif hasattr(packet, 'msg_gmm_type'):
            logging.debug("Unknown gmm type %s", packet.msg_gmm_type)
        else:
            logging.debug("Unknown msg type")
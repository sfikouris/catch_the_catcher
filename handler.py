
from cmath import nan
import header_file
import logging
import sys

logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)


######################
# HANDLE MM TYPE MSG #
######################

def handle_imsi_detach_indication(packet, score: header_file.score_board, gsm_attachment_procedure_bits: header_file.pattern_check,
                                    general_info: header_file.general_info):
    logging.debug("IMSI Detach Indication")
    score.clear_points()
    gsm_attachment_procedure_bits.clear_checker()
    if(hasattr(packet, 'gsm_a_tmsi')):
        logging.debug("\t TMSI : %s", packet.gsm_a_tmsi)

def handle_identify_request(packet, score: header_file.score_board, gsm_attachment_procedure_bits: header_file.pattern_check,
                            general_info: header_file.general_info):
        logging.debug("Identify Request")
        gsm_attachment_procedure_bits.set_checker(1)
        #probably need to check about IMSI and IMEI separate 

def handle_identify_response(packet, score: header_file.score_board, gsm_attachment_procedure_bits: header_file.pattern_check,
                                general_info: header_file.general_info):
    logging.debug("Identify Response")
    if(hasattr(packet, 'gsm_a_tmsi')):
        logging.debug("\t TMSI : %s", packet.gsm_a_tmsi)
    elif(hasattr(packet, 'e212_imsi')):
        logging.debug("\t IMSI Available : %s", packet.e212_imsi)

def handle_location_update_request(packet, score: header_file.score_board, gsm_attachment_procedure_bits: header_file.pattern_check,
                                    general_info: header_file.general_info):
    logging.debug("Location Updating Request")
    general_info.set_location_update_req_last_seen = True
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
        score.set_location_update_request(header_file.SCORE_BOARD.Points_Location_Updating_Request_TMSI.value)
    elif(hasattr(packet, 'e212_imsi')):
        logging.debug("\t IMSI Available : %s", packet.e212_imsi) #check if field imsi is correct
        score.set_location_update_request(header_file.SCORE_BOARD.Points_Location_Updating_Request_IMSI.value)

    if(retrun_flag):
        #return if pattern bits are not full.
        logging.debug("RETURN POINTS : %d", current_point)
        return current_point

def handle_location_update_accept(packet, score: header_file.score_board, gsm_attachment_procedure_bits: header_file.pattern_check,
                                    general_info: header_file.general_info):
    logging.debug("Location Updating Accept")        
    general_info.set_location_update_req_last_seen = False
    if(hasattr(packet, 'gsm_a_tmsi')):
        logging.debug("\t TMSI : %s", packet.gsm_a_tmsi)
    score.set_location_accept(header_file.SCORE_BOARD.Points_Location_Accept.value)

def handle_location_update_reject(packet, score: header_file.score_board, gsm_attachment_procedure_bits: header_file.pattern_check,
                                    general_info: header_file.general_info):
    logging.debug("Location Updating Reject")
    general_info.set_location_update_req_last_seen = False
    score.set_location_accept(header_file.SCORE_BOARD.Points_Location_Reject.value)
    return score.get_overall_score()

def handle_authentication_request(packet, score: header_file.score_board, gsm_attachment_procedure_bits: header_file.pattern_check,
                                    general_info: header_file.general_info):
    logging.debug("Authentication Request")    
    if(hasattr(packet, 'gsm_a_tmsi')):
        logging.debug("\t TMSI : %s", packet.gsm_a_tmsi)
    gsm_attachment_procedure_bits.set_checker(2)
    score.set_authentication_request(header_file.SCORE_BOARD.Points_Authentication_Request.value)

def handle_authetication_response(packet, score: header_file.score_board, gsm_attachment_procedure_bits: header_file.pattern_check,
                                    general_info: header_file.general_info):
    logging.debug("Authentication Response")
    if(hasattr(packet, 'gsm_a_tmsi')):
        logging.debug("\t TMSI : %s", packet.gsm_a_tmsi)

def handle_mm_information(packet, score: header_file.score_board, gsm_attachment_procedure_bits: header_file.pattern_check,
                            general_info: header_file.general_info):
    logging.debug("MM_Information")
    if(hasattr(packet, 'gsm_a_tmsi')):
        logging.debug("\t TMSI : %s", packet.gsm_a_tmsi)


dispatch_mm_type = {
    header_file.GSM_MSG_MM_TYPE.IMSI_Detach_Indication.value: handle_imsi_detach_indication,
    header_file.GSM_MSG_MM_TYPE.Identify_Request.value: handle_identify_request,
    header_file.GSM_MSG_MM_TYPE.Identify_Response.value: handle_identify_response,
    header_file.GSM_MSG_MM_TYPE.Location_Updating_Request.value: handle_location_update_request,
    header_file.GSM_MSG_MM_TYPE.Location_Updating_Accept.value: handle_location_update_accept,
    header_file.GSM_MSG_MM_TYPE.Location_Updating_Reject.value: handle_location_update_reject,
    header_file.GSM_MSG_MM_TYPE.Authentication_Request.value: handle_authentication_request,
    header_file.GSM_MSG_MM_TYPE.Authentication_Response.value: handle_authetication_response,
    header_file.GSM_MSG_MM_TYPE.MM_Information.value: handle_mm_information
}

#######################
# HANDLE GMM TYPE MSG #
#######################

def handle_attach_request(packet, score: header_file.score_board, gsm_attachment_procedure_bits: header_file.pattern_check):
    logging.debug("Attach_Request")
    if(hasattr(packet, 'gsm_a_tmsi')):
        logging.debug("\t TMSI : %s", packet.gsm_a_tmsi)   

def handle_attach_complete(packet, score: header_file.score_board, gsm_attachment_procedure_bits: header_file.pattern_check):
    logging.debug("Attach_Complete")
    score.set_attach_complete(header_file.SCORE_BOARD.Points_Attach_Complete.value)    

def handle_attach_accept(packet, score: header_file.score_board, gsm_attachment_procedure_bits: header_file.pattern_check):
    logging.debug("Attach_Accept")
    if(hasattr(packet, 'gsm_a_tmsi')):
        logging.debug("\t TMSI : %s", packet.gsm_a_tmsi)   
        gsm_attachment_procedure_bits.set_checker(4)
        score.set_attach_accept(header_file.SCORE_BOARD.Points_Attach_Accept.value)
        if gsm_attachment_procedure_bits.check_bits():
            score.set_pattern_points(header_file.SCORE_BOARD.Points_GSM_Pattern.value)
        return score.get_overall_score()       
    #if completed then foul score.

def handle_detach_request(packet, score: header_file.score_board, gsm_attachment_procedure_bits: header_file.pattern_check):
    logging.debug("Detach_Request")
    if(hasattr(packet, 'gsm_a_tmsi')):
        logging.debug("\t TMSI : %s", packet.gsm_a_tmsi)   
        score.clear_points()
        gsm_attachment_procedure_bits.clear_checker()

def handle_auth_and_ciphering_response(packet, score: header_file.score_board, gsm_attachment_procedure_bits: header_file.pattern_check):
    logging.debug("Authentication_And_Ciphering_Response")

def handle_auth_and_ciphering_request(packet, score: header_file.score_board, gsm_attachment_procedure_bits: header_file.pattern_check):
    logging.debug("Authentication_And_Ciphering_Request")
    score.set_auth_and_cipher(header_file.SCORE_BOARD.Points_Authentication_And_Ciphering_Request.value)
    gsm_attachment_procedure_bits.set_checker(3)  

def handle_gmm_information(packet, score: header_file.score_board, gsm_attachment_procedure_bits: header_file.pattern_check):
    logging.debug("GMM_Information")
    if(hasattr(packet, 'gsm_a_tmsi')):
        logging.debug("\t TMSI : %s", packet.gsm_a_tmsi)

dispatch_gmm_type = {
    header_file.GSM_MSG_GMM_TYPE.ATTACH_REQUEST.value: handle_attach_request,
    header_file.GSM_MSG_GMM_TYPE.ATTACH_COMPLETE.value: handle_attach_complete,
    header_file.GSM_MSG_GMM_TYPE.ATTACH_ACCEPT.value: handle_attach_accept,
    header_file.GSM_MSG_GMM_TYPE.DETACH_REQUEST.value: handle_detach_request,
    header_file.GSM_MSG_GMM_TYPE.AUTHENTICATION_AND_CIPHERING_RESPONSE.value: handle_auth_and_ciphering_response,
    header_file.GSM_MSG_GMM_TYPE.AUTHENTICATION_AND_CIPHERING_REQUEST.value: handle_auth_and_ciphering_request,
    header_file.GSM_MSG_GMM_TYPE.GMM_INFROMATION.value: handle_gmm_information
}

#######################
# HANDLE RR TYPE MSG #
#######################

def handle_system_information_type_3(packet, general_info: header_file.general_info, index):
    logging.debug("System_Information_Type 3")
    if(general_info.get_location_update_req_last_seen == nan):
        general_info.set_sip3_last_seen(index)
        general_info.set_cell_identity(packet.gsm_a_bssmap_cell_ci)

def handle_known_rr_msg(packet, general_info: header_file.general_info, index):
    int_value_rr = int(packet.msg_rr_type, 16)
    hex_value_rr = hex(int_value_rr)
    logging.debug(header_file.GSM_MSG_RR_TYPE(hex_value_rr).name)
    

dispatch_rr_type = {
    header_file.GSM_MSG_RR_TYPE.System_Information_Type_3.value: handle_system_information_type_3,
    header_file.GSM_MSG_RR_TYPE.System_Information_Type_13.value: handle_known_rr_msg,
    header_file.GSM_MSG_RR_TYPE.System_Information_Type_5ter.value: handle_known_rr_msg,
    header_file.GSM_MSG_RR_TYPE.System_Information_Type_2quater.value: handle_known_rr_msg,
    header_file.GSM_MSG_RR_TYPE.Channel_Release.value: handle_known_rr_msg,
    header_file.GSM_MSG_RR_TYPE.Measurement_Report.value: handle_known_rr_msg,
    header_file.GSM_MSG_RR_TYPE.Classmark_Change.value: handle_known_rr_msg,
    header_file.GSM_MSG_RR_TYPE.System_Information_Type_1.value: handle_known_rr_msg,
    header_file.GSM_MSG_RR_TYPE.System_Information_Type_2.value: handle_known_rr_msg,
    header_file.GSM_MSG_RR_TYPE.System_Information_Type_4.value: handle_known_rr_msg,
    header_file.GSM_MSG_RR_TYPE.System_Information_Type_5.value: handle_known_rr_msg,
    header_file.GSM_MSG_RR_TYPE.System_Information_Type_6.value: handle_known_rr_msg,
    header_file.GSM_MSG_RR_TYPE.Paging_Request_Type_1.value: handle_known_rr_msg,
    header_file.GSM_MSG_RR_TYPE.Paging_Request_Type_2.value: handle_known_rr_msg,
    header_file.GSM_MSG_RR_TYPE.GPRS_Suspension_Request.value: handle_known_rr_msg,
    header_file.GSM_MSG_RR_TYPE.Ciphering_Mode_Command.value: handle_known_rr_msg,
    header_file.GSM_MSG_RR_TYPE.Immediate_Assignment.value: handle_known_rr_msg
}
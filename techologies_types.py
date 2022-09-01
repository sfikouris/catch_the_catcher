import header_file
import logging
import sys

logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)

class techology(object):
    #constructor
    def __init__(self, score: header_file.score_board, gsm_attachment_procedure_bits: header_file.pattern_check, 
                    general_info:  header_file.general_info, packet=None):
        self.packet = packet
        self.score = score
        self.gsm_attachment_procedure_bits = gsm_attachment_procedure_bits
        self.general_info = general_info
        self.index = None
        self.dispatch_mm_type = {
            header_file.MM_TYPE_MSG.IMSI_Detach_Indication.value: self.handle_imsi_detach_indication,
            header_file.MM_TYPE_MSG.Identify_Request.value: self.handle_identify_request,
            header_file.MM_TYPE_MSG.Identify_Response.value: self.handle_identify_response,
            header_file.MM_TYPE_MSG.Location_Updating_Request.value: self.handle_location_update_request,
            header_file.MM_TYPE_MSG.Location_Updating_Accept.value: self.handle_location_update_accept,
            header_file.MM_TYPE_MSG.Location_Updating_Reject.value: self.handle_location_update_reject,
            header_file.MM_TYPE_MSG.Authentication_Request.value: self.handle_authentication_request,
            header_file.MM_TYPE_MSG.Authentication_Response.value: self.handle_authetication_response,
            header_file.MM_TYPE_MSG.MM_Information.value: self.handle_mm_information
        }

        self.dispatch_gmm_type = {
            header_file.GMM_TYPE_MSG.Attach_Request.value: self.handle_attach_request,
            header_file.GMM_TYPE_MSG.Attach_Complete.value: self.handle_attach_complete,
            header_file.GMM_TYPE_MSG.Attach_Accept.value: self.handle_attach_accept,
            header_file.GMM_TYPE_MSG.Detach_Request.value: self.handle_detach_request,
            header_file.GMM_TYPE_MSG.Authentication_And_Ciphering_Response.value: self.handle_auth_and_ciphering_response,
            header_file.GMM_TYPE_MSG.Authentication_And_Ciphering_Request.value: self.handle_auth_and_ciphering_request,
            header_file.GMM_TYPE_MSG.GMM_Information.value: self.handle_gmm_information,
            header_file.GMM_TYPE_MSG.Identity_Request.value: self.handle_identity_request,
            header_file.GMM_TYPE_MSG.Identity_Response.value: self.handle_identity_response,
            header_file.GMM_TYPE_MSG.Routing_Area_Update_Accept.value: self.handle_routing_area_update_accept,
            header_file.GMM_TYPE_MSG.Routing_Area_Update_Complete.value: self.handle_routing_area_update_complete
        }

        self.dispatch_rr_type = {
            header_file.RR_TYPE_MSG.System_Information_Type_3.value: self.handle_system_information_type_3,
            header_file.RR_TYPE_MSG.System_Information_Type_13.value: self.handle_known_rr_msg,
            header_file.RR_TYPE_MSG.System_Information_Type_5ter.value: self.handle_known_rr_msg,
            header_file.RR_TYPE_MSG.System_Information_Type_2quater.value: self.handle_known_rr_msg,
            header_file.RR_TYPE_MSG.Channel_Release.value: self.handle_known_rr_msg,
            header_file.RR_TYPE_MSG.Measurement_Report.value: self.handle_known_rr_msg,
            header_file.RR_TYPE_MSG.Classmark_Change.value: self.handle_known_rr_msg,
            header_file.RR_TYPE_MSG.System_Information_Type_1.value: self.handle_known_rr_msg,
            header_file.RR_TYPE_MSG.System_Information_Type_2.value: self.handle_known_rr_msg,
            header_file.RR_TYPE_MSG.System_Information_Type_4.value: self.handle_known_rr_msg,
            header_file.RR_TYPE_MSG.System_Information_Type_5.value: self.handle_known_rr_msg,
            header_file.RR_TYPE_MSG.System_Information_Type_6.value: self.handle_known_rr_msg,
            header_file.RR_TYPE_MSG.Paging_Request_Type_1.value: self.handle_known_rr_msg,
            header_file.RR_TYPE_MSG.Paging_Request_Type_2.value: self.handle_known_rr_msg,
            header_file.RR_TYPE_MSG.GPRS_Suspension_Request.value: self.handle_known_rr_msg,
            header_file.RR_TYPE_MSG.Ciphering_Mode_Command.value: self.handle_known_rr_msg,
            header_file.RR_TYPE_MSG.Immediate_Assignment.value: self.handle_known_rr_msg,
            header_file.RR_TYPE_MSG.Ciphering_Mode_Complete.value: self.handle_known_rr_msg
        }

    def set_index(self, new_index):
        self.index = new_index

    def handle_packet(self):
        raise NotImplementedError()

    def set_packet(self, new_packet):
        self.packet = new_packet

    ######################
    # HANDLE MM TYPE MSG #
    ######################

    def handle_imsi_detach_indication(self):
        logging.debug("IMSI Detach Indication")

    def handle_identify_request(self):
        logging.debug("Identify Request")

    def handle_identify_response(self):
        logging.debug("Identify Response")

    def handle_location_update_request(self):
        logging.debug("Location Updating Request")

    def handle_location_update_accept(self):
        logging.debug("Location Updating Accept")        

    def handle_location_update_reject(self):
        logging.debug("Location Updating Reject")

    def handle_authentication_request(self):
        logging.debug("Authentication Request")    

    def handle_authetication_response(self):
        logging.debug("Authentication Response")

    def handle_mm_information(self):
        logging.debug("MM_Information")

    #######################
    # HANDLE GMM TYPE MSG #
    #######################

    def handle_attach_request(self):
        logging.debug("Attach_Request")

    def handle_attach_complete(self):
        logging.debug("Attach_Complete")

    def handle_attach_accept(self):
        logging.debug("Attach_Accept")

    def handle_detach_request(self):
        logging.debug("Detach_Request")

    def handle_auth_and_ciphering_response(self):
        logging.debug("Authentication_And_Ciphering_Response")

    def handle_auth_and_ciphering_request(self):
        logging.debug("Authentication_And_Ciphering_Request")

    def handle_gmm_information(self):
        logging.debug("GMM_Information")

    def handle_identity_request(self):
        logging.debug("Identity_Request")

    def handle_identity_response(self):
        logging.debug("Identity_Response")

    def handle_routing_area_update_accept(self):
        logging.debug("Routing Area Update Accept")

    def handle_routing_area_update_complete(self):
        logging.debug("Routing Area Update Complete")

    #######################
    # HANDLE RR TYPE MSG #
    #######################

    def handle_system_information_type_3(self):
        logging.debug("System_Information_Type 3")

    def handle_known_rr_msg(self):
        int_value_rr = int(self.packet.msg_rr_type, 16)
        hex_value_rr = hex(int_value_rr)
        logging.debug(header_file.RR_TYPE_MSG(hex_value_rr).name)
    
class gsm(techology):
        #constructor
    def __init__(self, score: header_file.score_board, gsm_attachment_procedure_bits: header_file.pattern_check, 
                    general_info:  header_file.general_info, packet=None):
        super(gsm, self).__init__(score, gsm_attachment_procedure_bits, general_info, packet)

    ######################
    # HANDLE MM TYPE MSG #
    ######################

    def handle_imsi_detach_indication(self):
        logging.debug("IMSI Detach Indication")
        self.score.clear_points()
        self.gsm_attachment_procedure_bits.clear_checker()
        if(hasattr(self.packet, 'gsm_a_tmsi')):
            logging.debug("\t TMSI : %s", self.packet.gsm_a_tmsi)
    
    def handle_identify_request(self):
        logging.debug("Identify Request")
        self.gsm_attachment_procedure_bits.set_checker(1)
        #probably need to check about IMSI and IMEI separate 

    def handle_location_update_request(self):
        logging.debug("Location Updating Request")
        self.general_info.set_location_upbase_classdate_req_last_seen = True
        retrun_flag = False
        checker = self.gsm_attachment_procedure_bits.get_checker()
        if(checker == 0):
            self.gsm_attachment_procedure_bits.set_checker(0)
        else:
            current_point = self.score.get_overall_score()
            retrun_flag = not self.gsm_attachment_procedure_bits.check_bits()
            self.gsm_attachment_procedure_bits.set_checker(0)
            logging.debug("MAX RETURN POINTS : %d", current_point)
            #no need to return pattern bits because at attachment complete I will do it.
        if(hasattr(self.packet, 'gsm_a_tmsi')):
            logging.debug("\t TMSI Available : %s", self.packet.gsm_a_tmsi)
            self.score.set_location_update_request(header_file.SCORE_BOARD.Points_Location_Updating_Request_TMSI.value)
            self.general_info.__tmsi_mm = self.packet.gsm_a_tmsi
        elif(hasattr(self.packet, 'e212_imsi')):
            logging.debug("\t IMSI Available : %s", self.packet.e212_imsi) #check if field imsi is correct
            self.score.set_location_update_request(header_file.SCORE_BOARD.Points_Location_Updating_Request_IMSI.value)
            self.general_info.__imsi = self.packet.e212_imsi

        if(retrun_flag):
            #return if pattern bits are not full.
            logging.debug("RETURN POINTS : %d", current_point)
            return current_point

    def handle_location_update_accept(self):
        #add and maybe return some points here.
        logging.debug("Location Updating Accept")        
        self.general_info.set_location_update_req_last_seen = False
        if(hasattr(self.packet, 'gsm_a_tmsi')):
            logging.debug("\t TMSI : %s", self.packet.gsm_a_tmsi)
        self.score.set_location_accept(header_file.SCORE_BOARD.Points_Location_Accept.value)

    def handle_location_update_reject(self):
        logging.debug("Location Updating Reject")
        self.general_info.set_location_update_req_last_seen = False
        self.score.set_location_accept(header_file.SCORE_BOARD.Points_Location_Reject.value)
        return self.score.get_overall_score()

    def handle_authentication_request(self):
        logging.debug("Authentication Request")    
        if(hasattr(self.packet, 'gsm_a_tmsi')):
            logging.debug("\t TMSI : %s", self.packet.gsm_a_tmsi)
        self.gsm_attachment_procedure_bits.set_checker(2)
        self.score.set_authentication_request(header_file.SCORE_BOARD.Points_Authentication_Request.value)

    #######################
    # HANDLE GMM TYPE MSG #
    #######################

    def handle_attach_request(self):
        logging.debug("Attach_Request")
        if(hasattr(self.packet, 'gsm_a_tmsi')):
            logging.debug("\t TMSI : %s", self.packet.gsm_a_tmsi)   

    def handle_attach_complete(self):
        logging.debug("Attach_Complete")
        self.score.set_attach_complete(header_file.SCORE_BOARD.Points_Attach_Complete.value)    

    def handle_attach_accept(self):
        logging.debug("Attach_Accept")
        if(hasattr(self.packet, 'gsm_a_tmsi')):
            logging.debug("\t TMSI : %s", self.packet.gsm_a_tmsi)   
            self.gsm_attachment_procedure_bits.set_checker(4)
            self.score.set_attach_accept(header_file.SCORE_BOARD.Points_Attach_Accept.value)
            if self.gsm_attachment_procedure_bits.check_bits():
                self.score.set_pattern_points(header_file.SCORE_BOARD.Points_GSM_Pattern.value)
            return self.score.get_overall_score()       

    def handle_detach_request(self):
        logging.debug("Detach_Request")
        if(hasattr(self.packet, 'gsm_a_tmsi')):
            logging.debug("\t TMSI : %s", self.packet.gsm_a_tmsi)   
            self.score.clear_points()
            self.gsm_attachment_procedure_bits.clear_checker()

    def handle_auth_and_ciphering_request(self):
        logging.debug("Authentication_And_Ciphering_Request")
        self.score.set_auth_and_cipher(header_file.SCORE_BOARD.Points_Authentication_And_Ciphering_Request.value)
        self.gsm_attachment_procedure_bits.set_checker(3)  

    #######################
    # HANDLE RR TYPE MSG #
    #######################

    def handle_system_information_type_3(self):
        logging.debug("System_Information_Type 3")
        if(self.general_info.get_location_update_req_last_seen == None):
            self.general_info.set_sip3_last_seen(self.index)
            self.general_info.set_cell_identity(self.packet.gsm_a_bssmap_cell_ci)

    def handle_packet(self):
        if(hasattr(self.packet, 'msg_mm_type')):
            int_value_mm = int(self.packet.msg_mm_type, 16)
            hex_value_mm = hex(int_value_mm)
            if self.dispatch_mm_type.__contains__(hex_value_mm):
                score_points = self.dispatch_mm_type[hex_value_mm]()
                if(type(score_points) == int):
                    if(score_points == header_file.SCORE_BOARD.Legit_Operator):
                        logging.info("POINT ON PARSER!!!!!!!!!!!!!!!!!!!! %d", score_points)
                    else:
                        logging.info("IMSI CATCHER!!!!!!!!!! %d", score_points)  
            else:
                logging.debug("Unknown mm type %s", self.packet.msg_mm_type)
                logging.debug(self.packet)
        elif(hasattr(self.packet, 'msg_gmm_type')):
                    int_value_gmm = int(self.packet.msg_gmm_type) #check if 16 needed or why is not needed
                    hex_value_gmm = hex(int_value_gmm)
                    if self.dispatch_gmm_type.__contains__(hex_value_gmm):
                        score_points = self.dispatch_gmm_type[hex_value_gmm]()
                        if(type(score_points) == int):
                            if(score_points == header_file.SCORE_BOARD.Legit_Operator):
                                logging.info("POINT ON PARSER!!!!!!!!!!!!!!!!!!!! %d", score_points)
                            else:
                                logging.info("IMSI CATCHER!!!!!!!!!! %d", score_points) 
                    else:
                        logging.debug("Unknown gmm type %s", self.packet.msg_gmm_type)
                        logging.debug(self.packet)

        elif(hasattr(self.packet, 'msg_rr_type')):
            int_value_rr = int(self.packet.msg_rr_type, 16)
            hex_value_rr = hex(int_value_rr)
            if self.dispatch_rr_type.__contains__(hex_value_rr):
                self.dispatch_rr_type[hex_value_rr]()
            else:
                logging.debug("Unknown rr type %s", self.packet.msg_rr_type)
                logging.debug(self.packet)

        else:
            logging.debug("Unknown msg type")
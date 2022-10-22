from cmath import log
from operator import index
import header_file
import logging
import sys

logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)

class techology(object):
    #constructor
    def __init__(self, score: header_file.score_board, attachment_procedure_bits: header_file.pattern_check, 
                    general_info:  header_file.general_info, packet=None):
        self.packet = packet
        self.score = score
        self.attachment_procedure_bits = attachment_procedure_bits
        self.general_info = general_info
        self.index = None
        self.dispatch_mm_type = {
            header_file.MM_TYPE_MSG.IMSI_Detach_Indication.value : self.handle_imsi_detach_indication,
            header_file.MM_TYPE_MSG.Identify_Request.value : self.handle_identify_request,
            header_file.MM_TYPE_MSG.Identify_Response.value : self.handle_identify_response,
            header_file.MM_TYPE_MSG.Location_Updating_Request.value : self.handle_location_update_request,
            header_file.MM_TYPE_MSG.Location_Updating_Accept.value : self.handle_location_update_accept,
            header_file.MM_TYPE_MSG.Location_Updating_Reject.value : self.handle_location_update_reject,
            header_file.MM_TYPE_MSG.Authentication_Request.value : self.handle_authentication_request,
            header_file.MM_TYPE_MSG.Authentication_Response.value : self.handle_authetication_response,
            header_file.MM_TYPE_MSG.MM_Information.value : self.handle_mm_information,
            header_file.MM_TYPE_MSG.CM_SERVICE_REQUEST.value : self.handle_cm_service_request
        }

        self.dispatch_gmm_type = {
            header_file.GMM_TYPE_MSG.Attach_Request.value : self.handle_attach_request,
            header_file.GMM_TYPE_MSG.Attach_Complete.value : self.handle_attach_complete,
            header_file.GMM_TYPE_MSG.Attach_Accept.value : self.handle_attach_accept,
            header_file.GMM_TYPE_MSG.Detach_Request.value : self.handle_detach_request,
            header_file.GMM_TYPE_MSG.Authentication_And_Ciphering_Response.value : self.handle_auth_and_ciphering_response,
            header_file.GMM_TYPE_MSG.Authentication_And_Ciphering_Request.value : self.handle_auth_and_ciphering_request,
            header_file.GMM_TYPE_MSG.GMM_Information.value : self.handle_gmm_information,
            header_file.GMM_TYPE_MSG.Identity_Request.value : self.handle_identity_request,
            header_file.GMM_TYPE_MSG.Identity_Response.value : self.handle_identity_response,
            header_file.GMM_TYPE_MSG.Routing_Area_Update_Accept.value : self.handle_routing_area_update_accept,
            header_file.GMM_TYPE_MSG.Routing_Area_Update_Complete.value : self.handle_routing_area_update_complete
        }

        self.dispatch_rr_type = {
            header_file.RR_TYPE_MSG.System_Information_Type_3.value : self.handle_system_information_type_3,
            header_file.RR_TYPE_MSG.System_Information_Type_13.value : self.handle_known_rr_msg,
            header_file.RR_TYPE_MSG.System_Information_Type_5ter.value : self.handle_known_rr_msg,
            header_file.RR_TYPE_MSG.System_Information_Type_2quater.value : self.handle_known_rr_msg,
            header_file.RR_TYPE_MSG.Channel_Release.value : self.handle_known_rr_msg,
            header_file.RR_TYPE_MSG.Measurement_Report.value : self.handle_known_rr_msg,
            header_file.RR_TYPE_MSG.Classmark_Change.value : self.handle_known_rr_msg,
            header_file.RR_TYPE_MSG.System_Information_Type_1.value : self.handle_known_rr_msg,
            header_file.RR_TYPE_MSG.System_Information_Type_2.value : self.handle_known_rr_msg,
            header_file.RR_TYPE_MSG.System_Information_Type_4.value : self.handle_known_rr_msg,
            header_file.RR_TYPE_MSG.System_Information_Type_5.value : self.handle_known_rr_msg,
            header_file.RR_TYPE_MSG.System_Information_Type_6.value : self.handle_known_rr_msg,
            header_file.RR_TYPE_MSG.Paging_Request_Type_1.value : self.handle_known_rr_msg,
            header_file.RR_TYPE_MSG.Paging_Request_Type_2.value : self.handle_known_rr_msg,
            header_file.RR_TYPE_MSG.GPRS_Suspension_Request.value : self.handle_known_rr_msg,
            header_file.RR_TYPE_MSG.Ciphering_Mode_Command.value : self.handle_ciphering_mode_command,
            header_file.RR_TYPE_MSG.Ciphering_Mode_Complete.value : self.handle_known_rr_msg,
            header_file.RR_TYPE_MSG.Immediate_Assignment.value : self.handle_known_rr_msg
        }

        self.dispatch_emm_type = {
            header_file.EMM_TYPE_MSG.Authentication_Request.value : self.handle_authentication_request,
            header_file.EMM_TYPE_MSG.Identity_Request.value : self.handle_identify_request,
            header_file.EMM_TYPE_MSG.Security_Mode_Command.value : self.handle_security_mode_command,
            header_file.EMM_TYPE_MSG.Tracking_Area_Update_Reject.value : self.handle_location_update_reject
        }

        self.dispatch_rrc_type = {
            header_file.RRC_MESSAGE.RRCConnectionRequest.value : self.handle_rrc_connection_request,
            header_file.RRC_MESSAGE.RRCConnectionReconfiguration.value : self.handle_rrc_connection_reconfiguration,
            header_file.RRC_MESSAGE.RRCConnectionReleaseComplete.value : self.handle_rrc_connection_release_complete,
            header_file.RRC_MESSAGE.RRCConnectionReleaseLte.value : self.handle_rrc_connection_release_lte,
            header_file.RRC_MESSAGE.RRCConnectionReleaseUmts.value : self.handle_rrc_connection_release_umts,
            header_file.RRC_MESSAGE.RRCConnectionSetup.value : self.handle_rrc_connection_setup,
            header_file.RRC_MESSAGE.RRCConnectionSetupComplete.value : self.handle_rrc_connection_setup_complete,
            header_file.RRC_MESSAGE.RRCSecurityModeCommand.value : self.handle_rrc_security_mode_command,
            header_file.RRC_MESSAGE.RRCUeCapabilityEnquiry.value : self.handle_rrc_ue_capability_enquiry
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
    
    def handle_cm_service_request(self):
        logging.debug("CM_Service_Request")
    
    def handle_security_mode_command(self):
        logging.debug("Security_Mode_Command")


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

    def handle_ciphering_mode_command(self):
        logging.debug("Ciphering_Mode_Command")

    def handle_known_rr_msg(self):
        int_value_rr = int(self.packet.msg_rr_type, 16)
        hex_value_rr = hex(int_value_rr)
        logging.debug(header_file.RR_TYPE_MSG(hex_value_rr).name)

    #######################
    # HANDLE RRC TYPE MSG #
    #######################

    def handle_rrc_connection_request(self):
        logging.debug("RRC Connection Request")
    
    def handle_rrc_connection_setup(self):
        logging.debug("RRC Connection Setup")

    def handle_rrc_connection_reconfiguration(self):
        logging.debug("RRC Connection Reconfiguration")

    def handle_rrc_connection_release_lte(self):
        logging.debug("RRC Connection Release Lte")
    
    def handle_rrc_connection_release_umts(self):
        logging.debug("RRC Connection Release Umts")
    
    def handle_rrc_security_mode_command(self):
        logging.debug("RRC Security Mode Command")
    
    def handle_rrc_connection_release_complete(self):
        logging.debug("RRC Connection Release Complete")
    
    def handle_rrc_connection_setup_complete(self):
        logging.debug("RRC Connection Setup Complete")
    
    def handle_rrc_ue_capability_enquiry(self):
        logging.debug("RRC Ue Capability Enquiry")



class gsm(techology):
        #constructor
    def __init__(self, score: header_file.score_board, attachment_procedure_bits: header_file.pattern_check, 
                    general_info:  header_file.general_info, packet=None):
        super(gsm, self).__init__(score, attachment_procedure_bits, general_info, packet)

    ######################
    # HANDLE MM TYPE MSG #
    ######################

    def handle_imsi_detach_indication(self):
        logging.debug("IMSI Detach Indication")
        self.score.clear_points()
        self.attachment_procedure_bits.clear_checker()
        self.general_info.clear_vars()
        if(hasattr(self.packet, 'gsm_a_tmsi')):
            logging.debug("\t TMSI : %s", self.packet.gsm_a_tmsi)
    
    def handle_identify_request(self):
        logging.debug("Identify Request")
        self.attachment_procedure_bits.set_checker(1)

    def handle_location_update_request(self):
        logging.debug("Location Updating Request")
        self.general_info.set_location_update_req_last_seen(True)
        checker = self.attachment_procedure_bits.get_checker()
        current_point = self.score.get_overall_score()

        if(checker != 0):
            self.attachment_procedure_bits.clear_checker() # need to be clear ? 
            self.score.clear_points()

        self.attachment_procedure_bits.set_checker(0)
        if(hasattr(self.packet, 'gsm_a_tmsi')):
            logging.debug("\t TMSI Available : %s", self.packet.gsm_a_tmsi)
            self.general_info.set_tmsi_mm(self.packet.gsm_a_tmsi)
        elif(hasattr(self.packet, 'e212_imsi')):
            logging.debug("\t IMSI Available : %s", self.packet.e212_imsi) #check if field imsi is correct
            self.general_info.set_imsi(self.packet.e212_imsi)
        if(current_point != 0):
            #self.attachment_procedure_bits.clear_checker()  not sure here how it come in this state
            logging.INFO("WTF!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            return current_point        

    def handle_location_update_accept(self):
        logging.debug("Location Updating Accept")        
        self.general_info.set_location_update_req_last_seen(False)
        if(hasattr(self.packet, 'gsm_a_tmsi')):
            logging.debug("\t TMSI : %s", self.packet.gsm_a_tmsi)
        self.attachment_procedure_bits.set_checker(4)
        self.score.set_location_accept(header_file.SCORE_BOARD.Points_Location_Accept.value)
        self.general_info.set_location_update_req_last_seen(None)


    def handle_location_update_reject(self):
        logging.debug("Location Updating Reject")
        self.general_info.set_location_update_req_last_seen(False)
        self.score.set_location_accept(header_file.SCORE_BOARD.Points_Location_Reject.value)
        overall_score = self.score.get_overall_score()
        self.score.clear_points()
        self.attachment_procedure_bits.clear_checker() 
        self.general_info.set_location_update_req_last_seen(None)
        return overall_score

    def handle_authentication_request(self):
        logging.debug("Authentication Request")    
        self.attachment_procedure_bits.set_checker(2)
        if(self.packet.rand != 0):
            self.score.set_authentication_request(header_file.SCORE_BOARD.Points_Authentication_Request.value)

    #######################
    # HANDLE GMM TYPE MSG #
    #######################

    def handle_attach_request(self):
        logging.debug("Attach_Request")
        if(hasattr(self.packet, 'gsm_a_tmsi')):
            logging.debug("\t TMSI : %s", self.packet.gsm_a_tmsi)   
        self.attachment_procedure_bits.set_checker(5)

    def handle_attach_accept(self):
        logging.debug("Attach_Accept")
        if(hasattr(self.packet, 'gsm_a_tmsi')):
            logging.debug("\t TMSI : %s", self.packet.gsm_a_tmsi)   
            self.attachment_procedure_bits.set_checker(6)
            self.score.set_attach_accept(header_file.SCORE_BOARD.Points_Attach_Accept.value)
            if self.attachment_procedure_bits.check_bits():
                self.score.set_pattern_points(header_file.SCORE_BOARD.Points_Pattern.value)        
            overall_score = self.score.get_overall_score() 
            self.score.clear_points()
            self.attachment_procedure_bits.clear_checker()
            self.general_info.set_cell_id_on_attach(self.general_info.get_cell_identity())
            self.general_info.clear_vars()
            return overall_score
    
    def handle_detach_request(self):
        logging.debug("Detach_Request")
        if(hasattr(self.packet, 'gsm_a_tmsi')):
            logging.debug("\t TMSI : %s", self.packet.gsm_a_tmsi)   
            self.score.clear_points()
            self.attachment_procedure_bits.clear_checker()

    def handle_auth_and_ciphering_request(self):
        logging.debug("Authentication_And_Ciphering_Request")
        if(self.packet.gsm_a_gm_gmm_type_of_ciph_alg != 0):
            self.score.set_auth_and_cipher(header_file.SCORE_BOARD.Points_Authentication_And_Ciphering_Request.value)

    #######################
    # HANDLE RR TYPE MSG #
    #######################

    def handle_system_information_type_3(self):
        logging.debug("System_Information_Type 3")
        if(self.general_info.get_location_update_req_last_seen() == None):
            #print(self.index)
            self.general_info.set_sip3_last_seen(self.index)
            self.general_info.set_cell_identity(self.packet.gsm_a_bssmap_cell_ci)

    def handle_ciphering_mode_command(self):
        logging.debug("Ciphering_Mode_Command")
        self.attachment_procedure_bits.set_checker(3)
        #check if ciphering mode is on
        if(self.packet.gsm_a_rr_SC != 0):
            self.score.set_cipher_mode_command(header_file.SCORE_BOARD.Points_Ciphering_Mode_Command.value)


    #######################
    #   HANDLER LOGIC     #
    #######################
    def handle_packet(self):
        if(hasattr(self.packet, 'msg_mm_type')):
            int_value_mm = int(self.packet.msg_mm_type, 16)
            hex_value_mm = hex(int_value_mm)
            if self.dispatch_mm_type.__contains__(hex_value_mm):
                score_points = self.dispatch_mm_type[hex_value_mm]()
                self.handle_result(score_points)
            else:
                logging.debug("Unknown mm type %s", self.packet.msg_mm_type)
                logging.debug(self.packet)
        elif(hasattr(self.packet, 'msg_gmm_type')):
                    int_value_gmm = int(self.packet.msg_gmm_type) #check if 16 needed or why is not needed
                    hex_value_gmm = hex(int_value_gmm)
                    if self.dispatch_gmm_type.__contains__(hex_value_gmm):
                        score_points = self.dispatch_gmm_type[hex_value_gmm]()
                        self.handle_result(score_points)
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

    def handle_result(self, score_points):
        if(type(score_points) == int):
            if(score_points >= header_file.SCORE_BOARD.Legit_Operator):
                logging.info("REAL OPERATOR -> %d", score_points)
                logging.info("At Cell ID -> %s", self.general_info.get_cell_id_on_attach() )
                self.general_info.set_imsi_catched(False)
            else:
                logging.info("IMSI CATCHER -> %d", score_points) 
                self.general_info.set_imsi_catched(True)

class umts(techology):
        #constructor
    def __init__(self, score: header_file.score_board, attachment_procedure_bits: header_file.pattern_check, 
                    general_info:  header_file.general_info, packet=None):
        super(umts, self).__init__(score, attachment_procedure_bits, general_info, packet)

    #######################
    #   HANDLER LOGIC     #
    #######################
    def handle_packet(self):
        if(hasattr(self.packet, 'gsm_a_dtap_msg_mm_type')):
            int_value_mm = int(self.packet.gsm_a_dtap_msg_mm_type, 16)
            hex_value_mm = hex(int_value_mm)
            if self.dispatch_mm_type.__contains__(hex_value_mm):
                score_points = self.dispatch_mm_type[hex_value_mm]()
                self.handle_result(score_points) 
            else:
                logging.debug("Unknown mm type %s", self.packet.gsm_a_dtap_msg_mm_type)
                print("INT :", int_value_mm, "HEX:",hex_value_mm)
                logging.debug(self.packet)
        elif(hasattr(self.packet, 'gsm_a_dtap_msg_gmm_type')):
                    int_value_gmm = int(self.packet.gsm_a_dtap_msg_gmm_type) #check if 16 needed or why is not needed
                    hex_value_gmm = hex(int_value_gmm)
                    if self.dispatch_gmm_type.__contains__(hex_value_gmm):
                        score_points = self.dispatch_gmm_type[hex_value_gmm]()
                        self.handle_result(score_points)
                    else:
                        logging.debug("Unknown gmm type %s", self.packet.gsm_a_dtap_msg_gmm_type)
                        logging.debug(self.packet)

        elif(hasattr(self.packet, 'gsm_a_dtap_msg_rr_type')):
            int_value_rr = int(self.packet.gsm_a_dtap_msg_rr_type, 16)
            hex_value_rr = hex(int_value_rr)
            if self.dispatch_rr_type.__contains__(hex_value_rr):
                self.dispatch_rr_type[hex_value_rr]()
            else:
                logging.debug("Unknown rr type %s", self.packet.gsm_a_dtap_msg_rr_type)
                logging.debug(self.packet)

        elif(hasattr(self.packet, 'rrc_message')):
            if(self.packet.rrc_message == header_file.RRC_MESSAGE.SecurityModeCommand.value):
                logging.debug("THIS WILL NEVER RUN BASED ON THE FILTER IN PARSER!!")
                self.security_mode_command()
        else:
            logging.debug("Unknown msg type")

    def handle_result(self, score_points):
        if(type(score_points) == int):
            if(score_points >= header_file.SCORE_BOARD.Legit_Operator):
                logging.info("REAL OPERATOR -> %d", score_points)
            else:
                logging.info("IMSI CATCHER -> %d", score_points) 

    ######################
    # HANDLE MM TYPE MSG #
    ######################
    
    def handle_location_update_request(self):
        logging.debug("Location Updating Request")
        self.general_info.set_location_update_req_last_seen(True)
        checker = self.attachment_procedure_bits.get_checker()
        current_point = self.score.get_overall_score()

        if(checker != 0):
            self.attachment_procedure_bits.clear_checker() # need to be clear ? 
            self.score.clear_points()

        self.attachment_procedure_bits.set_checker(0)
        if(hasattr(self.packet, 'gsm_a_tmsi')):
            logging.debug("\t TMSI Available : %s", self.packet.gsm_a_tmsi)
            self.general_info.set_tmsi_mm(self.packet.gsm_a_tmsi)
        elif(hasattr(self.packet, 'e212_imsi')):
            logging.debug("\t IMSI Available : %s", self.packet.e212_imsi) #check if field imsi is correct
            self.general_info.set_imsi(self.packet.e212_imsi)
        if(current_point != 0):
            #self.attachment_procedure_bits.clear_checker()  not sure here how it come in this state
            logging.INFO("WTF!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            return current_point      

    def handle_authentication_request(self):
        logging.debug("Authentication Request")    
        self.attachment_procedure_bits.set_checker(2)
        if(self.packet.gsm_a_dtap_rand != 0):
            self.score.set_authentication_request(header_file.SCORE_BOARD.Points_Authentication_Request.value)

    def handle_identify_request(self):
        logging.debug("Identify Request")
        self.attachment_procedure_bits.set_checker(4)

    def handle_location_update_accept(self):
        logging.debug("Location Updating Accept")        
        self.general_info.set_location_update_req_last_seen(False)
        if(hasattr(self.packet, 'gsm_a_tmsi')):
            logging.debug("\t TMSI : %s", self.packet.gsm_a_tmsi)
        self.attachment_procedure_bits.set_checker(5)
        self.score.set_location_accept(header_file.SCORE_BOARD.Points_Location_Accept.value)
        self.general_info.set_location_update_req_last_seen(None)


    def handle_imsi_detach_indication(self):
        logging.debug("IMSI Detach Indication")
        self.score.clear_points()
        self.attachment_procedure_bits.clear_checker()
        self.general_info.clear_vars()
        if(hasattr(self.packet, 'gsm_a_tmsi')):
            logging.debug("\t TMSI : %s", self.packet.gsm_a_tmsi)

    def handle_location_update_reject(self):
        logging.debug("Location Updating Reject")
        self.general_info.set_location_update_req_last_seen(False)
        self.score.set_location_accept(header_file.SCORE_BOARD.Points_Location_Reject.value)
        overall_score = self.score.get_overall_score()
        self.score.clear_points()
        self.attachment_procedure_bits.clear_checker() 
        self.general_info.set_location_update_req_last_seen(None)
        return overall_score

    #######################
    # HANDLE GMM TYPE MSG #
    #######################

    def handle_detach_request(self):
        logging.debug("Detach_Request")
        if(hasattr(self.packet, 'gsm_a_tmsi')):
            logging.debug("\t TMSI : %s", self.packet.gsm_a_tmsi)   
            self.score.clear_points()
            self.attachment_procedure_bits.clear_checker()

    def handle_attach_request(self):
        logging.debug("Attach_Request")
        if(hasattr(self.packet, 'gsm_a_tmsi')):
            logging.debug("\t TMSI : %s", self.packet.gsm_a_tmsi)   
        self.attachment_procedure_bits.set_checker(1)

    def handle_attach_accept(self):
        logging.debug("Attach_Accept")
        if(hasattr(self.packet, 'gsm_a_tmsi')):
            logging.debug("\t TMSI : %s", self.packet.gsm_a_tmsi)   
            self.attachment_procedure_bits.set_checker(6)
            self.score.set_attach_accept(header_file.SCORE_BOARD.Points_Attach_Accept.value)
            if self.attachment_procedure_bits.check_bits():
                self.score.set_pattern_points(header_file.SCORE_BOARD.Points_Pattern.value)
            overall_score = self.score.get_overall_score() 
            self.score.clear_points()
            self.attachment_procedure_bits.clear_checker()
            self.general_info.set_cell_id_on_attach(self.general_info.get_cell_identity())
            self.general_info.clear_vars()
            return overall_score   

    def handle_auth_and_ciphering_request(self):
        logging.debug("Authentication_And_Ciphering_Request")
        if(self.packet.gsm_a_gm_gmm_type_of_ciph_alg != 0):
            self.score.set_auth_and_cipher(header_file.SCORE_BOARD.Points_Authentication_And_Ciphering_Request.value)

#TODO sip3 cell id etc
    def handle_system_information_type_3(self):
        logging.debug("System_Information_Type 3")
        if(self.general_info.get_location_update_req_last_seen() == None):
            #print(self.index)
            self.general_info.set_sip3_last_seen(self.index)
            self.general_info.set_cell_identity(self.packet.gsm_a_bssmap_cell_ci)
            
    def security_mode_command(self):
        logging.debug("Security Mode Command")
        self.attachment_procedure_bits.set_checker(3)
        if(self.packet.rrc_startRestart != 0):
            self.score.set_cipher_mode_command(header_file.SCORE_BOARD.Points_Ciphering_Mode_Command.value)

class lte(techology):
            #constructor
    def __init__(self, score: header_file.score_board, attachment_procedure_bits: header_file.pattern_check, 
                    general_info:  header_file.general_info, packet=None):
        super(lte, self).__init__(score, attachment_procedure_bits, general_info, packet)

    #######################
    #   HANDLER LOGIC     #
    #######################

    def handle_packet(self):
        if(hasattr(self.packet, 'nas_eps_nas_msg_emm_type')):
            int_value_emm = int(self.packet.nas_eps_nas_msg_emm_type, 10)
            hex_value_emm = hex(int_value_emm)
            if self.dispatch_emm_type.__contains__(hex_value_emm):
                score_points = self.dispatch_emm_type[hex_value_emm]()
                self.handle_result(score_points) 
            else:
                logging.debug("Unknown emm type %s", self.packet.nas_eps_nas_msg_emm_type)
                print("INT :", int_value_emm, "HEX:",hex_value_emm)
                logging.debug(self.packet)
                
        elif(hasattr(self.packet, 'lte-rrc_c1')):
                if(not(hasattr(self.packet, 'lte-rrc.dlInformationTransfer_element'))):
                    int_value_rrc = self.packet.lte_rrc_c1
                    if self.dispatch_rrc_type.__contains__(int_value_rrc):
                        score_points = self.dispatch_rrc_type[int_value_rrc]()
                        self.handle_result(score_points)
                    else:

                        logging.debug("Unknown RRC type %s", self.packet.lte_rrc_c1)
                        logging.debug(self.packet)
                        exit(0)
        else:
            logging.debug("Unknown msg type")
    
    def handle_result(self, score_points):
        if(type(score_points) == int):
            if(score_points >= header_file.SCORE_BOARD.Legit_Operator):
                logging.info("REAL OPERATOR -> %d", score_points)
                self.general_info.set_imsi_catched(False)
            else:
                logging.info("IMSI CATCHER -> %d", score_points) 
                self.general_info.set_imsi_catched(True)
#####
#EMM#
##### 
    def handle_authentication_request(self):
        logging.debug("Authendication Request")
        self.attachment_procedure_bits.set_checker(3)
        self.score.set_authentication_request(header_file.SCORE_BOARD.Points_Authentication_Request)
        return

    def handle_identify_request(self):
        logging.debug("Identify Request")
        self.attachment_procedure_bits.set_checker(2)
        return

    def handle_security_mode_command(self):
        logging.debug("security_mode_command")
        self.attachment_procedure_bits.set_checker(4)
        self.score.set_cipher_mode_command(header_file.SCORE_BOARD.Points_Ciphering_Mode_Command)
        return

    def handle_location_update_reject(self):
        logging.debug("Location Updating Reject")
        self.score.set_location_accept(header_file.SCORE_BOARD.Points_Location_Reject.value)
        overall_score = self.score.get_overall_score()
        self.score.clear_points()
        self.attachment_procedure_bits.clear_checker() 
        return overall_score
######
#RRC#
######   

    def handle_rrc_connection_request(self):
        logging.debug("RRC connection request")
        if(self.attachment_procedure_bits.get_checker()):
            self.attachment_procedure_bits.clear_checker()
            self.score.clear_points()

        self.attachment_procedure_bits.set_checker(0)


        return

    def handle_rrc_connection_setup(self):
        logging.debug("RRC connection setup")
        self.attachment_procedure_bits.set_checker(1)
        self.score.set_rrc_connection_setup(header_file.SCORE_BOARD.Points_RRC_Connection_Setup)
        return

    def handle_rrc_security_mode_command(self):
        logging.debug("RRC security mode command")
        self.attachment_procedure_bits.set_checker(5)
        self.score.set_rrc_security_mode_command(header_file.SCORE_BOARD.Points_RRC_Security_Mode_Command)
        return
    
    def handle_rrc_connection_reconfiguration(self):
        logging.debug("RRC connection reconfiguration")
        self.attachment_procedure_bits.set_checker(6)
        self.score.set_rrc_connection_reconfiguration(header_file.SCORE_BOARD.Points_RRC_Connection_Reconfguration)
        if self.attachment_procedure_bits.check_bits():
            logging.debug("RRC connection reconfiguration checking about bits")
            self.score.set_pattern_points(header_file.SCORE_BOARD.Points_Pattern)
        overall_score = self.score.get_overall_score()
        self.score.clear_points()
        self.attachment_procedure_bits.clear_checker()
        return overall_score  

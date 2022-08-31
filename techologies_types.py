import header_file
import logging
import sys

logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)

class techology(object):
    #constructor
    def __init__(self, packet, score: header_file.score_board, 
                gsm_attachment_procedure_bits: header_file.pattern_check, general_info:  header_file.general_info):
        self.packet = packet
        self.score = score
        self.gsm_attachment_procedure_bits = gsm_attachment_procedure_bits
        self.general_info = general_info

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

    def handle_identify_response(self):
        logging.debug("Identify Response")
        if(hasattr(self.packet, 'gsm_a_tmsi')):
            logging.debug("\t TMSI : %s", self.packet.gsm_a_tmsi)
        elif(hasattr(self.packet, 'e212_imsi')):
            logging.debug("\t IMSI Available : %s", self.packet.e212_imsi)

    def handle_location_update_request(self):
        logging.debug("Location Updating Request")
        self.general_info.set_location_update_req_last_seen = True
        retrun_flag = False
        checker = self.gsm_attachment_procedure_bits.get_checker()
        if(checker == 0):
            self.gsm_attachment_procedure_bits.set_checker(0)

        else:
            current_point = self.score.get_overall_score()
            retrun_flag = not self.gsm_attachment_procedure_bits.check_bits()
            self.gsm_attachment_procedure_bits.clear_checker()
            self.score.clear_points()
            self.gsm_attachment_procedure_bits.set_checker(0)
            logging.debug("MAX RETURN POINTS : %d", current_point)
            #no need to return pattern bits because at attachment complete I will do it.
        if(hasattr(self.packet, 'gsm_a_tmsi')):
            logging.debug("\t TMSI Available : %s", self.packet.gsm_a_tmsi)
            self.score.set_location_update_request(header_file.SCORE_BOARD.Points_Location_Updating_Request_TMSI.value)
            self.general_info.__tmsi_mm = packet.gsm_a_tmsi
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
            logging.debug("\t TMSI : %s", packet.gsm_a_tmsi)
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
        gsm_attachment_procedure_bits.set_checker(2)
        score.set_authentication_request(header_file.SCORE_BOARD.Points_Authentication_Request.value)

    def handle_authetication_response(self):
        logging.debug("Authentication Response")
        if(hasattr(self.packet, 'gsm_a_tmsi')):
            logging.debug("\t TMSI : %s", self.packet.gsm_a_tmsi)

    def handle_mm_information(self):
        logging.debug("MM_Information")
        if(hasattr(self.packet, 'gsm_a_tmsi')):
            logging.debug("\t TMSI : %s", self.packet.gsm_a_tmsi)


class gsm(techology):
    def handle_mm_information(self):
        logging.debug("GSM")
        if(hasattr(self.packet, 'gsm_a_tmsi')):
            logging.debug("\t TMSI : %s", self.packet.gsm_a_tmsi)

gsm_attachment_procedure_bits = header_file.pattern_check()
score = header_file.score_board()
general_info = header_file.general_info()
packet = ['key1' , 'lala']

emp = techology(packet, score, gsm_attachment_procedure_bits, general_info)
emp.handle_authentication_request()
print(emp.score.get_overall_score())



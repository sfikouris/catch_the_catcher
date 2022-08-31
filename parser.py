import pyshark 
import handler
import logging
import sys
import header_file

#logging.basicConfig(stream=sys.stderr, level=logging.INFO)

technology = str(sys.argv[1])

#cap = pyshark.FileCapture('pcaps/gsm_imsi_catcher.pcapng', display_filter='gsm_a.dtap')
cap = pyshark.FileCapture('pcaps/umts_attach_real_oper.pcapng', display_filter='rrc')
cap_json = pyshark.FileCapture('pcaps/gsm_multiple_attach_detach_request.pcapng', display_filter='gsm_a.dtap.msg_mm_type || gsm_a.dtap.msg_gmm_type', use_json = True)

#display_filter='gsm_a.dtap.msg_mm_type || gsm_a.dtap.msg_gmm_type'
#gsm_a.dtap.msg_rr_type == 0x1b
#pcaps/gsm_multiple_attach_detach_request.pcapng

#print(cap_mm[0]["gsm_a.dtap"])
# print(cap_mm[0]['gsm_a.dtap'].msg_mm_type)

# print(len([packet for packet in cap]))

#UMTS
# print(dir(cap[0].DATA))
# if(hasattr(cap[0].DATA, 'gsm_a_dtap_msg_gmm_type')):
#     print(cap[0].DATA.gsm_a_tmsi)
#     print("ASD")
# exit(1)
# print(dir(cap[44]['gsm_a.dtap']))
# print("\n",cap[44]['gsm_a.dtap']._all_fields)
# print(cap[44]['gsm_a.dtap'].e212_imsi)
# a = cap_mm[52]['gsm_a.dtap'].msg_gmm_type


#print(cap_json[44])

# print(type(a))
gsm_attachment_procedure_bits = header_file.pattern_check()
score = header_file.score_board()
general_info = header_file.general_info()

if technology == "gsm" :
    for index, packet in enumerate(cap):
        int_value_mm = 0
        int_value_gmm = 0
        int_value_rr = 0
        hex_value_mm = 0
        hex_value_gmm = 0
        hex_value_rr = 0
        score_points = None
        packet = packet["gsm_a.dtap"]
        if(hasattr(packet, 'msg_mm_type')):
            int_value_mm = int(packet.msg_mm_type, 16)
            hex_value_mm = hex(int_value_mm)
            if handler.dispatch_mm_type.__contains__(hex_value_mm):
                score_points = handler.dispatch_mm_type[hex_value_mm](packet, score, gsm_attachment_procedure_bits, general_info)
                if(type(score_points) == int):
                    if(score_points == header_file.SCORE_BOARD.Legit_Operator):
                        logging.info("POINT ON PARSER!!!!!!!!!!!!!!!!!!!! %d", score_points)
                    else:
                        logging.info("IMSI CATCHER!!!!!!!!!! %d", score_points)  
            else:
                logging.debug("Unknown mm type %s", packet.msg_mm_type)
                logging.debug(packet)
                
        elif(hasattr(packet, 'msg_gmm_type')):
            int_value_gmm = int(packet.msg_gmm_type) #check if 16 needed or why is not needed
            hex_value_gmm = hex(int_value_gmm)
            if handler.dispatch_gmm_type.__contains__(hex_value_gmm):
                score_points = handler.dispatch_gmm_type[hex_value_gmm](packet, score, gsm_attachment_procedure_bits)
                if(type(score_points) == int):
                    if(score_points == header_file.SCORE_BOARD.Legit_Operator):
                        logging.info("POINT ON PARSER!!!!!!!!!!!!!!!!!!!! %d", score_points)
                    else:
                        logging.info("IMSI CATCHER!!!!!!!!!! %d", score_points) 
            else:
                logging.debug("Unknown gmm type %s", packet.msg_gmm_type)
                logging.debug(packet)

        elif(hasattr(packet, 'msg_rr_type')):
            int_value_rr = int(packet.msg_rr_type, 16)
            hex_value_rr = hex(int_value_rr)
            if handler.dispatch_rr_type.__contains__(hex_value_rr):
                handler.dispatch_rr_type[hex_value_rr](packet, general_info, index)
            else:
                logging.debug("Unknown rr type %s", packet.msg_rr_type)
                logging.debug(packet)

        else:
            logging.debug("Unknown msg type")

elif technology == "umts":
    for index, packet in enumerate(cap):
        int_value_mm = 0
        int_value_gmm = 0
        int_value_rr = 0
        hex_value_mm = 0
        hex_value_gmm = 0
        hex_value_rr = 0
        score_points = None
        if(hasattr(packet.DATA,'gsm_a_dtap_msg_mm_type')):
            packet = packet.DATA
            int_value_mm = int(packet.gsm_a_dtap_msg_mm_type, 16)
            hex_value_mm = hex(int_value_mm)
            if handler.dispatch_mm_type.__contains__(hex_value_mm):    
                score_points = handler.dispatch_mm_type[hex_value_mm](packet, score, gsm_attachment_procedure_bits, general_info)
                if(type(score_points) == int):
                    if(score_points == header_file.SCORE_BOARD.Legit_Operator):
                        logging.info("POINT ON PARSER!!!!!!!!!!!!!!!!!!!! %d", score_points)
                    else:
                        logging.info("IMSI CATCHER!!!!!!!!!! %d", score_points)  
            else:
                logging.debug("Unknown mm type %s", packet.gsm_a_dtap_msg_mm_type)
                logging.debug(packet)
        elif(hasattr(packet.DATA, 'gsm_a_dtap_msg_gmm_type')):
            packet = packet.DATA
            int_value_gmm = int(packet.gsm_a_dtap_msg_gmm_type) #check why no 16 needed like mm.
            hex_value_gmm = hex(int_value_gmm)
            if handler.dispatch_gmm_type.__contains__(hex_value_gmm):
                score_points = handler.dispatch_gmm_type[hex_value_gmm](packet, score, gsm_attachment_procedure_bits)
                if(type(score_points) == int):
                    if(score_points == header_file.SCORE_BOARD.Legit_Operator):
                        logging.info("POINT ON PARSER!!!!!!!!!!!!!!!!!!!! %d", score_points)
                    else:
                        logging.info("IMSI CATCHER!!!!!!!!!! %d", score_points)  
            else:
                logging.debug("Unknown gmm type %s", packet.gsm_a_dtap_msg_gmm_type)
                print("DAMEE,", hex_value_gmm)
                logging.debug(cap[index])
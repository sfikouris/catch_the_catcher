import pyshark 
import handler
import logging
import sys
import header_file
logging.basicConfig(stream=sys.stderr, level=logging.INFO)

cap = pyshark.FileCapture('pcaps/gsm_imsi_catcher.pcapng', display_filter='gsm_a.dtap.msg_mm_type || gsm_a.dtap.msg_gmm_type')
cap_json = pyshark.FileCapture('pcaps/gsm_multiple_attach_detach_request.pcapng', display_filter='gsm_a.dtap.msg_mm_type || gsm_a.dtap.msg_gmm_type', use_json = True)

#gsm_a.dtap.msg_rr_type == 0x1b
#pcaps/gsm_multiple_attach_detach_request.pcapng

#print(cap_mm[0]["gsm_a.dtap"])
# print(cap_mm[0]['gsm_a.dtap'].msg_mm_type)

# print(len([packet for packet in cap]))

#print(cap[44]['gsm_a.dtap'])
# print(dir(cap[44]['gsm_a.dtap']))
# print("\n",cap[44]['gsm_a.dtap']._all_fields)
# print(cap[44]['gsm_a.dtap'].e212_imsi)
# a = cap_mm[52]['gsm_a.dtap'].msg_gmm_type


#print(cap_json[44])

# print(type(a))
#i=0
gsm_attachment_procedure_bits = header_file.pattern_check()
score = header_file.score_board()
for packet in cap:
    #print(i)
    #i=i+1
    #dispatch_msg_type[packet["gsm_a.dtap"]]

    int_value_mm = 0
    int_value_gmm = 0
    hex_value_mm = 0
    hex_value_gmm = 0
    score_points = None

    packet = packet["gsm_a.dtap"]
    if(hasattr(packet, 'msg_mm_type')):
        int_value_mm = int(packet.msg_mm_type, 16)
        hex_value_mm = hex(int_value_mm)
        if handler.dispatch_mm_type.__contains__(hex_value_mm):
            score_points = handler.dispatch_mm_type[hex_value_mm](packet, score, gsm_attachment_procedure_bits)
            if(type(score_points) == int):
                if(score_points == header_file.SCORE_BOARD.Legit_Operator):
                    logging.info("POINT ON PARSER!!!!!!!!!!!!!!!!!!!! %d", score_points)
                else:
                    logging.info("IMSI CATCHER!!!!!!!!!! %d", score_points)  
        else:
            logging.debug("Unknown mm type %s", packet.msg_mm_type)
            print(packet)

            
    elif(hasattr(packet, 'msg_gmm_type')):
        int_value_gmm = int(packet.msg_gmm_type)
        hex_value_gmm = hex(int_value_gmm)
        if handler.dispatch_gmm_type.__contains__(hex_value_gmm):
            handler.dispatch_gmm_type[hex_value_gmm](packet, score, gsm_attachment_procedure_bits)
            score_points = handler.dispatch_gmm_type[hex_value_gmm](packet, score, gsm_attachment_procedure_bits)
            if(type(score_points) == int):
                if(score_points == header_file.SCORE_BOARD.Legit_Operator):
                    logging.info("POINT ON PARSER!!!!!!!!!!!!!!!!!!!! %d", score_points)
                else:
                    logging.info("IMSI CATCHER!!!!!!!!!! %d", score_points) 
        else:
            logging.debug("Unknown gmm type %s", packet.msg_gmm_type)
            print(packet)

    else:
        logging.debug("Unknown msg type")
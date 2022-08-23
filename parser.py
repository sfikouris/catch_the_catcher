import pyshark 
import handler
import logging
import sys
logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)

cap = pyshark.FileCapture('pcaps/gsm_imsi_catcher.pcapng', display_filter='gsm_a.dtap.msg_mm_type || gsm_a.dtap.msg_gmm_type')
cap_json = pyshark.FileCapture('pcaps/gsm_multiple_attach_detach_request.pcapng', display_filter='gsm_a.dtap.msg_mm_type || gsm_a.dtap.msg_gmm_type', use_json = True)

#gsm_a.dtap.msg_rr_type == 0x1b
#pcaps/gsm_multiple_attach_detach_request.pcapng

#print(cap_mm[0]["gsm_a.dtap"])
# print(cap_mm[0]['gsm_a.dtap'].msg_mm_type)

print(len([packet for packet in cap]))

# print(cap[44]['gsm_a.dtap'])
# print(dir(cap[44]['gsm_a.dtap']))
# print("\n",cap[44]['gsm_a.dtap']._all_fields)
# print(cap[44]['gsm_a.dtap'].e212_imsi)
# a = cap_mm[52]['gsm_a.dtap'].msg_gmm_type


#print(cap_json[44])

# print(type(a))
#i=0
for packet in cap:
    #print(i)
    #i=i+1
    score_points = handler.handle_gsm_mm_packet(packet["gsm_a.dtap"])
    if (type(score_points) == int):
        if(score_points == 60):
            logging.info("POINT ON PARSER!!!!!!!!!!!!!!!!!!!! %d", score_points)
        else:
            logging.info("IMSI CATCHER!!!!!!!!!! %d", score_points)
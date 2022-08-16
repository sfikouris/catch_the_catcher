import pyshark 
import test_module

cap_gmm = pyshark.FileCapture('gsm_multiple_attach_detach_request.pcapng', display_filter='gsm_a.dtap.msg_gmm_type')
cap_mm = pyshark.FileCapture('gsm_multiple_attach_detach_request.pcapng', display_filter='gsm_a.dtap.msg_mm_type')


# print(cap_mm[0]["gsm_a.dtap"]._all_fields)
# print(cap_mm[0]['gsm_a.dtap'].msg_mm_type)

# print(dir(cap_mm[0]))

#print(dir(cap_mm[0]['gsm_a.dtap']))
#print(cap_mm[0]['gsm_a.dtap'].gsm_a_tmsi)

for packet in cap_mm:
   test_module.handle_gsm_mm_packet(packet["gsm_a.dtap"])
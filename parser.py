import pyshark 
import test_module

cap_gmm = pyshark.FileCapture('gsm_multiple_attach_detach_request.pcapng', display_filter='gsm_a.dtap.msg_gmm_type')
cap_mm = pyshark.FileCapture('gsm_multiple_attach_detach_request.pcapng', display_filter='gsm_a.dtap.msg_mm_type')

for packet in cap_mm:
   test_module.check_gsm_msg_mm_type(packet["gsm_a.dtap"].msg_mm_type)
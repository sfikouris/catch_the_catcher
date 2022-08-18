from tkinter import Y
import pyshark 
import handler

cap = pyshark.FileCapture('gsm_multiple_attach_detach_request.pcapng', display_filter='gsm_a.dtap.msg_mm_type || gsm_a.dtap.msg_gmm_type')

#print(cap_mm[0]["gsm_a.dtap"])
# print(cap_mm[0]['gsm_a.dtap'].msg_mm_type)

print(len([packet for packet in cap]))

# print(cap_mm[56]['gsm_a.dtap'])
# print(dir(cap_mm[56]['gsm_a.dtap']))
# print(cap_mm[52]['gsm_a.dtap'])
# a = cap_mm[52]['gsm_a.dtap'].msg_gmm_type
# print(type(a))
#i=0
for packet in cap:
    #print(i)
    #i=i+1
    handler.handle_gsm_mm_packet(packet["gsm_a.dtap"])
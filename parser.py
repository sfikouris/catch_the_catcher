import pyshark 


#protocols that are coming to a GSM attach
#GSM RLC/MAC, GSMTAP.
#need to take only gsmtap most probably. => display_filter='gsm_a.dtap.msg_gmm_type'
cap = pyshark.FileCapture('example.pcapng', display_filter='gsm_a.dtap.msg_gmm_type')
print(cap)


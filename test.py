import pyshark 
import header_file
import techologies_types


attachment_procedure_bits = header_file.pattern_check()
score = header_file.score_board()
general_info = header_file.general_info()

'''GSM TESTING'''
gsm_cap = pyshark.FileCapture('pcaps/gsm_multiple_attach_detach_request.pcapng', display_filter='gsm_a.dtap')
#Read techology
# packet = gsm_cap[328]["gsm_a.dtap"]

# print(dir(packet))
# print(packet._all_fields)
# print(packet.gsm_a_gm_gmm_type_of_ciph_alg)

# gsm_cap = pyshark.FileCapture('pcaps/gsm_multiple_attach_detach_request.pcapng', display_filter='gsm_a.dtap')
# gsm = techologies_types.gsm(score, attachment_procedure_bits, general_info)
# for index, packet in enumerate(gsm_cap):
#     packet = packet["gsm_a.dtap"]
#     gsm.set_packet(packet)
#     gsm.set_index(index)
#     print(index)
#     gsm.handle_packet()

'''UMTS TESTING'''
#umts_cap = pyshark.FileCapture('pcaps/umts_attach_real_oper.pcapng', display_filter='gsm_a.dtap')
umts_cap = pyshark.FileCapture('pcaps/umts_attach_real_oper.pcapng', display_filter='rrc.message')
#packet = umts_cap[88].DATA
umts = techologies_types.umts(score, attachment_procedure_bits, general_info)

# print(umts_cap[25])
packet = umts_cap[21]
#print(dir(packet))

print(packet.DATA._all_fields)
# print(packet.DATA.rrc_startRestart)

# for index, packet in enumerate(umts_cap):
#     print(index)
#     if(hasattr(packet, 'DATA')):
#         packet = packet.DATA
#         if(hasattr(packet, 'gsm_a_dtap_msg_mm_type')):
#             print("MM")
#         elif(hasattr(packet, 'gsm_a_dtap_msg_gmm_type')):
#             print("GMM")
#         elif(hasattr(packet, 'gsm_a_dtap_msg_rr_type')):
#             print("RR")
#         elif(hasattr(packet, 'rrc_message')):
#             if(packet.rrc_message == header_file.RRC_MESSAGE.SecurityModeCommand.value):
#                 print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAaaa")
#             else:
#                 print(packet.rrc_message)
#         else:
#             print(packet)
#             print(packet._all_fields)
            
    
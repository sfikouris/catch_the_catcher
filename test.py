import pyshark 
import header_file
import techologies_types

gsm_cap = pyshark.FileCapture('pcaps/gsm_multiple_attach_detach_request.pcapng', display_filter='gsm_a.dtap')

#Read techology

packet = gsm_cap[328]["gsm_a.dtap"]

print(dir(packet))
print(packet._all_fields)
print(packet.gsm_a_gm_gmm_type_of_ciph_alg)



# attachment_procedure_bits = header_file.pattern_check()
# score = header_file.score_board()
# general_info = header_file.general_info()


# gsm_cap = pyshark.FileCapture('pcaps/gsm_multiple_attach_detach_request.pcapng', display_filter='gsm_a.dtap')
# gsm = techologies_types.gsm(score, attachment_procedure_bits, general_info)
# for index, packet in enumerate(gsm_cap):
#     packet = packet["gsm_a.dtap"]
#     gsm.set_packet(packet)
#     gsm.set_index(index)
#     print(index)
#     gsm.handle_packet()
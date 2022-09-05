import pyshark 
import logging
import sys
import header_file
import techologies_types
logging.basicConfig(stream=sys.stderr, level=logging.INFO)

#Read techology
technology = str(sys.argv[1])

attachment_procedure_bits = header_file.pattern_check()
score = header_file.score_board()
general_info = header_file.general_info()

if technology == "gsm":
    gsm_cap = pyshark.FileCapture('pcaps/gsm_multiple_attach_detach_request.pcapng', display_filter='gsm_a.dtap')
    gsm = techologies_types.gsm(score, attachment_procedure_bits, general_info)
    for index, packet in enumerate(gsm_cap):
        packet = packet["gsm_a.dtap"]
        gsm.set_packet(packet)
        gsm.set_index(index)
        gsm.handle_packet()
elif technology == "umts":
    umts_cap = pyshark.FileCapture('pcaps/umts_attach_real_oper.pcapng', display_filter='gsm_a.dtap')
    #umts_cap = pyshark.FileCapture('pcaps/umts_imsi_catcher.pcapng', display_filter='gsm_a.dtap')
    umts = techologies_types.umts(score, attachment_procedure_bits, general_info)
    for index, packet in enumerate(umts_cap):
        if(hasattr(packet, 'DATA')):
            packet = packet.DATA
            umts.set_packet(packet)
            umts.set_index(index)
            umts.handle_packet()
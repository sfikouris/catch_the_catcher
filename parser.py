import pyshark 
#import logging
import sys
import header_file
import techologies_types
import subprocess

#logging.basicConfig(stream=sys.stderr, level=logging.INFO)

#Read techology
technology = str(sys.argv[1])

#Read the type of detection Live or static
detection = str(sys.argv[2])

if detection == "live":
    process = subprocess.Popen(['./../../QCSuper/qcsuper.py', '--adb', '--pcap-dump', 'testing_sub'])
    try:
        print('Running in process', process.pid)
        process.wait(timeout=30)
    except subprocess.TimeoutExpired:
        print('Timed out', process.pid)
        process.kill()
        print('Timed out', process.pid)
    print('Done')

attachment_procedure_bits = header_file.pattern_check()
score = header_file.score_board()
general_info = header_file.general_info()

if technology == "gsm":
    #gsm_cap = pyshark.FileCapture('pcaps/gsm_multiple_attach_detach_request.pcapng', display_filter='gsm_a.dtap')
    gsm_cap = pyshark.FileCapture('testing_sub', display_filter='gsm_a.dtap')
    gsm = techologies_types.gsm(score, attachment_procedure_bits, general_info)
    for index, packet in enumerate(gsm_cap):
        packet = packet["gsm_a.dtap"]
        gsm.set_packet(packet)
        gsm.set_index(index)
        gsm.handle_packet()
        if(general_info.get_imsi_catched()):
            print("IMSI CATCHER IN PARSER")
            print("cell id of rogue cell : ", general_info.get_cell_identity())
            general_info.set_imsi_catched(False)
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
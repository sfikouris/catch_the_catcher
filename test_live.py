from concurrent.futures import process
from re import X
import pyshark 
import os 
import subprocess
import sys
#os.system("python ../../QCSuper/qcsuper.py --adb --wireshark-live")
process = subprocess.Popen(['./../../QCSuper/qcsuper.py', '--adb', '--pcap-dump', 'testing_sub'])
try:
    print('Running in process', process.pid)
    process.wait(timeout=5)
except subprocess.TimeoutExpired:
    print('Timed out', process.pid)
    process.kill()
    print('Timed out', process.pid)
print('Done')
# cap = pyshark.LiveCapture()
# cap.sniff(timeout=50)
#TODO find a way to kill adb.
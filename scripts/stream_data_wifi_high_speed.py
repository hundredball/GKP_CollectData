import sys; sys.path.append('..') # help python find cyton.py relative to scripts folder
from openbci import wifi as bci
import logging
import numpy as np

def printData(sample):
    global records
    #print(sample.sample_number)
    #print(sample.channel_data)
    #records = np.vstack((records, np.array(sample.channel_data)))


if __name__ == '__main__':
    logging.basicConfig(filename="test.log",format='%(asctime)s - %(levelname)s : %(message)s',level=logging.DEBUG)
    logging.info('---------LOG START-------------')
    # If you don't know your IP Address, you can use shield name option
    # If you know IP, such as with wifi direct 192.168.4.1, then use ip_address='192.168.4.1'
    records = np.zeros(16)
    trial_num = 1
    shield_name = 'OpenBCI-4D85'
    shield = bci.OpenBCIWiFi(shield_name=shield_name, log=True, high_speed=True)
    print("WiFi Shield Instantiated")
    shield.start_streaming(printData)
    shield.loop()

# -*- coding: utf-8 -*-
"""
Created on Tue Jul 27 16:30:47 2021

@author: Sandora
"""

from pylablib.devices import Thorlabs
import time
import struct
from ThorlabsShutterFunctions import *


# USER DEFINED PARAMETERS
on_time = int(5e3) # in 1 ms steps
off_time = int(5e3)
num_cycles = 2


print('Device found: ',Thorlabs.list_kinesis_devices())

try:

    shutter = Thorlabs.kinesis.BasicKinesisDevice("68000959")
    shutter.open()
    # on_time, off_time, num_cycles = get_cycle_params(shutter)
    
    set_operating_mode(shutter,2)
    set_cycle_params(shutter, on_time, off_time, num_cycles)
    
    # open shutter once
    shutter_on(shutter)
    # time.sleep(2)
    # shutter_off(shutter)

    

    shutter.close()

except KeyboardInterrupt:
    shutter.close()
    print('Interrupted by user')    
        
except:
    shutter.close()
    print('Sth not working here')
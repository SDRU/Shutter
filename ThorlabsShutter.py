# -*- coding: utf-8 -*-
"""
Created on Tue Jul 27 16:30:47 2021

@author: Sandora
"""

from pylablib.devices import Thorlabs
import time


# USER DEFINED PARAMETERS
on_time = 5e3 # in 1 ms steps
off_time = 5e3
num_cycles = 3

devices = Thorlabs.list_kinesis_devices()
print('Devices found: ',devices)

class DeviceNotConnectedError(Exception):
    pass

try:
    
    for device in devices:
        serial_nr = device[0]
        if serial_nr.startswith("6"):
            shutter = Thorlabs.kinesis.KinesisDevice(serial_nr)
            shutter.open()
            
        else:
            raise DeviceNotConnectedError
    on_time, off_time, num_cycles = shutter.get_cycle_params()
    
    shutter.set_operating_mode(mode=3)
    shutter.set_cycle_params(on_time=on_time, off_time=off_time, num_cycles=num_cycles)
    
    # # open shutter once
    shutter.shutter_open()
    
    time.sleep(35)
        
    
    shutter.close()
    
except DeviceNotConnectedError:
    print("No shutter connected")

except KeyboardInterrupt:
    shutter.close()
    print('Interrupted by user')    
        
except:
    shutter.close()
    print('Sth not working here')
    
    

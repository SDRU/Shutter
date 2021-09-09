# -*- coding: utf-8 -*-
"""
Created on Tue Aug  3 15:46:18 2021

@author: Sandora
"""

import struct

def set_cycle_params(shutter,on_time, off_time, num_cycles):
    message = struct.pack("<HLLL",1,int(on_time),int(off_time),int(num_cycles))
    shutter.send_comm(0x04C3,param1=0x0E,param2=0x00,source=0x01,dest=0x50)
    shutter.send_comm_data(0x04C3,data=message,source=0x01,dest=0x50)
    
    
def get_cycle_params(shutter):
    params=shutter.query(0x04C4,param1=0x01,param2=0x00,source=0x01,dest=0x50).data
    print(params)
    on_time, off_time, num_cycles = struct.unpack("<LLL",params[2:14])
    return on_time, off_time, num_cycles

def shutter_on(shutter):
    shutter.send_comm(0x04CB,param1=0x01,param2=0x01,source=0x01,dest=0x50)
    
def shutter_off(shutter):
    shutter.send_comm(0x04CB,param1=0x01,param2=0x02,source=0x01,dest=0x50)
    
def set_operating_mode(shutter,mode):
    #   0x01 SOLENOID_MANUAL - In this mode, operation of the 
    # solenoid is via the front panel ‘Enable’ button, or by the 
    # ‘Output’ buttons on the GUI panel. 
    #   0x02 SOLENOID_SINGLE - In this mode, the solenoid will 
    # open and close each time the front panel ‘Enable’ button is 
    # pressed, or the ‘Output ON’ button on the GUI panel is 
    # clicked. The ON and OFF times are specified by calling the 
    # MGMSG_MOT_SET_SOL_CYCLEPARAMS message. 
    #   0x03 SOLENOID_AUTO - In this mode, the solenoid will open 
    # and close continuously after the front panel ‘Enable’ button 
    # is pressed, or the ‘Output ON’ button on the GUI panel is 
    # clicked. The ON and OFF times, and the number of cycles 
    # performed, are specified by calling the 
    # MGMSG_MOT_SET_SOL_CYCLEPARAMS message.
    #   0x04 SOLENOID_TRIGGER - In Triggered mode, a rising edge 
    # on rear panel TRIG IN BNC input will start execution of the 
    # parameters programmed on the unit (On Time, Off Time, 
    # Num Cycles - see MGMSG_MOT_SET_SOL_CYCLEPARAMS
    # message.). The unit must be primed (i.e. the ENABLE button 
    # pressed and the ENABLED LED lit) before the unit can 
    # respond to the external trigger
    shutter.send_comm(0x04C0,param1=0x01,param2=mode,source=0x01,dest=0x50)

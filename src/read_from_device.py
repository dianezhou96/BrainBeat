
import zephyr
from zephyr.testing import simulation_workflow

import platform
import serial


import sys
#sys.path.append( "C:\Users\gleslie\Dropbox (MIT)\PC\LSL\liblsl-Python\pylsl")
from pylsl import StreamInfo, StreamOutlet


z_breathing = StreamInfo('Breathing','Breathing',1,25,'float32','COM5');
z_ecg = StreamInfo('ECG','ECG',1,250,'float32','COM5');
z_acceleration = StreamInfo('Acc','Acceleration',3,100,'float32','COM5');
#z_rr = StreamInfo('Zephyr','RR',1,100,'float32','BHBHT012580-iSerialPort1');



# next make an outlet
z_breathing_outlet = StreamOutlet(z_breathing, 32, 360)
z_ecg_outlet = StreamOutlet(z_ecg, 32, 360)
z_acceleration_outlet = StreamOutlet(z_acceleration, 32, 360)
#z_rr_outlet = StreamOutlet(z_rr)

def callback(value_name, value):
    print value_name, value

    if value_name=='breathing':
        mysample=[value]
        z_breathing_outlet.push_sample(mysample)
    elif value_name=='ecg':
        mysample=[value]
        z_ecg_outlet.push_sample(mysample)
    elif value_name=='acceleration':
        mysample=list(value)
        z_acceleration_outlet.push_sample(mysample)

    # create the new sample and push to the stream
    #mysample = [hand.palm_position.x,hand.palm_position.y,hand.palm_position.z]
    #outlet.push_sample(mysample)
    return

def main():
    zephyr.configure_root_logger()
    
    #serial_port_dict = {"Darwin": "/dev/cu.BHBHT001931-iSerialPort1",
    #serial_port_dict = {"Darwin": "/dev/tty.BHBHT012580-iSerialPort1",
    serial_port_dict = {"Darwin": "/dev/cu.BHBHT012580-iSerialPort1",
                        "Windows": "COM5"}


    
    serial_port = serial_port_dict[platform.system()]
    ser = serial.Serial(serial_port)
    
    simulation_workflow([callback], ser)


if __name__ == "__main__":
    main()

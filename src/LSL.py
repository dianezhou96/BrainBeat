### SAMPLE CODE ###
#  for communicating with LSL

from pylsl import StreamInfo, StreamOutlet
# first create a new stream info (here we set the name to Leap, the content-type to mocap, 3 channels, 100 Hz, and float-valued data)
# The last value would be the serial number of the device or some other more or less locally unique identifier for the stream as far as available (you could also omit it but interrupted connections wouldn't auto-recover).
info = StreamInfo('Zephyr','Breathing-ECG-acceleration-rr',4,100,'float32','BHBHT012580-iSerialPort1');

# next make an outlet
outlet = StreamOutlet(info)

# create the new sample and push to the stream
mysample = [hand.palm_position.x,hand.palm_position.y,hand.palm_position.z]
outlet.push_sample(mysample)
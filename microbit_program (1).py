# Add your Python code here. E.g.
from microbit import *
#sets period to 10ms
pin16.set_analog_period(10)
while True:
    #makes var knob and sets it equal to the knob outout int
    knob=pin2.read_analog()
    #converts knob value to a value the motor can read
    #the equation below is for y=mx+b, where the m is slope and equals (.175/1023)
    #the x vaule is the knob and the b vaule is 0.055 which is the starting %
    y = (0.175/1023)*knob+.055
    #moves motor using the converted knob value
    #y is a percent of 1024 so we have to multiply
    pin16.write_analog(y*1024)
    

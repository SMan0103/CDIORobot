#!/usr/bin/env python3

from time import sleep

from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_B, SpeedPercent, MoveTank, Motor
from ev3dev2.sensor import INPUT_1
from ev3dev2.sensor.lego import TouchSensor
from ev3dev2.led import Leds


 
input("press to start")

print("driving")


#Get the motor to driving part

m = Motor(OUTPUT_A)
# n = LargeMotor(OUTPUT_B)
m.on_for_rotations(-100, 25)

# m.on_for_rotations(100, 3)
# n.on_for_rotations(-100, 5)


print("done")
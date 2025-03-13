#!/usr/bin/env python3

from time import sleep
from math import pi

from ev3dev2.motor import LargeMotor, Motor, OUTPUT_A, OUTPUT_B, SpeedPercent, MoveTank
from ev3dev2.sensor import INPUT_1
from ev3dev2.sensor.lego import TouchSensor
from ev3dev2.led import Leds

wheel_dia = 25 # mm
wheel_circumf = 25*pi*2

print("Initializing")

#mA = Motor(OUTPUT_A)
mAll = MoveTank(OUTPUT_A, OUTPUT_B, motor_class=Motor)


def movemm(mm):
    print("Driving motors")
    print("circ: ", wheel_circumf)
    rotations = mm/wheel_circumf
    print("rot:", rotations)
    mAll.on_for_rotations(left_speed=SpeedPercent(10), right_speed=SpeedPercent(10), rotations=rotations) 


movemm(10)
#!/usr/bin/env python3

from time import sleep
from math import pi

from ev3dev2.motor import LargeMotor, Motor, OUTPUT_A, OUTPUT_B, SpeedPercent, MoveTank
from ev3dev2.sensor import INPUT_1
from ev3dev2.sensor.lego import TouchSensor, GyroSensor
from ev3dev2.led import Leds


userinput = input("Press enter to start program")


while(userinput != 'q'):
    wheel_dia = 25 # mm
    wheel_circumf = 25*pi*2
    Robotwith = 220

    print("Initializing")

    #mA = Motor(OUTPUT_A)
    mAll = MoveTank(OUTPUT_A, OUTPUT_B, motor_class=Motor)
    # mAll.gyro = GyroSensor(INPUT_1)

    def movemm(mm):
        print("Driving motors")
        print("circ: ", wheel_circumf)
        rotations = mm/wheel_circumf
        print("rot:", rotations)
        mAll.on_for_rotations(left_speed=SpeedPercent(10), right_speed=SpeedPercent(10), rotations=rotations) 



    def rotagedeg(deg):
        mm = (Robotwith / deg) * 100 
        print("Driving motors")
        print("circ: ", wheel_circumf)
        rotations = mm/wheel_circumf
        print("rot:", rotations)
        mAll.on_for_rotations(left_speed=SpeedPercent(75), right_speed=SpeedPercent(-75), rotations=rotations) 


    # movemm(10)


    rotagedeg(90)

    # mAll.turn_degrees(50, 90)
    userinput = input("Press enter to start program")
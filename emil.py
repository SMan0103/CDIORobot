#!/usr/bin/env python3

from time import sleep

from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_B, OUTPUT_C,OUTPUT_D, SpeedPercent, MoveTank, Motor,MoveSteering
from ev3dev2.sensor import INPUT_1
from ev3dev2.sensor.lego import TouchSensor
from ev3dev2.led import Leds


# input("press to start")

# print("driving")


# #Get the motor to driving part

# m = Motor(OUTPUT_A)
# # n = LargeMotor(OUTPUT_B)
# m.on_for_rotations(-100, 25)

# # m.on_for_rotations(100, 3)
# # n.on_for_rotations(-100, 5)


# print("done")


# LargeMotor(address=OUTPUT_A).on(speed=0)

robot = MoveSteering(left_motor_port=OUTPUT_A, right_motor_port=OUTPUT_B)
grabber = LargeMotor(address=OUTPUT_C)

grabber.on(speed=100)
hej = ""
while hej != 'q':
    hej = input("type")
    if(hej == 'q'):
        # robot.off()
        grabber.off()
    # if(hej == 'g'):
    #     GrabberHelper = Motor(OUTPUT_D)
    #     GrabberHelper.on_for_rotations(speed=-100, rotations=10)
    #     GrabberHelper.on_for_rotations(speed=100, rotations=10)

    else:
        robot.on(steering=0,speed=int(hej))
        pass
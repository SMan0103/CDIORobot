#!/usr/bin/env python3

from time import sleep
from math import pi

import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("192.168.137.139", 12358))
server_socket.listen(1)

print("Waiting for connection...")
conn, addr = server_socket.accept()
# print(f"Connected by {addr}")

from ev3dev2.motor import LargeMotor, Motor, OUTPUT_A, OUTPUT_B, OUTPUT_C, OUTPUT_D, SpeedPercent, MoveTank, MoveSteering
from ev3dev2.sensor import INPUT_1
from ev3dev2.sensor.lego import TouchSensor, GyroSensor
from ev3dev2.led import Leds




userinputforMetoh = ''


robot = MoveSteering(left_motor_port=OUTPUT_A, right_motor_port=OUTPUT_B)
grabber = LargeMotor(address=OUTPUT_C)

grabber.on(speed=100)

def GrabberHelper():
        """
        The helper grabber for the main grabber if a bold is in the coner.
        """
        GrabberHelper = Motor(OUTPUT_D)
        GrabberHelper.on_for_rotations(speed=-50, rotations=0.32)
        sleep(1)
        GrabberHelper.on_for_rotations(speed=50, rotations=0.32)

def drop():
    grabber.on(speed=-100)   


def powerdown():
    grabber.off()
    robot.off()
    conn.close()
    server_socket.close()
    exit()


while(userinputforMetoh != 'q'):
    userinputforMetoh = ''
    wheel_dia = 25 # mm
    wheel_circumf = 25*pi*2
    Robotwith = 220

    while userinputforMetoh == "":
        userinputforMetoh= conn.recv(1024).decode()
        try:
            splitInput = userinputforMetoh.split("\n")[-2].split("#") 
        except: 
            powerdown()
        

        Rotate = int(splitInput[0])
        
        moment = int(splitInput[1])

        #print("Received: " + userinputforMetoh)
        print("moment: ", Rotate)
        print("Rotate: ", moment)
            

    if (userinputforMetoh == 'd'):
        drop()

    robot.on(steering=Rotate,speed=moment) 




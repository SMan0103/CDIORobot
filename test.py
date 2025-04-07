#!/usr/bin/env python3

from time import sleep
from math import pi
import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("192.168.137.139", 12358))
server_socket.listen(1)

print("Waiting for connection...")
conn, addr = server_socket.accept()

from ev3dev2.motor import LargeMotor, Motor, OUTPUT_A, OUTPUT_B, OUTPUT_C, OUTPUT_D, SpeedPercent, MoveTank, MoveSteering

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
    while userinputforMetoh == "":
        userinputforMetoh= conn.recv(1024).decode()
        try:
            splitInput = userinputforMetoh.split("\n")[-3].split("#") 
        except: 
            powerdown()
        
        Rotate = int(splitInput[0])
        moment = int(splitInput[1])
        helper = bool(splitInput[2])

        if(helper == True):
             GrabberHelper()

        print("helper: ", helper)
        print("moment: ", Rotate)
        print("Rotate: ", moment)
            

    if (userinputforMetoh == 'd'):
        drop()

    robot.on(steering=Rotate,speed=moment) 




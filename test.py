#!/usr/bin/env python3

from time import sleep
from math import pi

import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("192.168.138.130", 12358))
server_socket.listen(1)

print("Waiting for connection...")
conn, addr = server_socket.accept()
# print(f"Connected by {addr}")



userinputforMetoh = ''

from ev3dev2.motor import LargeMotor, Motor, OUTPUT_A, OUTPUT_B, OUTPUT_C, OUTPUT_D, SpeedPercent, MoveTank, MoveSteering
from ev3dev2.sensor import INPUT_1
from ev3dev2.sensor.lego import TouchSensor, GyroSensor
from ev3dev2.led import Leds

# userinput = input("Press enter to start program")
robot = MoveSteering(left_motor_port=OUTPUT_A, right_motor_port=OUTPUT_B)
# grabber = LargeMotor(address=OUTPUT_C)



while(userinputforMetoh != 'q'):
    userinputforMetoh = ''
    wheel_dia = 25 # mm
    wheel_circumf = 25*pi*2
    Robotwith = 220

    while userinputforMetoh == "":
        userinputforMetoh= conn.recv(1024).decode()
        # userinputforMetoh.split("\n", -1)[0]
        #print("wait for input")
        #print(userinputforMetoh)
        #print("\n")
        splitInput = userinputforMetoh.split("\n")[-2].split("#") 
        Rotate = int(splitInput[0])
        
        moment = int(splitInput[1])

        #print("Received: " + userinputforMetoh)
        print("moment: ", Rotate)
        print("Rotate: ", moment)
        if userinputforMetoh == 'q':
            # grabber.off()
            robot.off()
            conn.close()
            server_socket.close()
            exit()
        
    # def GrabberHelper():
    #     """
    #     The helper grabber for the main grabber if a bold is in the coner.
    #     """
    #     GrabberHelper = Motor(OUTPUT_C)
    #     GrabberHelper.on_for_rotations(speed=-100, rotations=10)
    #     GrabberHelper.on_for_rotations(speed=100, rotations=10)
    
    
    # grabber.on(speed=100)

    

    robot.on(steering=Rotate,speed=moment) 

#!/usr/bin/env python3

from time import sleep
from math import pi

import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("192.168.138.143", 12353))
server_socket.listen(1)

print("Waiting for connection...")
conn, addr = server_socket.accept()
# print(f"Connected by {addr}")



userinputforMetoh = ''

from ev3dev2.motor import LargeMotor, Motor, OUTPUT_A, OUTPUT_B, OUTPUT_C, SpeedPercent, MoveTank
from ev3dev2.sensor import INPUT_1
from ev3dev2.sensor.lego import TouchSensor, GyroSensor
from ev3dev2.led import Leds


# userinput = input("Press enter to start program")


while(userinputforMetoh != 'q'):
    userinputforMetoh = ''
    wheel_dia = 25 # mm
    wheel_circumf = 25*pi*2
    Robotwith = 220


    while userinputforMetoh == "":
        print("wait for input")
        userinputforMetoh= conn.recv(1024).decode()
        
        Rotate = userinputforMetoh.split("#",1)[0]
        
        moment = userinputforMetoh.split("#",1)[-1]

        print("Received: " + userinputforMetoh)
        if userinputforMetoh == 'q':
            conn.close()
            server_socket.close()
            exit()

    print("Initializing")
    mAll = MoveTank(OUTPUT_A, OUTPUT_B, motor_class=Motor)
    
    def movemm(mm):
        """
        @parm The length that is need to drive forward.   
        """
        print("Driving motors")
        print("circ: ", wheel_circumf)
        rotations = mm/wheel_circumf
        print("rot:", rotations)
        mAll.on_for_rotations(left_speed=SpeedPercent(50), right_speed=SpeedPercent(50), rotations=rotations) 

    
    def Rotatefunc(Deg):
        """
        @parm The length that is need to drive forward.   
        """
        mm = Deg/Robotwith
        print("Driving motors")
        print("circ: ", wheel_circumf)
        rotations = (mm/wheel_circumf) * 100
        print("rot:", rotations)
        mAll.on_for_rotations(left_speed=SpeedPercent(50), right_speed=SpeedPercent(-50), rotations=rotations) 

    
    def GrabberHelper():
        """
        The helper grabber for the main grabber if a bold is in the coner.
        """
        GrabberHelper = Motor(OUTPUT_C)
        GrabberHelper.on_for_rotations(speed=-100, rotations=10)
        GrabberHelper.on_for_rotations(speed=100, rotations=10)
    
    
    def mainGrabber():
        """
        Spinning the main grabber.
        """
        pass
    

    def Dropping():
        """
        Reversing the main grabber so all the ball will fall out.
        """
        pass


    mAll.on()
    movemm(int(moment))
    Rotatefunc(int(Rotate))

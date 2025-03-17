#!/usr/bin/env python3

from time import sleep
from math import pi

import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("192.168.138.21", 12352))
server_socket.listen(1)

print("Waiting for connection...")
conn, addr = server_socket.accept()
# print(f"Connected by {addr}")



userinputforMetoh = ''

from ev3dev2.motor import LargeMotor, Motor, OUTPUT_A, OUTPUT_B, SpeedPercent, MoveTank
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
        

        # one = hej.split("#",1)[0]
        # two = hej.split("#",1)[-1]
        Rotate = userinputforMetoh.split("#",1)[0]
        # print(Rotate)
        moment = userinputforMetoh.split("#",1)[-1]

        print("Received: " + userinputforMetoh)
        if userinputforMetoh == 'q':
            conn.close()
            server_socket.close()
            exit()

    print("Initializing")
    mAll = MoveTank(OUTPUT_A, OUTPUT_B, motor_class=Motor)
    mAll.gyro = GyroSensor(INPUT_1)

    
    def movemm(mm):
        """
        @parm The length that is need to drive forward.   
        """
        print("Driving motors")
        print("circ: ", wheel_circumf)
        rotations = mm/wheel_circumf
        print("rot:", rotations)
        mAll.on_for_rotations(left_speed=SpeedPercent(50), right_speed=SpeedPercent(50), rotations=rotations) 



    movemm(int(moment))
    
    mAll.turn_degrees(25, int(Rotate))
        


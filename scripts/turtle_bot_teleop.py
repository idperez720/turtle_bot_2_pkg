#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist
from pynput import keyboard as kb

move_msg = Twist()
velLin = 0 
velAng = 0

move_msg.linear.x = 0
move_msg.linear.y = 0
move_msg.linear.z = 0
move_msg.angular.x = 0
move_msg.angular.y = 0
move_msg.angular.z = 0

def on_press(key):
    #print(move)
    try:
        if key.char == 'w':
            move_msg.linear.x = velLin         
            
        elif key.char == 's':
            move_msg.linear.x = -velLin
        elif key.char == 'a':
            move_msg.angular.z = velAng
        elif key.char == 'd':
            move_msg.angular.z = -velAng

    except:
        pass

def on_release(key):
    try:
        if key.char == 'w' or key.char == 's':
            move_msg.linear.x = 0
        elif key.char == 'a' or key.char == 'd':
            move_msg.angular.z = 0

    except:
        pass
listener = kb.Listener(
            on_press=on_press,
            on_release=on_release)

def move():
    cmd_vel_pub = rospy.Publisher('/turtlebot_cmdVel', Twist, queue_size=10)
    rospy.Rate(10)

    while not rospy.is_shutdown():
        cmd_vel_pub.publish(move_msg)

                
                    
if __name__ == '__main__':
    rospy.init_node('turtle_bot_teleop', anonymous=True)
    velLin = float(input('Ingrese la velociadad lineal deseada: '))
    velAng = float(input('Ingrese la velociadad lineal deseada: '))
    listener.start()
    move()

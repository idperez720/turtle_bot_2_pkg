#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist
from pynput import keyboard as kb

move_msg = Twist()
vel = 0

move_msg.linear.x = 0
move_msg.linear.y = 0
move_msg.linear.z = 0
move_msg.angular.x = 0
move_msg.angular.y = 0
move_msg.angular.z = 0
print(move_msg)

def on_press(key):
    #print(move)
    try:
        if key.char == 'w':
            print('w on press') 
            move_msg.linear.x = vel         
            
        elif key.char == 's':
            print('s on press')
            move_msg.linear.x = -vel
        elif key.char == 'a':
            print('a on press')
            move_msg.angular.z = vel
        elif key.char == 'd':
            print('d on press')
            move_msg.angular.z = -vel

    except:
        pass

def on_release(key):
    try:
        if key.char == 'w' or key.char == 's':
            move_msg.linear.x = 0
            print('a on release')
        elif key.char == 'a' or key.char == 'd':
            move_msg.angular.z = 0
            print('s on release')

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
    vel = float(input('Ingrese la velociadad deseada: '))
    listener.start()
    move()

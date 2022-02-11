#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
import keyboard as key


class turtle_bot_teleop:

    def __init__(self):

        ## rosrate define
        self.rate = rospy.Rate(10)

        ## Variable initialization
        self.turtle_pos_x = 0.0
        self.turtle_pos_y = 0.0
        self.turtle_pos_z = 0.0
        self.turtle_linear_vel = 0.0
        self.turtle_move = False
        self.angular_vel = 0.0
        self.move = Twist()

        #Ask for velocity
        # self.turtle_lineal_vel = input('Linear Velocity')

        self.cmd_vel_pub = rospy.Publisher('/turtlebot_cmdVel', Twist, queue_size=10)
        self.orientation = rospy.Publisher('/turtlebot_orientation', Twist, queue_size=10)
        self.position = rospy.Subscriber('/turtlebot_position', Twist, self.callback_pos)


    def callback_pos(self, data):

        self.turtle_pos_x = data.linear.x
        self.turtle_pos_y = data.linear.y
        self.turtle_pos_z = data.angular.z

        self.turtle_pos = [self.turtle_pos_x, self.turtle_pos_y, self.turtle_pos_z]
        print(self.turtle_pos)



        #self.moveit()
        if key.is_pressed('w'):
            self.move.linear = 5
            self.cmd_vel_pub.publish(self.move)
        ## Move revers
        if key.is_pressed('s'):
            self.move.linear = -5
            self.cmd_vel_pub.publish(self.move)
        ## Move left

    def moveit(self):
        ## Move straigth
        if key.is_pressed('w'):
            self.move.linear = 5
            self.cmd_vel_pub.publish(self.move)
        ## Move revers
        if key.is_pressed('s'):
            self.move.linear = -5
            self.cmd_vel_pub.publish(self.move)
        ## Move left
       # if keyboard.is_pressed('left'):

        ## Move right
       # if keyboard.is_pressed('right'):

if __name__ == '__main__':
    print('hola')
    rospy.init_node('turtle_bot_teleop', anonymous=True)
    print('hola')
    turtle_bot_teleop()
    rospy.spin()

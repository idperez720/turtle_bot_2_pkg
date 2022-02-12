#!/usr/bin/env python3
import rospy
import numpy as np
from geometry_msgs.msg import Twist
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib as mpl
import math
import matplotlib.patches as patches
import tkinter as Tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

trackX = [] 
trackY = []
trackZ = []


def callback_pose(data):

    turtle_pos_x = np.round(data.linear.x, 3)
    turtle_pos_y = np.round(data.linear.y, 3)
    turtle_pos_z = np.round(data.angular.z, 3)

    trackX.append(turtle_pos_x)
    trackY.append(turtle_pos_y)
    trackZ.append(turtle_pos_z)

    pos_array = [turtle_pos_x, turtle_pos_y, turtle_pos_z]
    print(pos_array)


def animate(i, trackX, trackY, trackZ):
    # Draw x and y lists

    t = mpl.markers.MarkerStyle(marker=(3,0))
    t._transform = t.get_transform().rotate_deg(math.degrees(trackZ[-1]))

    
    ax.clear()
    rect = patches.Rectangle((2.3, -2.3), -4.6, 4.6, linewidth=1)
    ax.add_patch(rect)
    ax.scatter([-2.3, -2.3, 2.3, 2.3],[2.3, -2.3, -2.3, 2.3])
    ax.plot(trackX, trackY, color='w')







if __name__ == '__main__':
    # crea el nodo
    rospy.init_node('turtle_bot_interface', anonymous=True)
    rospy.Subscriber('/turtlebot_position', Twist, callback_pose)
    rospy.Rate(60)
    
    fig = plt.figure(figsize=(5,5))
    root = Tk.Tk()

    label = Tk.Label(root,text="SHM Simulation").grid(column=0, row=0)

    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.get_tk_widget().grid(column=0,row=1)
    
    ax = fig.add_subplot(1, 1, 1)
    # Format plot
    ax.set_xlim([-2.3, 2.3])
    ax.set_ylim([-2.3, 2.3])

    save_btn = Tk.Button(master = root,
                        height=2,
                        width=10,
                        text='save')
    save_btn.grid(column=0, row=0)
    
    # Set up plot to call animate() function periodically
    ani = animation.FuncAnimation(fig, animate, fargs=(trackX, trackY, trackZ), interval=0)

    Tk.mainloop()
    

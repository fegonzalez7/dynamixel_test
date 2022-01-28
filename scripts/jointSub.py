#!/usr/bin/env python
"""
Allows to subscribe to the topic /joint_states
"""
import rospy
from std_msgs.msg import String
from sensor_msgs.msg import JointState

__author__ = "F Gonzalez, S Realpe, JM Fajardo"
__credits__ = ["Felipe Gonzalez", "Sebastian Realpe", "Jose Manuel Fajardo", "Robotis"]
__email__ = "fegonzalezro@unal.edu.co"
__status__ = "Test"

def callback(data):
    rospy.loginfo(data.position)
    if data.position[4]>-2:
        print('gripper abierto')
    else:
        print('gripper cerrado')

def listener():
    rospy.init_node('joint_listener', anonymous=True)
    rospy.Subscriber("/dynamixel_workbench/joint_states", JointState, callback)
    rospy.spin()

if __name__ == '__main__':
    try:
        while not rospy.is_shutdown():
            listener()
    except rospy.ROSInterruptException:
        pass
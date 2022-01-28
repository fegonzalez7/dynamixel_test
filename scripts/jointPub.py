"""
Allows to publish in the topic /joint_trajectory
"""
import rospy
from std_msgs.msg import String
from sensor_msgs.msg import JointState
from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint

__author__ = "F Gonzalez, S Realpe, JM Fajardo"
__credits__ = ["Felipe Gonzalez", "Sebastian Realpe", "Jose Manuel Fajardo", "Robotis"]
__email__ = "fegonzalezro@unal.edu.co"
__status__ = "Test"

def joint_publisher():
    pub = rospy.Publisher('/joint_trajectory', JointTrajectory, queue_size=0)
    rospy.init_node('joint_publisher', anonymous=False)
    
    while not rospy.is_shutdown():
        state = JointTrajectory()
        state.header.stamp = rospy.Time.now()
        state.joint_names = ["joint_1", "joint_2", "joint_3", "joint_4", "joint_5"]
        point = JointTrajectoryPoint()
        point.positions = [0, 0, 0, 0, 0]    
        point.time_from_start = rospy.Duration(0.5)
        state.points.append(point)
        pub.publish(state)
        print('published command')
        rospy.sleep(1)

        state = JointTrajectory()
        state.header.stamp = rospy.Time.now()
        state.joint_names = ["joint_1", "joint_2", "joint_3", "joint_4", "joint_5"]
        point = JointTrajectoryPoint()
        point.positions = [0.25, 0, 0, 0, 1.3]    
        point.time_from_start = rospy.Duration(0.5)
        state.points.append(point)
        pub.publish(state)
        print('published command')
        rospy.sleep(1)

if __name__ == '__main__':
    try:
        joint_publisher()
    except rospy.ROSInterruptException:
        pass
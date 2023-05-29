"""
.. module: custom_msg_node
   :platform: Unix
   :synopsis: Python module for creat custom messages
.. moduleauthor:: Arghavan Dalvand
ROS node for creat custom messages
Subscribes to: `/odom` topic
Publishes to: `/robot_informations` topic

A node to publish custom odometry messages.

This node subscribes to the `/odom` topic and publishes custom messages to
the `/robot_informations` topic.

The custom message type is `odom_custom_msg` which has four fields:
- x (float32): x coordinate of robot's position
- y (float32): y coordinate of robot's position
- vel_x (float32): linear velocity of robot in x direction
- vel_y (float32): linear velocity of robot in y direction
"""




#! /usr/bin/env python3
import rospy
from nav_msgs.msg import Odometry
from second_assignment_rt1.msg import odom_custom_msg
import os
import sys


def publisher(data):
    """Publishes custom ROS message to the 'robot_informations' topic containing position and velocity data.

    This function creates a custom ROS message with position and velocity data extracted from the `Odometry` message
    received as input. The custom message is then published to the `robot_informations` topic.

    Args:
        data (nav_msgs.msg.Odometry): The original message from the `odom` topic.

    Returns:
        None

    Raises:
        None
    """
    

    # Publishes a specific type of ROS message
    publishes_robot_data = rospy.Publisher('robot_informations', odom_custom_msg, queue_size=5)
    """The *publisher()* function publishes a custom ROS message to the *robot_informations* topic containing position and velocity data.
       The Odometry message is passed as a parameter to the function, which extracts the relevant data and publishes it in the custom message."""

    creat_custom_msg = odom_custom_msg()

    creat_custom_msg.x = data.pose.pose.position.x
    creat_custom_msg.y = data.pose.pose.position.y
    creat_custom_msg.vel_x = data.twist.twist.linear.x
    creat_custom_msg.vel_y = data.twist.twist.linear.y

    print(creat_custom_msg)
    # Publishes a specific type of ROS message
    publishes_robot_data.publish(creat_custom_msg)


if __name__ == '__main__':
    try:
        # Initializes a rospy node
        rospy.init_node('custom_msg_node')    
        rospy.Subscriber("/odom", Odometry, publisher)

        # Spin() simply keeps python from existing until this node is stopped
        rospy.spin()
        """ The code then enters a loop using *rospy.spin()*, which keeps the node running until it receives a signal to stop. """
    except rospy.ROSInterruptException:
        print("program interrupted before completion", file=sys.stderr)



"""
Module: service_node
Platform: Unix
Synopsis: Python module for a ROS node that provides a service callback function and a subscriber callback function to count the number of cancelled and reached goals respectively.
Module Author: Arghavan Dalvand

This module contains a ROS node that provides a service callback function and a subscriber callback function to count the number of cancelled and reached goals respectively. The service callback function returns the count of cancelled and reached goals, whereas the subscriber callback function counts the number of cancelled and reached goals and updates the corresponding variables.

Subscribes to:
    /reaching_goal/result

Publishes to: None

Clients: None

"""


#!/usr/bin/env python3

import rospy
from std_srvs.srv import Empty,EmptyResponse
import assignment_2_2022.msg
import os
import sys


reached_goal_count =0
canceled_goal_count = 0
sequence =1 


def service_node(request):
   
    """
    A ROS service callback function that returns the count of cancelled and reached goals.

    Args:
        request (std_srvs/EmptyRequest): A request message with empty content.

    Returns:
        std_srvs/EmptyResponse: An empty response message.
    """
    global canceled_goal_count , reached_goal_count , sequence
    print(f"Sequence: {sequence}\nNumber of canceled goal: {canceled_goal_count}\nnumber of reached goal: {reached_goal_count}")
    print("****")
    sequence += 1
    return EmptyResponse()



def actionserver_subscriber(data):
   
    """
    A ROS subscriber callback function that counts the number of cancelled and reached goals.

    Args:
        data (``assignment_2_2022/PlanningActionResult``): A message containing the status of the goal.
        
    Note: This function assumes that it is subscribing to the 'PlanningActionResult' topic,
    where the status values are 2 for cancelled goals and 3 for reached goals.
    """

    if data.status.status == 2:

        global canceled_goal_count
        canceled_goal_count += 1
    
    elif data.status.status == 3:

        global reached_goal_count
        reached_goal_count += 1


if __name__ == "__main__":
    try:
        # Writing log messages
        rospy.logwarn("service started")

        # Initializes a rospy node
        rospy.init_node('service_node')

        rospy.Subscriber("/reaching_goal/result", assignment_2_2022.msg.PlanningActionResult, actionserver_subscriber)

        rospy.Service('reach_cancel_ints', Empty, service_node)

        # Spin() simply keeps python from existing until this node is stopped
        rospy.spin()
    except rospy.ROSInterruptException:
        print("program interrupted before completion", file=sys.stderr)

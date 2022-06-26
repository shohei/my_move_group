#!/usr/bin/env python
from math import pi
import sys

import moveit_commander
import rospy

def main():
    moveit_commander.roscpp_initialize(sys.argv)
    rospy.init_node('joint_planner')
    move_group = moveit_commander.MoveGroupCommander('my_robot_arm')
    joint_goal = [0, 80*pi/180, 80*pi/180, 0];
    move_group.set_joint_value_target(joint_goal)
    move_group.go(wait=True)
    move_group.stop()

if __name__=="__main__":
    main()

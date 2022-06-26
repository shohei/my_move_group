#!/usr/bin/env python
import sys
import moveit_commander
import rospy

def main():
    moveit_commander.roscpp_initialize(sys.argv)

    rospy.init_node('robot_info')
    robot = moveit_commander.RobotCommander()

    print('==Group Info==')
    print('[group_names]',robot.get_group_names())
    print('[current_state]',robot.get_current_state())
    print('')

    move_group = moveit_commander.MoveGroupCommander('my_robot_arm')

    print('[name]',move_group.get_name())
    print('[planning_frame]',move_group.get_planning_frame())
    print('[interface_description]',move_group.get_interface_description())
    print('')

    print('==Joint Info==')
    print('[active_joints]',move_group.get_active_joints())
    print('[current_joint_values]',move_group.get_current_joint_values())
    print('')

    print('==EndEffector Info==')
    print('[has_end_effector_link]',move_group.has_end_effector_link())
    print('[end_effector_link]',move_group.get_current_pose())
    print('[current_rpy]',move_group.get_current_rpy())
    print('')

if __name__=="__main__":
    main()

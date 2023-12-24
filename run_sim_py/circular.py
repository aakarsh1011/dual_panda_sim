#!/usr/bin/env python

import sys  # Add this line to import the sys module
import rospy
import moveit_commander
from geometry_msgs.msg import PoseStamped
from math import cos, sin  # Import cos and sin from math module

def generate_circular_trajectory(radius, num_points):
    trajectory = []
    for i in range(num_points):
        angle = 2 * i * 3.14159 / num_points
        x = radius * cos(angle)
        y = radius * sin(angle)
        z = 0.5  # Set an appropriate height
        trajectory.append([x, y, z])
    return trajectory

def main():
    moveit_commander.roscpp_initialize(sys.argv)
    rospy.init_node('circular_motion_node', anonymous=True)

    # Add a longer sleep duration before initializing the RobotCommander
    rospy.sleep(5)  # You can adjust this duration based on your system and network speed

    robot = moveit_commander.RobotCommander()
    group = moveit_commander.MoveGroupCommander("panda_1")

    # Set planner parameters if needed
    group.set_planner_id("RRTConnectkConfigDefault")
    group.set_num_planning_attempts(5)
    group.set_goal_orientation_tolerance(0.01)

    radius = 0.2  # Adjust the radius accordingly
    num_points = 100  # Adjust the number of points accordingly
    trajectory = generate_circular_trajectory(radius, num_points)

    for point in trajectory:
        pose = PoseStamped()
        pose.header.frame_id = "panda_1_link0"
        pose.pose.position.x = point[0]
        pose.pose.position.y = point[1]
        pose.pose.position.z = point[2]
        pose.pose.orientation.w = 1.0

        group.set_pose_target(pose)
        group.go(wait=True)
        rospy.sleep(0.1)  # Adjust sleep duration for desired speed

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass


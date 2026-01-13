#!/usr/bin/env python
"""Cooperative pick-pass-place task for two Panda arms in Gazebo.

This script coordinates two MoveIt groups (default: panda_1 and panda_2)
through a basic pick -> handoff -> place routine. It uses MoveIt planning
and attaches/detaches a collision object to simulate grasp/hand-off.

Usage:
  rosrun franka_gazebo cooperative_task.py
  rosrun franka_gazebo cooperative_task.py --group-a panda_1 --group-b panda_2
"""

import argparse
import sys

import moveit_commander
import rospy
from geometry_msgs.msg import PoseStamped


def build_pose(frame_id, x, y, z, qw=1.0, qx=0.0, qy=0.0, qz=0.0):
    pose = PoseStamped()
    pose.header.frame_id = frame_id
    pose.pose.position.x = x
    pose.pose.position.y = y
    pose.pose.position.z = z
    pose.pose.orientation.w = qw
    pose.pose.orientation.x = qx
    pose.pose.orientation.y = qy
    pose.pose.orientation.z = qz
    return pose


def move_to_pose(group, target_pose, description):
    group.set_pose_target(target_pose)
    success = group.go(wait=True)
    group.stop()
    group.clear_pose_targets()
    if not success:
        rospy.logerr("Failed to reach pose: %s", description)
    else:
        rospy.loginfo("Reached pose: %s", description)
    return success


def wait_for_scene(scene, object_id, attached=False, timeout=5.0):
    start_time = rospy.get_time()
    while (rospy.get_time() - start_time) < timeout and not rospy.is_shutdown():
        attached_objects = scene.get_attached_objects([object_id])
        is_attached = len(attached_objects.keys()) > 0
        is_known = object_id in scene.get_known_object_names()
        if attached and is_attached:
            return True
        if not attached and is_known:
            return True
        rospy.sleep(0.1)
    return False


def add_pick_object(scene, frame_id, object_id, size, pose):
    scene.add_box(object_id, pose, size=size)
    if not wait_for_scene(scene, object_id, attached=False):
        rospy.logwarn("Timed out waiting for object to appear in the scene")


def attach_object(scene, group, object_id):
    eef_link = group.get_end_effector_link()
    if not eef_link:
        rospy.logwarn("End effector link not found for group %s", group.get_name())
        return False
    scene.attach_box(eef_link, object_id)
    if not wait_for_scene(scene, object_id, attached=True):
        rospy.logwarn("Timed out waiting for object to attach")
        return False
    return True


def detach_object(scene, object_id):
    scene.remove_attached_object(name=object_id)
    if not wait_for_scene(scene, object_id, attached=False):
        rospy.logwarn("Timed out waiting for object to detach")
        return False
    return True


def main():
    parser = argparse.ArgumentParser(description="Cooperative pick-pass-place task")
    parser.add_argument("--group-a", default="panda_1", help="MoveIt group for arm A")
    parser.add_argument("--group-b", default="panda_2", help="MoveIt group for arm B")
    parser.add_argument("--object-id", default="handoff_box", help="Planning scene object id")
    args = parser.parse_args()

    moveit_commander.roscpp_initialize(sys.argv)
    rospy.init_node("cooperative_pick_pass_place", anonymous=True)

    rospy.sleep(2.0)

    scene = moveit_commander.PlanningSceneInterface()
    group_a = moveit_commander.MoveGroupCommander(args.group_a)
    group_b = moveit_commander.MoveGroupCommander(args.group_b)

    group_a.set_planner_id("RRTConnectkConfigDefault")
    group_b.set_planner_id("RRTConnectkConfigDefault")

    # Create a pick object in front of arm A.
    pick_pose = build_pose("panda_1_link0", 0.4, -0.3, 0.15)
    add_pick_object(scene, "panda_1_link0", args.object_id, size=(0.04, 0.04, 0.08), pose=pick_pose)

    # Arm A pick sequence.
    move_to_pose(group_a, build_pose("panda_1_link0", 0.4, -0.3, 0.25), "arm A pre-pick")
    move_to_pose(group_a, build_pose("panda_1_link0", 0.4, -0.3, 0.17), "arm A pick")
    attach_object(scene, group_a, args.object_id)
    move_to_pose(group_a, build_pose("panda_1_link0", 0.35, 0.0, 0.35), "arm A handoff")

    # Arm B handoff sequence.
    move_to_pose(group_b, build_pose("panda_2_link0", 0.35, 0.0, 0.35), "arm B handoff")
    detach_object(scene, args.object_id)
    attach_object(scene, group_b, args.object_id)

    # Arm B place sequence.
    move_to_pose(group_b, build_pose("panda_2_link0", 0.45, 0.3, 0.25), "arm B pre-place")
    move_to_pose(group_b, build_pose("panda_2_link0", 0.45, 0.3, 0.15), "arm B place")
    detach_object(scene, args.object_id)

    rospy.loginfo("Cooperative pick-pass-place task complete")


if __name__ == "__main__":
    try:
        main()
    except rospy.ROSInterruptException:
        pass

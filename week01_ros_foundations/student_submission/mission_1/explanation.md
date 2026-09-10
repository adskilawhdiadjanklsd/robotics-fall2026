# Mission 1

## Command Path Explanation

The guard has to check if the commands in the /student_cmd_vel does not cause any issues then it publishes the command to /cmd_vel.

## Graph Explanation

A ROS 2 graph shows how the different components of a robot communicate with each other.  /course_cmd_vel_guard is a node and /student_cmd_vel is a topic.

## Guided Checks

{'bridge_info': True, 'command_topics': True, 'guard_info': True, 'node_list': True, 'scan_info': True, 'scan_message': True}

## Scan Observation

I found angle increment which represents that the LiDAR is moving over some degree of an angle every time to see its surrounding.

## Tools Explanation

Gazebo is responsible for sensing while RViz is responsible for helping people see the data.

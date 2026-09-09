# Mission 1

## Scan Observation

I found angle increment which represents that the LiDAR is moving over some degree of an angle every time to see its surrounding.

## Guided Checks

{'node_list': True, 'guard_info': True, 'bridge_info': True, 'scan_info': True, 'scan_message': True, 'command_topics': True}

## Graph Explanation

A ROS 2 graph shows how the different components of a robot communicate with each other.  /course_cmd_vel_guard is a node and /student_cmd_vel is a topic.

## Command Path Explanation

The guard has to check if the commands in the /student_cmd_vel does not cause any issues then it publishes the command to /cmd_vel.

## Tools Explanation

Gazebo is responsible for sensing while RViz is responsible for helping people see the data.

# Week 1: Discovering a Robot Through ROS 2

## Student

- Name: Wei Xi Huang
- Email: weixi.huang15@login.cuny.edu

## mission_1.command_path_explanation

The guard has to check if the commands in the /student_cmd_vel does not cause any issues then it publishes the command to /cmd_vel.

## mission_1.graph_explanation

A ROS 2 graph shows how the different components of a robot communicate with each other.  /course_cmd_vel_guard is a node and /student_cmd_vel is a topic.

## mission_1.guided_checks

{'bridge_info': True, 'command_topics': True, 'guard_info': True, 'node_list': True, 'scan_info': True, 'scan_message': True}

## mission_1.scan_observation

I found angle increment which represents that the LiDAR is moving over some degree of an angle every time to see its surrounding.

## mission_1.tools_explanation

Gazebo is responsible for sensing while RViz is responsible for helping people see the data.

## mission_2.measurement_explanation



## mission_2.motion_comparison



## mission_2.prediction_locks

{'straight': '2026-09-10T00:49:51.166200+00:00'}

## mission_2.predictions

{'straight': 'I predict the robot will move 0.45 meters forward.'}

## mission_2.safety_explanation



## part_1.activity

{'sensor': {'normal': True, 'changed': True}, 'timing': {'normal': True, 'changed': True}, 'hardware': {'normal': True, 'changed': True}}

## part_2.activity

{'reactive': {'normal': True, 'changed': True}, 'behavior': {'normal': True, 'changed': True}, 'deliberative': {'normal': True, 'changed': True}, 'hybrid': {'normal': True, 'changed': True}, 'safety': {'normal': True, 'changed': True}}

## part_3.activity

{'middleware': {'single': True, 'multiple': True}, 'communication': {'topic': True, 'service': True}, 'failure': {'healthy': True, 'sensor': True, 'type': True, 'visualization': True}, 'inspection': {'nodes': True, 'node_info': True, 'topics': True, 'topic_info': True, 'echo': True, 'services': True, 'broken': True}}

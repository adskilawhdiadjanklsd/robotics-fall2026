# Week 1: Discovering a Robot Through ROS 2

## Student

- Name: Wei Xi Huang
- Email: weixi.huang15@login.cuny.edu

## final.architecture_evidence

The node is reactive because it only sees what is immediately in front of it and stops if it senses something in front of it. For it to be a hybrid system it would need to map out some part of the area and know how to move around object blocking it.

## final.course_reflection



## final.hardware_next

I would test the time the function is being processed and the time it takes for the components to get the data.

## final.middleware_debugging

The ROS graph can let you see the publishers and subscribers of a topic or node. This can help you see if what is being connected or not.

## final.system_synthesis

Robot software is difficult because there are many parts that need to work together and that it has to work in the real world. We need to make sure that the robots are not causing problems and crashing into things. We also need to make sure the is a false safe and determine if the data send speed is also not causing safety issues. This is a reactive architecture because the front_distance function uses LiDAR to see and if there is something is detected in front then it will trigger a stop command. The trade-off of this architecture is that it is not that complicated but it lacks spatial awareness. It can not go around the object blocking it's way and just stops since it only looks at what is in front of it and does not have a map of the surrounding area. The ROS 2 middleware connects the sensing, decision, guard, and actuation nodes. The sensing to the decision by having the LiDAR node to record data then the decision node takes the data and decides the velocity then guard node checks if the values are valid and then sends to the actuation which moves the robot. Timing and invalid data affect safety because if the components take a bit longer to send data over, the other components will have previous data which is not the current data and can cause some calculation errors which can cause the safety issues. The  command guard layer can restrict unsafe motion. It can set the range of velocity that the robot can move at and if the communication between the parts fail  or a component crashes, it can instantly trigger a hard stop so that the robot will never perform any dangerous or unpredictable actions. 

## final.timing_evidence

The one with robot speed and response time.

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

Estimated traveled path and start-to-end distance have different measurements because estimated traveled path is the total amount the robot moved while start-to-end distance is the diameter of the curve so it is a straight line from starting point to the ending point.

## mission_2.modified_settings

{'linear_x': 0.22, 'angular_z': 0.8, 'duration': 4.0}

## mission_2.motion_comparison

The rotation simulation result was what I predicted. I predicted 1.5 radians which is about 86 degrees then take 7% less from it is about 80 which is close to 72 and the start-to-end distance is 0 because it didn't have a forward speed.

## mission_2.prediction_locks

{'curve': '2026-09-10T23:15:53.252797+00:00', 'curve_modified': '2026-09-10T23:19:46.207871+00:00', 'rotation': '2026-09-10T23:11:36.174562+00:00', 'straight': '2026-09-10T00:49:51.166200+00:00'}

## mission_2.predictions

{'curve': 'I predict an arc or a circle because it is moving  while turning right so it should curve.', 'curve_modified': 'This curve should be turning left and be tighter because of the higher turning speed', 'rotation': 'I predict its position will stay the same while its direction will be facing 1.50 radians left', 'straight': 'I predict the robot will move 0.45 meters forward.'}

## mission_2.safety_explanation

The command guard checks if the the values of every command to prevent invalid values. The final zero command sets the forward speed and turning speed to zero when the robot has no more commands to execute. The timeout is needed if the communications are not getting to the robot while the it is moving and sends a stop command to the robot.

## mission_3.data_to_command

The front_distance function converts the LiDAR data into an angle and only keeps the angles that are within a range and is a valid number and returns the smallest number. The decide_velocity function if the inputs are valid then it returns a value from 0 to 0.18.

## mission_3.missing_data_safety

The robot stops when there is no valid front measurement because it is safer and so that it doesn't bump into anything.

## mission_3.system_layers

front_distance function acts records what the LiDAR gives it and uses the information then it gets passed to the guard to check if the values are valid then gives a value. decision_velocity function gets a velocity and then gives a number between 0 and 0.18. All this information goes o the ROS node and the command guard needs to check if the everything is good like if it is receiving the communication and nothing crashes.

## part_1.activity

{'sensor': {'normal': True, 'changed': True}, 'timing': {'normal': True, 'changed': True}, 'hardware': {'normal': True, 'changed': True}}

## part_2.activity

{'reactive': {'normal': True, 'changed': True}, 'behavior': {'normal': True, 'changed': True}, 'deliberative': {'normal': True, 'changed': True}, 'hybrid': {'normal': True, 'changed': True}, 'safety': {'normal': True, 'changed': True}}

## part_3.activity

{'middleware': {'single': True, 'multiple': True}, 'communication': {'topic': True, 'service': True}, 'failure': {'healthy': True, 'sensor': True, 'type': True, 'visualization': True}, 'inspection': {'nodes': True, 'node_info': True, 'topics': True, 'topic_info': True, 'echo': True, 'services': True, 'broken': True}}

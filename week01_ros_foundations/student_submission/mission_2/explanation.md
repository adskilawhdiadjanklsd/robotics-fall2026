# Mission 2

## Measurement Explanation

Estimated traveled path and start-to-end distance have different measurements because estimated traveled path is the total amount the robot moved while start-to-end distance is the diameter of the curve so it is a straight line from starting point to the ending point.

## Motion Comparison

The rotation simulation result was what I predicted. I predicted 1.5 radians which is about 86 degrees then take 7% less from it is about 80 which is close to 72 and the start-to-end distance is 0 because it didn't have a forward speed.

## Prediction Locks

{'straight': '2026-09-10T00:49:51.166200+00:00', 'rotation': '2026-09-10T23:11:36.174562+00:00', 'curve': '2026-09-10T23:15:53.252797+00:00', 'curve_modified': '2026-09-10T23:19:46.207871+00:00'}

## Predictions

{'straight': 'I predict the robot will move 0.45 meters forward.', 'rotation': 'I predict its position will stay the same while its direction will be facing 1.50 radians left', 'curve': 'I predict an arc or a circle because it is moving  while turning right so it should curve.', 'curve_modified': 'This curve should be turning left and be tighter because of the higher turning speed'}

## Safety Explanation

The command guard checks if the the values of every command to prevent invalid values. The final zero command sets the forward speed and turning speed to zero when the robot has no more commands to execute. The timeout is needed if the communications are not getting to the robot while the it is moving and sends a stop command to the robot.

## Modified Settings

{'linear_x': 0.22, 'angular_z': 0.8, 'duration': 4.0}

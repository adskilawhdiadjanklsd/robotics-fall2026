# Mission 3

## Data To Command

The front_distance function converts the LiDAR data into an angle and only keeps the angles that are within a range and is a valid number and returns the smallest number. The decide_velocity function if the inputs are valid then it returns a value from 0 to 0.18.

## Missing Data Safety

The robot stops when there is no valid front measurement because it is safer and so that it doesn't bump into anything.

## System Layers

front_distance function acts records what the LiDAR gives it and uses the information then it gets passed to the guard to check if the values are valid then gives a value. decision_velocity function gets a velocity and then gives a number between 0 and 0.18. All this information goes o the ROS node and the command guard needs to check if the everything is good like if it is receiving the communication and nothing crashes.

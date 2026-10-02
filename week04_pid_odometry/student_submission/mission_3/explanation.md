# mission_3 Submission

- Name: (not provided)
- Section: (not provided)

## Explanations

### technical_analysis

It seems like forward speed did not affect how accurate the robot is moving. Too little Kd makes it be off of the blue line a bit but did not go too close to the pedestrians in this case. Increasing Kp made it so that the robot going to the next point faster and not curving the route as much when it is a straight line. Increasing Kd made it so that the robot moves more slowly when it needs to turn but when it is too high it makes too much of an arc when it turns and is not following the route that well and can crash into a pedestrian. Low Ki made it so that when the robot is turning into a straight, it would make a very big curve and not follow the route very well. Increasing the Ki made it so that it made more of a straight line and followed the path more accurately. Low wheel radius estimate makes it go more to the left and too high wheel radius estimate makes it go more to the right.

### human_centered_analysis

The most consequential failure for a pedestrian is that the robot goes super fast and crashes into them. At low speeds it might not do as much damage as if it is going very fast. If you want the robot to be more cautious and go more slowly, it might be blocking the way and might freeze because it doesn't want to do anything risky. If you want the robot to go faster, it is more risky and might cause more accidents and have more errors. The engineers should be responsible for what the robot should do and it depends on the situation.
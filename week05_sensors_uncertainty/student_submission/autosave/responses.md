# Week 5: Sensors, Noise, and Uncertainty

- course_id: 24545015
- email: weixi.huang15@login.cuny.edu
- name: Wei Xi Huang

## concepts.observation

More noise makes the data points be more apart. The bigger numbers get bigger and the smaller numbers get smaller. More bias makes the data points to be higher than the actual and low bias makes it lower than the actual.

## final.course_reflection

The value of connecting technical work with human considerations is that the robot should be safe for people around it and also not stopping the work of other people. If the robot keeps making unnecessary stops it may not be able to function in the environment and even hindering other people.

## final.synthesis

We can use different distance estimations methods to estimate the actual distance. The rolling average takes the mean over a window and minimize the error but has a slower reaction to sudden changes. Median takes the middle number over a window and removes outliers and it has a faster reaction to sudden changes. The different configurations also affect the distance estimation. Taking in more readings make it have less error but reacts slower to sudden changes. The weights make it have more noise and increases error but reacts faster to sudden changes. Depending on the context, we should configure the robot differently. A robot is a warehouse can be more risky compared to a robot working around people. The assistive robot should have more stopping threshold and caution margin than the warehouse robot. By being more safe, the assistive robot has less unnecessary stops and false safes than the warehouse robot. 

## mission_1.bias

0.216

## mission_1.bias_vs_variance

Biased sensor will be constantly some amount over or under the actual distance. A noisy sensor will have more readings that are all over the place with some being very small and some being very large.

## mission_1.dropouts

4

## mission_1.mean

2.216

## mission_1.median

2.21

## mission_1.more_samples

No because the sensors are picking up readings that are constantly off. It might be better to have an offset.

## mission_1.outliers

1

## mission_1.prediction

Bias is the difference between the actual value and estimated value. Variance is how spread apart the data is from the mean.

## mission_1.prediction_draft

Bias is the difference between the actual value and estimated value. Variance is how spread apart the data is from the mean.

## mission_1.profile

biased

## mission_1.robot_consequence

The robot senses a person in front of it but because of the bias, the robot thinks that the person is more further away then it is actually and does not stop in time and crashes into the person.

## mission_1.variance

0.00495

## mission_2.comparison

Moving average 3 window has less max_error than median 3 windows. Moving average had 1.12 max_error while the median 3 windows are increasing gradually with the increase of weight from 1.23 to 1.54. But median has a faster response_delay than moving average and is decreasing with increasing weight. Moving average response_delay was 1.15 while median was 1.1 and decreased to 0.5.

## mission_2.fusion_choice

With same weight of 0.25, moving average has less max_error than median. Moving average max_error was 1.12 with 3 windows, 1.20 with 7 windows, and 1.21 with 11 windows while median max_error was 1.23. However median response time was faster with response_delay of 1.1 compared to the moving average response_delay which was all greater than median response_delay. Increasing the weights made the max_error bigger but decreases the response_delay.

## mission_2.manual_average

4.167

## mission_2.manual_fusion

2.25

## mission_2.manual_median

2.3

## mission_2.prediction_draft

More weight should have more error and faster reaction to big changes

## mission_2.responsiveness

Smoothing would take longer to stop if something suddenly is in the way. The robot might not stop in time and crash into a person. Responsiveness would be faster to react to something suddenly in its way. It would be more likely to stop before crashing into a person nearby.

## mission_2.selected

0

## mission_3.Assistive.prediction_draft

more readings at or bellow stop so slower to react

## mission_3.Warehouse.prediction_draft

more window so less error

## mission_3.context_comparison

Warehouse robot has more unnecessary stops and false safes when dropout bursts. Assistive robot has more unnecessary stops when it is fast approaching. The consequences of this is it makes it go slower and can block people.

## mission_3.error_costs

Warehouse robot has more unnecessary-stops and false-safes. Assistive robot constantly had 0 false_safe_rate and 0.027 unnecessary_stop_rate. Warehouse robot has a positive non zero false_safe_rate which increases when windows increased and has a constant 0.0357 unnecessary_stop_rate.

## mission_3.limitations

It doesn't establish what happens when there the area is crowded. Consult a worker or manager to know when it is crowded and when it is able to function properly.

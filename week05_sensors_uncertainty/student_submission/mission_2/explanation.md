# Mission 2

## comparison

Moving average 3 window has less max_error than median 3 windows. Moving average had 1.12 max_error while the median 3 windows are increasing gradually with the increase of weight from 1.23 to 1.54. But median has a faster response_delay than moving average and is decreasing with increasing weight. Moving average response_delay was 1.15 while median was 1.1 and decreased to 0.5.

## fusion_choice

With same weight of 0.25, moving average has less max_error than median. Moving average max_error was 1.12 with 3 windows, 1.20 with 7 windows, and 1.21 with 11 windows while median max_error was 1.23. However median response time was faster with response_delay of 1.1 compared to the moving average response_delay which was all greater than median response_delay. Increasing the weights made the max_error bigger but decreases the response_delay.

## manual_average

4.167

## manual_fusion

2.25

## manual_median

2.3

## prediction_draft

More weight should have more error and faster reaction to big changes

## responsiveness

Smoothing would take longer to stop if something suddenly is in the way. The robot might not stop in time and crash into a person. Responsiveness would be faster to react to something suddenly in its way. It would be more likely to stop before crashing into a person nearby.

## selected

0

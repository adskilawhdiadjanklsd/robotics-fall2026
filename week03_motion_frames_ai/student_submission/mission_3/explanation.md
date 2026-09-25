# Mission 3

## Ai Disclosure

I used gemini. I used it to check if I included the necessary tests and it caught some errors like putting variables in the wrong place.

## Assigned Pattern

rounded_rectangle

## Assumptions

It sets the speeds to a value within the range and calculates the the time it should take to do the long leg, short leg, and the arcs. It also assumes that positive x is moving forward and positive radians is turning left. 

## Evidence Analysis

test_my_pattern_geometry tests the first segment then checks if the segments are alternating from long length to short length so that it is making a rectangle and it also checks if the angle is 90 degrees when it has to make the round edges. 
test_my_pattern_order tests if the pattern order is correct. It should alternate from a straight line to an arc. Straight line has no angle and positive velocity. Arc has both positive angle and positive velocity.

## Live Issue

Stop decision and live motion and stop is not verified at first. I talked to the professor about this issue and he fixed it and now it is just live motion and stop that is still not verified.

## Live Pending

True

## Modifications

The generated code seems to be fine. It chose velocities that are within the limit and calculated the time it should take and in total is within the time limit.

## Original Output

AssumptionsSegment Class Structure: The existing Segment dataclass or class accepts linear_x (m/s), angular_z (rad/s), and duration (s) as its initialization parameters.Arc Kinematics: To execute a left 90-degree ($\pi/2 \text{ rad}$) turn with a radius ($R = 0.15 \text{ m}$) while respecting the maximum angular speed constraint ($\omega \le 0.80 \text{ rad/s}$), we set $\omega = 0.80 \text{ rad/s}$. The required linear speed for the arc is calculated as $v = \omega \times R = 0.80 \times 0.15 = 0.12 \text{ m/s}$ (well under the $0.22 \text{ m/s}$ limit). The duration is derived as $t = \frac{\theta}{\omega} = \frac{\pi / 2}{0.80} \approx 1.9635 \text{ seconds}$.Straight Leg Kinematics: For the straight segments ($0.40 \text{ m}$ and $0.25 \text{ m}$), we use a linear speed of $v = 0.20 \text{ m/s}$ with $\omega = 0.0 \text{ rad/s}$, yielding durations of $2.0 \text{ seconds}$ and $1.25 \text{ seconds}$ respectively.Total Duration & Limits: The sum of all segment durations is approximately $13.85 \text{ seconds}$, satisfying the strict limit of $\le 60 \text{ seconds}$ total and $\le 30 \text{ seconds}$ per segment.Implementation (pattern.py)Here is the implementation of the build_pattern function for rounded_rectangle:Pythonimport math

def build_pattern(pattern_name: str) -> list:
    """
    Constructs and returns the sequence of segments for the requested pattern name.
    """
    if pattern_name != 'rounded_rectangle':
        raise ValueError(f"Unknown pattern name: '{pattern_name}'. Expected 'rounded_rectangle'.")

    # Kinematic limits & parameters
    straight_v = 0.20  # m/s (<= 0.22 limit)
    arc_w = 0.80       # rad/s (<= 0.80 limit)
    arc_radius = 0.15  # m
    arc_v = arc_w * arc_radius  # 0.12 m/s
    
    # 90 degrees = pi / 2 radians
    arc_angle = math.pi / 2.0
    arc_duration = arc_angle / arc_w  # ~1.9635 s

    dur_040 = 0.40 / straight_v  # 2.00 s
    dur_025 = 0.25 / straight_v  # 1.25 s

    # 8 alternating segments: 4 straight legs and 4 left arcs
    segments = [
        Segment(linear_x=straight_v, angular_z=0.0, duration=dur_040),  # 1. Forward 0.40m
        Segment(linear_x=arc_v, angular_z=arc_w, duration=arc_duration),      # 2. Left arc 90°
        Segment(linear_x=straight_v, angular_z=0.0, duration=dur_025),  # 3. Forward 0.25m
        Segment(linear_x=arc_v, angular_z=arc_w, duration=arc_duration),      # 4. Left arc 90°
        Segment(linear_x=straight_v, angular_z=0.0, duration=dur_040),  # 5. Forward 0.40m
        Segment(linear_x=arc_v, angular_z=arc_w, duration=arc_duration),      # 6. Left arc 90°
        Segment(linear_x=straight_v, angular_z=0.0, duration=dur_025),  # 7. Forward 0.25m
        Segment(linear_x=arc_v, angular_z=arc_w, duration=arc_duration),      # 8. Left arc 90°
    ]
    
    return segments
Proposed TestsTo ensure robust operation and compliance with all course constraints, the following unit tests should be added to your test suite:test_rounded_rectangle_segment_count: Asserts that build_pattern('rounded_rectangle') returns exactly 8 segments.test_kinematic_constraints: Iterates through all generated segments and asserts that:$\vert{}linear\_x\vert{} \le 0.22$$\vert{}angular\_z\vert{} \le 0.80$$0 < duration \le 30.0$Total duration of all combined segments $\le 60.0$ seconds.test_unknown_pattern_raises_value_error: Asserts that passing an invalid pattern name (e.g., 'square') correctly raises a ValueError.

## Original Prompt

This is a ROS 2 Jazzy Python package. Implement only build_pattern(pattern_name: str) -> list[Segment] for 'rounded_rectangle' in the existing pattern.py.

The course-provided pattern_node.py calls this function, publishes the returned segments repeatedly through /student_cmd_vel, and sends the final zero command.

Use the existing Segment class with linear_x (m/s), angular_z (rad/s), and duration (s).

Return the ordered segments for the assigned specification and raise ValueError for an unknown pattern name.

Stay within 0.22 m/s, 0.80 rad/s, 30 seconds per segment, and 60 seconds total.

Do not replace the wrapper or course checks. Explain assumptions and propose tests.



The robot should make a rounded rectangle. The speeds must be less than or equal to 0.22 m/s and less than or equal to 0.80 rad/s. At most 30 seconds per segment and total has to be less than or equal to 60 seconds. The robot has to be within a 2 m by 2 m area. The robot should end near the starting position.

1. Move forward 0.4 m.

2. Make a left arc by turning 90 degrees while making arcs of radius 0.15 m.

3. Move forward 0.25 m.

4. Make a left arc by turning 90 degrees while making arcs of radius 0.15 m.

5. Move forward 0.4 m.

6. Make a left arc by turning 90 degrees while making arcs of radius 0.15 m.

7. Move forward 0.25 m.

8. Make a left arc by turning 90 degrees while making arcs of radius 0.15 m. 



## Original Source

import math

def build_pattern(pattern_name: str) -> list:
    """
    Constructs and returns the sequence of segments for the requested pattern name.
    """
    if pattern_name != 'rounded_rectangle':
        raise ValueError(f"Unknown pattern name: '{pattern_name}'. Expected 'rounded_rectangle'.")

    # Kinematic limits & parameters
    straight_v = 0.20  # m/s (<= 0.22 limit)
    arc_w = 0.80       # rad/s (<= 0.80 limit)
    arc_radius = 0.15  # m
    arc_v = arc_w * arc_radius  # 0.12 m/s
    
    # 90 degrees = pi / 2 radians
    arc_angle = math.pi / 2.0
    arc_duration = arc_angle / arc_w  # ~1.9635 s

    dur_040 = 0.40 / straight_v  # 2.00 s
    dur_025 = 0.25 / straight_v  # 1.25 s

    # 8 alternating segments: 4 straight legs and 4 left arcs
    segments = [
        Segment(linear_x=straight_v, angular_z=0.0, duration=dur_040),  # 1. Forward 0.40m
        Segment(linear_x=arc_v, angular_z=arc_w, duration=arc_duration),      # 2. Left arc 90°
        Segment(linear_x=straight_v, angular_z=0.0, duration=dur_025),  # 3. Forward 0.25m
        Segment(linear_x=arc_v, angular_z=arc_w, duration=arc_duration),      # 4. Left arc 90°
        Segment(linear_x=straight_v, angular_z=0.0, duration=dur_040),  # 5. Forward 0.40m
        Segment(linear_x=arc_v, angular_z=arc_w, duration=arc_duration),      # 6. Left arc 90°
        Segment(linear_x=straight_v, angular_z=0.0, duration=dur_025),  # 7. Forward 0.25m
        Segment(linear_x=arc_v, angular_z=arc_w, duration=arc_duration),      # 8. Left arc 90°
    ]
    
    return segments

## Problems

I had to check if the values are set within the range and the calculations are correct and that total time should be 60 seconds or less. 

## Saved Specification

The robot should make a rounded rectangle. The speeds must be less than or equal to 0.22 m/s and less than or equal to 0.80 rad/s. At most 30 seconds per segment and total has to be less than or equal to 60 seconds. The robot has to be within a 2 m by 2 m area. The robot should end near the starting position.
1. Move forward 0.4 m.
2. Make a left arc by turning 90 degrees while making arcs of radius 0.15 m.
3. Move forward 0.25 m. 
4. Make a left arc by turning 90 degrees while making arcs of radius 0.15 m.
5. Move forward 0.4 m.
6. Make a left arc by turning 90 degrees while making arcs of radius 0.15 m.
7. Move forward 0.25 m. 
8. Make a left arc by turning 90 degrees while making arcs of radius 0.15 m.

## Specification

The robot should make a rounded rectangle. The speeds must be less than or equal to 0.22 m/s and less than or equal to 0.80 rad/s. At most 30 seconds per segment and total has to be less than or equal to 60 seconds. The robot has to be within a 2 m by 2 m area. The robot should end near the starting position.
1. Move forward 0.4 m.
2. Make a left arc by turning 90 degrees while making arcs of radius 0.15 m.
3. Move forward 0.25 m. 
4. Make a left arc by turning 90 degrees while making arcs of radius 0.15 m.
5. Move forward 0.4 m.
6. Make a left arc by turning 90 degrees while making arcs of radius 0.15 m.
7. Move forward 0.25 m. 
8. Make a left arc by turning 90 degrees while making arcs of radius 0.15 m.

## Test Plan

Pattern behavior test should test that it has 8 segments in correct alternating order and that it is within the 2 m by 2 m area.
Velocity-limit test should test that the forward velocity is 0.22 m/s or less and angle velocity is 0.8 rad/s or less.
Stop test should test that the robot stops after the 8 segments.

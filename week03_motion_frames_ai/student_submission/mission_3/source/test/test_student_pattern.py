import os
import unittest
from week03_pattern.pattern import build_pattern
import math

class MyPatternTests(unittest.TestCase):
    def test_my_pattern_geometry(self):
        segments = build_pattern(os.environ["WEEK03_ASSIGNED_PATTERN"])
        # check segments = 8
        self.assertEqual(len(segments), 8, "Rounded rectangle must have exactly 8 segments.")
        # first segment moves about 0.4 meters with rounded to 4 decimal places
        self.assertAlmostEqual(segments[0].linear_x * segments[0].duration, 0.40, places=4)
        # check if first segment has an angle
        self.assertEqual(segments[0].angular_z, 0.0, "First segment should be a straight line.")

        # checks if alternating 0.4 and 0.25 m
        self.assertAlmostEqual(segments[0].linear_x * segments[0].duration, 0.40, places=4)
        self.assertAlmostEqual(segments[2].linear_x * segments[2].duration, 0.25, places=4)
        self.assertAlmostEqual(segments[4].linear_x * segments[4].duration, 0.40, places=4)
        self.assertAlmostEqual(segments[6].linear_x * segments[6].duration, 0.25, places=4)

        # check if angle is 90 degrees
        expected_angle = math.pi / 2
        for i in [1, 3, 5, 7]:
            self.assertAlmostEqual(segments[i].angular_z * segments[i].duration, expected_angle, places=4)

    def test_my_pattern_order(self):
        # Check another property with a known expected result.
        segments = build_pattern(os.environ["WEEK03_ASSIGNED_PATTERN"])
        # Check alternaing segments
        for i, seg in enumerate(segments):
            if i % 2 == 0:
                # needs to be a stright line
                self.assertEqual(seg.angular_z, 0.0, f"Segment {i} must be straight.")
                self.assertGreater(seg.linear_x, 0.0)
            else:
                # needs to be an arc
                self.assertGreater(seg.angular_z, 0.0, f"Segment {i} must be an arc.")
                self.assertGreater(seg.linear_x, 0.0)

        # total time needs to be less than 60 seconds
        total_duration = sum(seg.duration for seg in segments)
        self.assertLessEqual(total_duration, 60.0, "Total duration must not exceed 60 seconds.")
        
        # segment need to be within a range and run less than 30 seconds
        for i, seg in enumerate(segments):
            self.assertLessEqual(abs(seg.linear_x), 0.22, f"Segment {i} linear speed exceeds 0.22 m/s.")
            self.assertLessEqual(abs(seg.angular_z), 0.80, f"Segment {i} angular speed exceeds 0.80 rad/s.")
            self.assertLessEqual(seg.duration, 30.0, f"Segment {i} duration exceeds 30 seconds.")

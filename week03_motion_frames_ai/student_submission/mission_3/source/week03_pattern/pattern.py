"""AI-assisted motion pattern implementation.

Preserve the original AI response in Streamlit. Review it, then implement a safe
version here. The node accepts only segments returned by ``build_pattern``.
"""
from __future__ import annotations
from dataclasses import dataclass
import math

@dataclass(frozen=True)
class Segment:
    linear_x: float
    angular_z: float
    duration: float

def build_pattern(pattern_name: str) -> list[Segment]:
    """Return ordered, bounded motion segments for the assigned pattern.

    Supported assignments are ``rounded_rectangle``, ``l_path``, and
    ``alternating_arcs``. Do not include the final stop; the ROS wrapper always
    publishes it and the evaluator verifies it.
    """
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


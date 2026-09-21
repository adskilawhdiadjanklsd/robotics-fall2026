"""Mission 2 student implementation.

Complete only ``transform_camera_point`` after preserving the initial AI output
in the guide. Course tests supply both real and simulated TF buffers.
"""
from geometry_msgs.msg import PointStamped
import tf2_ros
import tf2_geometry_msgs  # Crucial for tf2 to handle PointStamped


def transform_camera_point(tf_buffer: tf2_ros.Buffer, point: PointStamped) -> PointStamped | None:
    """
    Transforms a PointStamped from the 'hall_camera' frame into 'base_link'.
    
    Args:
        tf_buffer: An active tf2_ros.Buffer instance.
        point: A geometry_msgs/msg/PointStamped message.
        
    Returns:
        The transformed PointStamped in 'base_link', or None if unavailable.
        
    Raises:
        ValueError: If the point's frame_id is not 'hall_camera'.
    """
    # 1. Enforce strict source frame validation
    if point.header.frame_id != 'hall_camera':
        raise ValueError(
            f"Invalid source frame_id: expected 'hall_camera', got '{point.header.frame_id}'"
        )
    
    target_frame = 'base_link'
    
    try:
        # 2. Transform the point using standard rclpy duration
        transformed_point = tf_buffer.transform(
            point,
            target_frame,
            timeout=__import__('rclpy').duration.Duration(seconds=0.1)
        )
        return transformed_point

    except (tf2_ros.LookupException, 
            tf2_ros.ConnectivityException, 
            tf2_ros.ExtrapolationException,
            tf2_ros.TransformException):
        # Return None gracefully if any TF exception occurs
        return None
#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import PointStamped
import tf2_ros
import tf2_geometry_msgs  # Crucial for transforming geometry_msgs via tf2


class HallwayPointTransformer(Node):

    def __init__(self):
        super().__init__('hallway_point_transformer')

        # Target frame we want to convert the point into
        self.target_frame = 'base_link'

        # Initialize TF2 buffer and listener
        self.tf_buffer = tf2_ros.Buffer()
        self.tf_listener = tf2_ros.TransformListener(self.tf_buffer, self)

        # Subscriber for the camera point (assuming PointStamped)
        self.subscription = self.create_subscription(
            PointStamped,
            '/hallway_camera/point',
            self.point_callback,
            10
        )

        # Publisher for the transformed point in base_link
        self.publisher = self.create_publisher(
            PointStamped,
            '/hallway_camera/point_base_link',
            10
        )

        self.get_logger().info('Hallway Point Transformer Node has been initialized.')

    def point_callback(self, msg: PointStamped):
        try:
            # Wait for the transform to become available (timeout after 0.1 seconds)
            # This ensures we don't drop frames if tf lags slightly
            transform = self.tf_buffer.lookup_transform(
                self.target_frame,
                msg.header.frame_id,
                rclpy.time.Time(),
                timeout=rclpy.duration.Duration(seconds=0.1)
            )

            # Transform the PointStamped into the target frame ('base_link')
            transformed_point = self.tf_buffer.transform(
                msg, 
                self.target_frame, 
                timeout=rclpy.duration.Duration(seconds=0.5)
            )

            # Publish the result
            self.publisher.publish(transformed_point)
            
            self.get_logger().debug(
                f"Transformed point from [{msg.header.frame_id}] to [{self.target_frame}]: "
                f"x={transformed_point.point.x:.2f}, y={transformed_point.point.y:.2f}, z={transformed_point.point.z:.2f}"
            )

        except (tf2_ros.LookupException, 
                tf2_ros.ConnectivityException, 
                tf2_ros.ExtrapolationException) as e:
            self.get_logger().warn(f'Could not transform point: {e}')


def main(args=None):
    rclpy.init(args=args)
    node = HallwayPointTransformer()
    
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
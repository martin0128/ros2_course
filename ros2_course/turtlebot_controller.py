import rclpy
from rclpy.node import Node
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist

class ObstacleAvoidance(Node):
    def __init__(self):
        super().__init__('obstacle_avoidance')

        # Define the desired distance to keep from obstacles
        self.desired_distance = 0.5

        # Create a publisher for the velocity command
        self.pub = self.create_publisher(Twist, '/cmd_vel', 10)

        # Subscribe to the laser scan topic
        self.sub = self.create_subscription(LaserScan, '/scan', self.scan_callback, 10)

    # Callback function for the laser scan data
    # Callback function for the laser scan data
    def scan_callback(self, data):
        # Get the range data from the laser scan
        ranges = data.ranges

        # Calculate the minimum range value
        front = min(min(ranges[:20]), min(ranges[-20:]))

        # Initialize the robot's velocity command
        cmd_vel = Twist()

        # Check if the robot is too close to an obstacle
        if front < self.desired_distance:
            # Set angular velocity to rotate
            cmd_vel.angular.z = 0.5

            cmd_vel.linear.x = 0.0
        else:
            # Set linear velocity to move forward
            cmd_vel.linear.x = 0.5
            cmd_vel.angular.z = 0.0

        # Publish the velocity command
        self.pub.publish(cmd_vel)


def main(args=None):
    rclpy.init(args=args)
    obstacle_avoidance = ObstacleAvoidance()
    rclpy.spin(obstacle_avoidance)
    obstacle_avoidance.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

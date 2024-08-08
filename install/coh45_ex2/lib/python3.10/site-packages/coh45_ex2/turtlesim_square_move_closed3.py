# this code was referenced from Beginner client library 
# tutorials in the ROS2 wiki
#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
import math

class SquareTurtleClosed(Node):

    def __init__(self):
        super().__init__('square_turtle_closed')   # this name is shown in rqt_graph
        cmd_vel_topic = 'turtle1/cmd_vel'
        pose_topic = 'turtle1/pose'
        self.publisher_ = self.create_publisher(Twist, cmd_vel_topic,  10)
        self.subscription = self.create_subscription(Pose,pose_topic,self.pose_callback,10)
        self.pose = Pose()
        self.i = 0
        self.origin_x = self.pose.x
        self.origin_y = self.pose.y
        self.state = 1 # state = side of the square


    def pose_callback(self,data):
        self.pose = data
        self.get_logger().info(f"Pose x:{data.x}, y:{data.y}, theta:{data.theta}")

        velocity_message = Twist() # create a twist message that will be published

        if (self.origin_x == 0):  #Origin is set when pose callback is called for the first time
            self.origin_x = self.pose.x
            self.origin_y = self.pose.y
            self.get_logger().info(f"Position Origin x: {self.origin_x}")
            self.get_logger().info(f"Position Origin y: {self.origin_y}")

        self.x_delta = self.pose.x - self.origin_x
        self.y_delta = self.pose.y - self.origin_y

        self.get_logger().info(f"Delta x: {self.x_delta}")
        self.get_logger().info(f"Delta y: {self.y_delta}")
        # The idea is that delta of 3 units is used as the side of the square.

        self.get_logger().info(f"Side of the square: {self.state}")

        if (self.state == 1):
            if (self.x_delta < 3):
                velocity_message.linear.x = 1.0 # move 1.0 units forward to the right
                velocity_message.linear.y = 0.0
                velocity_message.angular.z = 0.0
            elif (self.x_delta >= 3):
                velocity_message.linear.x = 0.0
                velocity_message.linear.y = 1.0
                velocity_message.angular.z = math.pi / 2
                self.state = 2 # Turn 90 degrees, only move on Y direction and move along side 2 of the square
        elif (self.state == 2):
            if (self.y_delta < 3):
                velocity_message.linear.x = 0.0 
                velocity_message.linear.y = 1.0 # move 1.0 units upwards
                velocity_message.angular.z = 0.0
            elif (self.y_delta >= 3):
                velocity_message.linear.x = -1.0 # move 1.0 units backward to the left
                velocity_message.linear.y = 0.0 
                velocity_message.angular.z = - math.pi / 2
                self.state = 3 # Turn 90 degrees, only move on X direction and move along side 3 of the square
        elif (self.state == 3):
            if (0 < self.x_delta < 4): #changed from 3 to 4
                velocity_message.linear.x = -1.0 # move 1.0 units backward to the left
                velocity_message.linear.y = 0.0
                velocity_message.angular.z = 0.0
            elif (self.x_delta <= 0):
                velocity_message.linear.x = 0.0
                velocity_message.linear.y = -1.0 # move 1.0 units downwards
                velocity_message.angular.z = - math.pi / 2
                self.state = 4 # Turn 90 degrees, only move on Y direction and move along side 4 of the square
        elif (self.state == 4):
            if (0 < self.y_delta < 4): #changed from 3 to 4
                velocity_message.linear.x = 0.0 
                velocity_message.linear.y = -1.0 # move 1.0 units upwards
                velocity_message.angular.z = 0.0
            elif (self.y_delta <= 0):
                velocity_message.linear.x = 1.0 # move 1.0 units backward to the left
                velocity_message.linear.y = 0.0 
                velocity_message.angular.z = - math.pi / 2
                self.state = 1 # Turn 90 degrees, only move on X direction and move along side 3 of the square


        self.publisher_.publish(velocity_message)
        self.get_logger().info('Move in a square')

def main(args=None):
    rclpy.init(args=args)

    square_turtle_closed = SquareTurtleClosed()

    rclpy.spin(square_turtle_closed)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    square_turtle_closed.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
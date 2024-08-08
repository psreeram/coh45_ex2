# this code was referenced from Beginner client library 
# tutorials in the ROS2 wiki
#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist, Pose
from turtlesim.msg import Pose
from math import radians

class SquareTurtle(Node):
    def __init__(self):
        super().__init__('square_turtle')

        self.publisher_ = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        self.subscriber_ = self.create_subscription(Pose, '/turtle1/pose', self.pose_callback, 10)

        self.state = 1  # Initial state
        self.x_increment = 0.1
        self.y_increment = 0.0
        self.angle = radians(0)
        self.angle_state = 0

    def pose_callback(self, msg):
        x = msg.x
        y = msg.y

        if self.state == 1:  # Side 1
            if x > 8:
                self.state = 2
                self.x_increment = 0.0
                self.y_increment = 0.1
                if self.angle_state == 0:
                    self.angle = radians(90)  # 90 degrees in radians
                    self.angle_state == 1
                self.move(self.x_increment, self.y_increment)
            else:
                self.move(self.x_increment, self.y_increment)

        elif self.state == 2:  # Side 2
            if y > 8:
                self.state = 3
                self.x_increment = -0.1
                self.y_increment = 0.0
                self.angle = radians(180)  # 270 degrees in radians
                self.move(self.x_increment, self.y_increment)
            else:
                self.move(self.x_increment, self.y_increment)

        elif self.state == 3:  # Side 3
            if x < 2:
                self.state = 4
                self.x_increment = 0.0
                self.y_increment = -0.1
                self.angle = radians(270)  # 270 degrees in radians
                self.move(self.x_increment, self.y_increment)
            else:
                self.move(self.x_increment, self.y_increment)

        elif self.state == 4:  # Side 4
            if y < 2:
                self.state = 1
                self.x_increment = 0.1
                self.y_increment = 0.0
                self.angle = radians(0)  # 90 degrees in radians
                self.move(self.x_increment, self.y_increment)
            else:
                self.move(self.x_increment, self.y_increment)

    def move(self, x_vel, y_vel):
        msg = Twist()
        msg.linear.x = x_vel
        msg.linear.y = y_vel
        msg.angular.z = self.angle
        self.publisher_.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    square_turtle = SquareTurtle()
    rclpy.spin(square_turtle)
    rclpy.shutdown()

if __name__ == '__main__':
    main()

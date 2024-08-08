# this code was referenced from Beginner client library 
# tutorials in the ROS2 wiki
#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
from math import radians


class TurtlesimNodeSquareMoveClosed(Node):

    def __init__(self):
        super().__init__('turtlesim_node_square_move_closed')   # this name is shown in rqt_graph
        cmd_vel_topic = 'turtle1/cmd_vel'
        pose_topic = 'turtle1/pose'
        self.publisher_ = self.create_publisher(Twist, cmd_vel_topic,  10)
        self.subscription = self.create_subscription(Pose,pose_topic,self.pose_callback,10)
        self.pose = Pose()
        timer_period = 1.0  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0

    def timer_callback(self):
        
        velocity_message = Twist() # create a twist message that will be published
        #this message will move turtlesim forward in X direction alone by 1 unit every 0.5 seconds 
        # and turn by 90 degrees giving the net effect of a cicrle
                
        
        self.get_logger().info(f"Position x: {round(self.pose.x)}")
        self.get_logger().info(f"Position y: {round(self.pose.y)}")
        if (5 <= self.pose.x <= 8 and self.pose.y == 6):
            velocity_message.linear.x = 1.0
        elif (self.pose.x > 8 and self.pose.y == 6):
            velocity_message.linear.y = 1.0
            velocity_message.angular.z = radians(90)
        elif (self.pose.x > 8 and 6 < self.pose.y <= 8):
            velocity_message.linear.y= 1.0
        elif (self.pose.x > 8 and self.pose.y > 8):
            velocity_message.linear.x = -1.0
            velocity_message.angular.z = radians(90)
        elif (5 <= self.pose.x <= 8 and self.pose.y > 8):
            velocity_message.linear.x = -1.0
        else:  
            velocity_message.linear.x = -1.0
         
        self.publisher_.publish(velocity_message)
        self.get_logger().info('Move in a square using closed loop')
        self.i += 1

    def pose_callback(self,data):
        self.pose = data



def main(args=None):
    rclpy.init(args=args)

    turtlesim_node_square_move_closed = TurtlesimNodeSquareMoveClosed()

    rclpy.spin(turtlesim_node_square_move_closed)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    turtlesim_node_square_move_closed.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
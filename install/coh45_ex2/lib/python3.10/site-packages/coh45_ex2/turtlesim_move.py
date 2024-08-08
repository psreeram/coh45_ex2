# this code was referenced from Beginner client library 
# tutorials in the ROS2 wiki
#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist


class TurtlesimNode1(Node):

    def __init__(self):
        super().__init__('turtlesim_node_1')   # this name is shown in rqt_graph
        cmd_vel_topic = 'turtle1/cmd_vel'
        self.publisher_ = self.create_publisher(Twist, cmd_vel_topic,  10)
        timer_period = 0.5  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0

    def timer_callback(self):
        
        velocity_message = Twist() # create a twist message that will be published
        #this message will move turtlesim forward in X direction alone by 1 unit every 0.5 seconds
        velocity_message.linear.x = 1.0 
        self.publisher_.publish(velocity_message)
        self.get_logger().info('Move forward by 1.0 unit')
        self.i += 1


def main(args=None):
    rclpy.init(args=args)

    turtlesim_node_1 = TurtlesimNode1() 

    rclpy.spin(turtlesim_node_1)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    turtlesim_node_1.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
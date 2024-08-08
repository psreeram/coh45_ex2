# this code was referenced from Beginner client library 
# tutorials in the ROS2 wiki
# Gemini suggestions where also used
#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from coh45_ex2.turtlesim_circle_move import TurtlesimNodeDrawCircle # Circle move implementation - Open loop
from coh45_ex2.turtlesim_square_move import TurtlesimNodeSquareMove # Square move implementation - Open loop
from coh45_ex2.turtlesim_triangle_move import TurtlesimNodeTriangleMove # Triangle move implementation - Open loop
from coh45_ex2.turtlesim_square_move_closed3 import SquareTurtleClosed # Square move implementation - Closed loop

class UserShapeMoveNode(Node):

    def __init__(self):
        super().__init__('user_shape_move_node') #this name is shown in rqt_graph

        self.available_options = ["Square","Circle","Triangle","Square Closed loop"]


        def get_user_input(shape_options):
            # Prompts the user to choose from the list of shape options.
            # Args: A list of strings representing the available options
            # Returns: The user's chosen options as a string.
        
            while True:
                print("Please choose an option: (e.g. 2)")
                for i, option in enumerate(shape_options, start=1):
                    print(f"{i}. {option}")

                user_choice = input("Enter your choice of how you want turtlesim to move: ")
                try:
                    user_choice_int = int(user_choice)
                    if 1 <= user_choice_int <= len(shape_options):
                        return shape_options[user_choice_int-1]
                    else:
                        print("Invalid choice. Please enter a number betweeb 1 and ", len(shape_options))
                except ValueError:
                    print("Invalid input. Please enter a number.")

        while True:
            chosen_shape = get_user_input(self.available_options)
            # Based on the chosen shape, instantiate that shape node for the movement
            if (chosen_shape == 'Circle'):
                circle_node = TurtlesimNodeDrawCircle()
                rclpy.spin(circle_node)
                break
            elif (chosen_shape == 'Square'):
                square_node = TurtlesimNodeSquareMove()
                rclpy.spin(square_node)
                break
            elif (chosen_shape == 'Triangle'):
                triangle_node = TurtlesimNodeTriangleMove()
                rclpy.spin(triangle_node)
                break
            elif (chosen_shape == 'Square Closed loop'):
                square_closed_node = SquareTurtleClosed()
                rclpy.spin(square_closed_node)
                break
            else:
                print("Invalid input")


def main(args=None):
    rclpy.init(args=args)

    user_input_node = UserShapeMoveNode()

    rclpy.spin(user_input_node)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    user_input_node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()



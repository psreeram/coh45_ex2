from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    user_input_node = Node(
        package='coh45_ex2',
        executable='user_input_node',
        name='user_input_node'
    )
    return LaunchDescription([
        user_input_node
    ])
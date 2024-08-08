from setuptools import find_packages, setup

# added to handle launch files
from glob import glob
import os

package_name = 'coh45_ex2'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'),  # added to handle launch files
        glob(os.path.join('launch', '*launch.[pxy][yma]*'))) # added to handle launch files
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Sree',
    maintainer_email='psreeram@gmail.com',
     description='Examples done in Rigbetellabs ROS2 program',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'turtlesim_node_1 = coh45_ex2.turtlesim_move:main',
            'turtlesim_node_draw_circle = coh45_ex2.turtlesim_circle_move:main',
            'turtlesim_node_square_move = coh45_ex2.turtlesim_square_move:main',
            'turtlesim_node_triangle_move = coh45_ex2.turtlesim_triangle_move:main',
            'square_turtle_closed = coh45_ex2.turtlesim_square_move_closed3:main',
            'user_input_node = coh45_ex2.userinput:main'
        ],
    },
)

Problem statement for Exercise 2:

Ex 2A - create a Node that will move the turtle ( in any direction ) | it should displace from its original position <br>
Ex 2B - create a Node that will move the turtle to create a SQUARE , TRIANGLE , 5 POINTER STAR | VIA OPEN LOOP | VIA CLOSED LOOP <br>
Ex 2C - create a small application where User will give inputs to draw a shape | all nodes to be started via launch file 


Ex2A: Solution: THis is addressed in the python file turtlesim_move.py

Ex2B: Solution: This is partially achieved in the following python files:<br>
a) Movement along a square (open loop - which means without any feedback loop) - turtlesim_square_move.py<br>
b) Movement along a circle (open loop - which means without any feedback loop) - turtlesim_circle_move.py<br>
c) Movement along a triangle (open loop - which means without any feedback loop) - turtlesim_triangle_move.py<br>
d) Movement along a 5 Pointer Star - not coded<br>
e) Movement along a square (closed loop - which means with feedback using the Pose message) - turtlesim_square_move_closed3.py<br>
f) Movement along a Circle / Triangle (closed loop) - not coded<br>


Ex 2C: Solution: THis is addressed in the python file userinput.py<br>
- this internally instantiates the nodes from a), b), c), e) from Ex2B<br>
- currently launch file is not working.


Video of Ex 2C : User input given as square and then turtlebot moving in a square<br>
![Watch the video](https://raw.githubusercontent.com/username/repository/branch/path/to/video.mp4)

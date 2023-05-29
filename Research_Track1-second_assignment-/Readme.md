### [Research_Track_1](https://unige.it/enoff.f/2021/ins/51201.html?codcla=10635),[Robotics Engineering](https://courses.unige.it/10635)([UNIGE](https://unige.it/it/)) : Second assignment

### Professor. [Carmine Recchiuto](https://github.com/CarmineD8)

The second assignment of research track 1 course is about the use of a robot simulator in ROS. 

The tasks for this assignment are to move the robot in the environment to the goal position that chosen by user.
In this assignment we are using operator ROS custom messages, costum services, and actions. Also graphical interfaces (Rviz and Gazebo) was using the to view the robot's simulation.
It is also required to create a launch file to start the simulation.

The new package was built alongside the package assignment_2_2022.
The task of this assignment was to implement four new nodes in the robot simulation:


*	A node that implements an action client and enables users to set or cancel targets (x, y)or to cancel it.
* A node that using the values posted on the topic, publish the robot's position and speed as a custom message(x,y, vel_x, vel_z), by relying on the values published on the topic /odom.
* A service node that prints the quantity of goals reached and canceled upon call;
* A node that prints the robot's average speed and distance from the target while subscribing to the robot's position and velocity using a custom message. 
To control how quickly the node broadcasts the data, use a parameter.

The Robot environment
---------
![Tux, the Linux mascot](/image/environment.png)

The Robot 
---------
![Tux, the Linux mascot](/image/Robot.png)

Installing and running
----------------------
you have installed ROS and created your workspace you have to download the package second_assignment in the src folder of your workspace.

Run the following command from the shell:
```bash
$ git clone https://github.com/CarmineD8/assignment_2_2022.git
```
Run the following command from the shell:\
```bash
$ git clone https://github.com/ArghavanDalvand/Research_Track1-second_assignment-.git
```
Then you have to run:
IMPORTANT: be sure to run the command above in the root folder of your workspace
```bash
$ catkin_make #properly build the workspace
```
In this state we can run the code thanks to the launch file you can simply run all the nodes using the command:
```bash
$ roslaunch second_assignment_rt1 second_assignment_rt1.launch
```

Flowchart
----------------------
![Tux, the Linux mascot](/image/FlowChart.png)

rqt_graph command
----------------------
The rqt_graph command provides a GUI plugin for visualizing the ROS computation graph. 
It is useful to have an immediate comprehension of how nodes and related topics work together.
In this case, the resulting graph is fairly simple because there are only four nodes (represented as elliptical boxes) and two topics (represented as rectangular boxes). 
To visualize the graph, you only need to run:
```bash
$ rqt_graph
```
NOTE: this command works properly only if all nodes are running}

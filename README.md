# dual_panda_sim
Customizable panda simulation world on gazebo with three objects, *"rod"*, *"stone"* and a *"box"* along with two franka emika panda arms. 

# Abstract

A python script is designed to inquire about the selection of the object along with the dimensions required by the user, to initate a gazebo simulation of the respective object with two panda arms. After the official installation of the franka emika, ros noetic in a ubuntu environment verison 20.04. Store the folder *"run_sim_py"* in the *"franka_gazebo"* folder and contents of repository's *"models"* folder to the *"models"* folder present in the *"franka_gazebo"*.
![workflow](https://github.com/aakarsh1011/dual_panda_sim/blob/main/images/workflow.png "workflow")



# Installation of Franka kernel

The official franka kernel installation steps can be found here https://frankaemika.github.io/docs/installation_linux.html

# Process

After the sucessful installation of the franka kernel, navigate to the *run_sim_py* folder and run the *main.py* script and follow the instructions


# Images 

Running *main.py*
![terminal](https://github.com/aakarsh1011/dual_panda_sim/blob/main/images/python_script1.png "Initiating the python scrpt")

Choosing the object and dimensions
![terminal](https://github.com/aakarsh1011/dual_panda_sim/blob/main/images/python_script2.png "Choosing the object and dimensions")

Input has to be provided, if notthing to providing. please use the default values mentioned in the output.

Three windows will be started
1. Gazebo simulation
2. Rviz window for each franka emika arm. 

## Box
![image of box in simulation](https://github.com/aakarsh1011/dual_panda_sim/blob/main/images/box.png "box")

## Rod
![image of rod in simulation](https://github.com/aakarsh1011/dual_panda_sim/blob/main/images/rod.png "rod")

The orientation of the rod can be adjusted by changing the *<pose>* tag present in the *franka_gazebo/models/rod/model_template.sdf*, present under *<link name='link'>*

## Stone
![image of stone in simulation](https://github.com/aakarsh1011/dual_panda_sim/blob/main/images/stone.png "stone")

# rosgraphs and workflow

Here you can take a look at the rosgraph of all the topics and nodes that are being used while the simulation is running
![nodes and topics graph](https://github.com/aakarsh1011/dual_panda_sim/blob/main/images/node_and_topics.png "nodes and topics")

Here is another compact view of just the nodes currently running 
![nodes graph](https://github.com/aakarsh1011/dual_panda_sim/blob/main/images/nodes.png "nodes only")

# Current status
Motion planning of each hand 

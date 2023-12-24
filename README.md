# dual_panda_sim
Customizable panda simulation world on gazebo with three objects, *"rod"*, *"stone"* and a *"box"* along with two franka emika panda arms. 

# Workflow

A python script is designed to inquire about the selection of the object along with the dimensions required by the user, to initate a gazebo simulation of the respective object with two panda arms. After the official installation of the franka emika, ros noetic in a ubuntu environment verison 20.04. Store the folder *"run_sim_py"* in the *"franka_gazebo"* folder and contents of repository's *"models"* folder to the *"models"* folder present in the *"franka_gazebo"*.

# Installation of Franka kernel

The official franka kernel installation steps can be found here https://frankaemika.github.io/docs/installation_linux.html

# Process

After the sucessful installation of the franka kernel, navigate to the *run_sim_py* folder and run the *main.py* script and follow the instructions


# Images 

Running *main.py*
![alt text](https://github.com/aakarsh1011/dual_panda_sim/images/python_script1.png "Initiating the python scrpt")

Choosing the object and dimensions
![alt text](https://github.com/aakarsh1011/dual_panda_sim/images/python_script2.png "Choosing the object and dimensions")

Input has to be provided, if notthing to providing. please use the default values mentioned in the output.

Three windows will be started
1. Gazebo simulation
2. Rviz window for each franka emika arm. 

## Box
![alt text](https://github.com/aakarsh1011/dual_panda_sim/images/box.png "box")

## Rod
![alt text](https://github.com/aakarsh1011/dual_panda_sim/images/rod.png "rod")

The orientation of the rod can be adjusted by changing the *<pose>* tag present in the *franka_gazebo/models/rod/model_template.sdf*, present under *<link name='link'>*

## Stone
![alt text](https://github.com/aakarsh1011/dual_panda_sim/images/stone.png "stone")


# Current status
Motion planning of each hand 

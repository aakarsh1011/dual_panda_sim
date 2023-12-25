# main_script.py
import os
import subprocess

from box_edit import customize_box_model
from rod_edit import customize_rod_model
from stone_edit import customize_stone_model

def main():
    print("Choose an object to spawn:")
    print("1. box")
    print("2. rod")
    print("3. stone")

    choice = input("Enter your choice (1/2/3): ")

    if choice == '1': #### BOX ####
        print("box expects four inputs.")
        print("Default values m = 0.1, x = 0.1, y = 0.1, z = 0.1")
        mass = float(input("Enter Mass: "))
        dim_x = float(input("Enter Dimension X: "))
        dim_y = float(input("Enter Dimension Y: "))
        dim_z = float(input("Enter Dimension Z: "))
        model_dimensions = [dim_x,dim_y,dim_z]

        # change as per your location
        template_path = "/home/aakarsh/project/catkin_ws/src/franka_ros/franka_gazebo/models/box/model_template.sdf"
        output_path = "/home/aakarsh/project/catkin_ws/src/franka_ros/franka_gazebo/models/box/model.sdf"
        roslaunch_command = "roslaunch franka_gazebo panda_co_op.launch " \
        "world:=$(rospack find franka_gazebo)/world/box.sdf " \
            "controller:=cartesian_impedance_example_controller " \
                "rviz:=false"

        # Customize the model
        customize_box_model(template_path, output_path, mass, model_dimensions)

    elif choice == '2': #### ROD ####
        print("rod expects three inputs.")
        print("Default values m = 0.1, radius = 0.01, length = 0.2")
        mass = float(input("Enter Mass: "))
        radius = float(input("Enter Radius: "))
        length = float(input("Enter Length: "))
        

        # change as per your location
        template_path = "/home/aakarsh/project/catkin_ws/src/franka_ros/franka_gazebo/models/rod/model_template.sdf"
        output_path = "/home/aakarsh/project/catkin_ws/src/franka_ros/franka_gazebo/models/rod/model.sdf"
        roslaunch_command = "roslaunch franka_gazebo panda_co_op.launch " \
        "world:=$(rospack find franka_gazebo)/world/rod.sdf " \
            "controller:=cartesian_impedance_example_controller " \
                "rviz:=false"

        # Customize the model
        customize_rod_model(template_path, output_path, mass, radius, length)

    elif choice == '3': #### STONE ####
        print("stone expects four inputs.")
        print("Default values m = 0.1024, x = 0.025, y = 0.032, z = 0.064")
        mass = float(input("Enter Mass: "))
        dim_x = float(input("Enter Dimension X: "))
        dim_y = float(input("Enter Dimension Y: "))
        dim_z = float(input("Enter Dimension Z: "))
        model_dimensions = [dim_x,dim_y,dim_z]

        # change as per your location
        template_path = "/home/aakarsh/project/catkin_ws/src/franka_ros/franka_gazebo/models/stone/model_template.sdf"
        output_path = "/home/aakarsh/project/catkin_ws/src/franka_ros/franka_gazebo/models/stone/model.sdf"
        roslaunch_command = "roslaunch franka_gazebo panda_co_op.launch " \
        "world:=$(rospack find franka_gazebo)/world/stone.sdf " \
            "controller:=cartesian_impedance_example_controller " \
                "rviz:=false"

        # Customize the model
        customize_stone_model(template_path, output_path, mass, model_dimensions)
        

    else:
        print("Invalid choice. Exiting.")


    # Run the roslaunch command
    subprocess.run(roslaunch_command, shell=True)

if __name__ == "__main__":
    main()

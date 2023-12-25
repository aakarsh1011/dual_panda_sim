import os
import subprocess

from box_edit import customize_box_model
from rod_edit import customize_rod_model
from stone_edit import customize_stone_model

def main():
    # User prompt for choosing an object to spawn
    print("Choose an object to spawn:")
    print("1. box")
    print("2. rod")
    print("3. stone")

    # Get user input for the chosen object
    choice = input("Enter your choice (1/2/3): ")

    # Get the base directory of the script
    base_dir = os.path.dirname(os.path.abspath(__file__))
    # Define the directory where the models are stored relative to the base directory
    model_dir = os.path.join(base_dir, "../models")  # Adjust this path based on your project structure

    if choice == '1':  # BOX
        # User instructions and input gathering for box parameters
        print("box expects four inputs.")
        print("Default values m = 0.1, x = 0.1, y = 0.1, z = 0.1")
        mass = float(input("Enter Mass: "))
        dim_x = float(input("Enter Dimension X: "))
        dim_y = float(input("Enter Dimension Y: "))
        dim_z = float(input("Enter Dimension Z: "))
        model_dimensions = [dim_x, dim_y, dim_z]

        # Define paths for box model template and output, and the roslaunch command
        template_path = os.path.join(model_dir, "box/model_template.sdf")
        output_path = os.path.join(model_dir, "box/model.sdf")
        roslaunch_command = f"roslaunch franka_gazebo panda_co_op.launch " \
                             f"world:=$(rospack find franka_gazebo)/world/box.sdf " \
                             f"controller:=cartesian_impedance_example_controller " \
                             f"rviz:=false"

        # Customize the box model
        customize_box_model(template_path, output_path, mass, model_dimensions)

    elif choice == '2':  # ROD
        # User instructions and input gathering for rod parameters
        print("rod expects three inputs.")
        print("Default values m = 0.1, radius = 0.01, length = 0.2")
        mass = float(input("Enter Mass: "))
        radius = float(input("Enter Radius: "))
        length = float(input("Enter Length: "))

        # Define paths for rod model template and output, and the roslaunch command
        template_path = os.path.join(model_dir, "rod/model_template.sdf")
        output_path = os.path.join(model_dir, "rod/model.sdf")
        roslaunch_command = f"roslaunch franka_gazebo panda_co_op.launch " \
                             f"world:=$(rospack find franka_gazebo)/world/rod.sdf " \
                             f"controller:=cartesian_impedance_example_controller " \
                             f"rviz:=false"

        # Customize the rod model
        customize_rod_model(template_path, output_path, mass, radius, length)

    elif choice == '3':  # STONE
        # User instructions and input gathering for stone parameters
        print("stone expects four inputs.")
        print("Default values m = 0.1024, x = 0.025, y = 0.032, z = 0.064")
        mass = float(input("Enter Mass: "))
        dim_x = float(input("Enter Dimension X: "))
        dim_y = float(input("Enter Dimension Y: "))
        dim_z = float(input("Enter Dimension Z: "))
        model_dimensions = [dim_x, dim_y, dim_z]

        # Define paths for stone model template and output, and the roslaunch command
        template_path = os.path.join(model_dir, "stone/model_template.sdf")
        output_path = os.path.join(model_dir, "stone/model.sdf")
        roslaunch_command = f"roslaunch franka_gazebo panda_co_op.launch " \
                             f"world:=$(rospack find franka_gazebo)/world/stone.sdf " \
                             f"controller:=cartesian_impedance_example_controller " \
                             f"rviz:=false"

        # Customize the stone model
        customize_stone_model(template_path, output_path, mass, model_dimensions)

    else:
        print("Invalid choice. Exiting.")

    subprocess.run(roslaunch_command, shell=True)

if __name__ == "__main__":
    main()

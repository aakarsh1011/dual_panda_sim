import os

def customize_stone_model(template_path, output_path, mass, dimensions):
    # Read the template SDF file
    with open(template_path, 'r') as file:
        template_content = file.read()

    print(template_path)

    # Replace placeholders with actual values
    customized_content = template_content.replace('{{MASS}}', str(mass))
    customized_content = customized_content.replace('{{DIM_X}}', str(dimensions[0]))
    customized_content = customized_content.replace('{{DIM_Y}}', str(dimensions[1]))
    customized_content = customized_content.replace('{{DIM_Z}}', str(dimensions[2]))

    # Save the customized SDF file
    with open(output_path, 'w') as file:
        file.write(customized_content)


    print(f"Customized SDF file saved to: {output_path}")


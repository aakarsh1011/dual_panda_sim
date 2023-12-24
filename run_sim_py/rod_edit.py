import os

def customize_rod_model(template_path, output_path, mass, radius,length):
    # Read the template SDF file
    with open(template_path, 'r') as file:
        template_content = file.read()

    # Replace placeholders with actual values
    customized_content = template_content.replace('{{MASS}}', str(mass))
    customized_content = customized_content.replace('{{RADIUS}}', str(radius))
    customized_content = customized_content.replace('{{LENGTH}}', str(length))
    

    # Save the customized SDF file
    with open(output_path, 'w') as file:
        file.write(customized_content)


    print(f"Customized SDF file saved to: {output_path}")



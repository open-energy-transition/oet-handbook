import os
import random
import string

def random_string(length=10):
    # Generate a random string of fixed length
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))

def create_folder_with_files(path, folder_name, position):
    # Create a new directory
    new_path = os.path.join(path, folder_name)
    os.makedirs(new_path, exist_ok=True)

    # Create index.mdx with specific content
    index_content = f"""---
sidebar_position: {position}
sidebar_label: {folder_name}
sidebar_class_name: green
---
import DocCardList from '@theme/DocCardList';

# Engineering

## teeeeemp

At our company, we are committed to providing a safe and inclusive workplace for all employees. This policy outlines our expectations for behavior and conduct in the workplace.

## Code of Conduct

All employees are expected to adhere to the following code of conduct:

- Treat all colleagues with respect and professionalism
- Avoid any behavior that could be considered discriminatory or harassing
- Maintain confidentiality of company and client information
- Follow all company policies and procedures
- Report any violations of this code of conduct to management

## Work Hours

Employees are expected to work their designated hours as outlined in their employment contract. Any changes to work hours must be approved by management in advance.

## Remote Work

Employees may be permitted to work remotely on a case-by-case basis, subject to approval by management. Remote work arrangements must be agreed upon in writing and may be subject to periodic review.

## Social Media

Employees are expected to use social media responsibly and in a manner that does not reflect poorly on the company. Any posts or comments that could be considered offensive or inappropriate may result in disciplinary action.

## Conclusion

We take our commitment to providing a safe and inclusive workplace seriously. Any violations of this policy may result in disciplinary action, up to and including termination of employment.
<DocCardList />
"""
    with open(os.path.join(new_path, 'index.mdx'), 'w') as file:
        file.write(index_content)

    # Create a random named .md file with basic content
    random_md_filename = random_string(8) + '.md'
    md_content = """

# Engineering

## teeeeemp

At our company, we are committed to providing a safe and inclusive workplace for all employees. This policy outlines our expectations for behavior and conduct in the workplace.

## Code of Conduct

All employees are expected to adhere to the following code of conduct:

- Treat all colleagues with respect and professionalism
- Avoid any behavior that could be considered discriminatory or harassing
- Maintain confidentiality of company and client information
- Follow all company policies and procedures
- Report any violations of this code of conduct to management

## Work Hours

Employees are expected to work their designated hours as outlined in their employment contract. Any changes to work hours must be approved by management in advance.

## Remote Work

Employees may be permitted to work remotely on a case-by-case basis, subject to approval by management. Remote work arrangements must be agreed upon in writing and may be subject to periodic review.

## Social Media

Employees are expected to use social media responsibly and in a manner that does not reflect poorly on the company. Any posts or comments that could be considered offensive or inappropriate may result in disciplinary action.

## Conclusion

We take our commitment to providing a safe and inclusive workplace seriously. Any violations of this policy may result in disciplinary action, up to and including termination of employment.

"""
    
    with open(os.path.join(new_path, random_md_filename), 'w') as file:
        file.write(md_content)

def main():
    path = '/home/akshat/oet-handbook/docs'  # Change to your desired path
    num_folders = 25  # Number of folders to create
    start_position = 5  # Starting position for sidebar

    for i in range(num_folders):
        folder_name = random_string()
        create_folder_with_files(path, folder_name, start_position + i)

if __name__ == "__main__":
    main()

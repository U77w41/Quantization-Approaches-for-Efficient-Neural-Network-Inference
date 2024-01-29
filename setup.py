# Run this py file before to download the requirement files
# import subprocess

# def install_libraries(requirements_file):
#     with open(requirements_file, 'r') as file:
#         libraries = [line.strip() for line in file.readlines() if line.strip()]

#     for library in libraries:
#         subprocess.call(['pip', 'install', library])

# if __name__ == "__main__":
#     # Installing the requirements
#     requirements_file = "requirements.txt"
#     install_libraries(requirements_file)

import os

# Directories needed
dirs = [
    os.path.join("data", "raw"),
    os.path.join("data","processed"),
    "docs",
    "references",
    "reports",
    "notebooks",
    "saved_models",
    "src"
]

# Create the directories and write a .gitkeep file inside each directory (we cannot commit an empty directory in git)
for dir in dirs:
    os.makedirs(dir , exist_ok=True)
        

files = ['params.yaml',
        '.gitignore', # Here we push all the files which we dont want to push into git
        'requirements.txt',
        os.path.join('src' , '__init__.py' ),
        os.path.join('notebooks', 'quantization_tutorial.ipynb')]

# Creating the params and gitignore files
for file_ in files:
    with open(file_, "w") as f:
        pass
    
# Adding the .gitkeep files to the empty directories
for dir in dirs:
    if not os.listdir(dir):
        with open(os.path.join(dir, '.gitkeep'), 'w') as f:
            pass
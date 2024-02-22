# Import the necessary modules.
from setuptools import setup, find_packages
from typing import List

# Define a constant for the hyphen-e-dot string.
HYPHEN_E_DOT = '-e .'

# Define a function to get the list of requirements from a requirements file.
def get_requirements(file_path:str)->List[str]:
    """
    this function will return a list of requirements 
    """
    # Initialize an empty list to store the requirements.
    requirements = []
    # Open the specified file_path
    with open(file_path) as file_obj:
        # Read the lines from the requirements file.
        requirements = file_obj.readlines()
        # Remove the newline characters from the requirements.
        requirements = [req.replace("\n", "") for req in requirements]

        # Remove the hyphen-e-dot string from the requirements list if it exists.
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    # Return the list of requirements.
    return requirements

setup(
    name = 'My_ml_project', # Specify the name of the project
    version = '0.1',  # Specify the version of the project
    author = 'Minich', # Specify the author of the project
    author_email = 'minichworks@gmail.com', # Specify the email of the author
    description = 'A machine learning project for predicting employee perfomance', # Specify the description of the project
    packages = find_packages(),  # Automatically find packages in the project directory
    # install_requires = [
    #     'numpy',
    #     'pandas',
    #     'seaborn',
    #     'scikit-learn',
    #  # Add more dependecies if you have them
    # ]
    # You will be working with many libraries and it is not feasible to include all here. That's why we included the txt file
    
    # Specify the dependencies required for the project by parsing a requirements file
    install_requires = get_requirements('requirements.txt')

)
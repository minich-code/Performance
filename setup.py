from setuptools import setup, find_packages
from typing import List

HYPHEN_E_DOT = '-e .'


def get_requirements(file_path:str)->List[str]:
    """
    this function will return a list of requirements 
    """

    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    
    return requirements

setup(
    name = 'My_ml_project',
    version = '0.1',
    author = 'Minich',
    author_email = 'minichworks@gmail.com',
    description = 'A machine learning project for predicting employee perfomance',
    packages = find_packages(),
    # install_requires = [
    #     'numpy',
    #     'pandas',
    #     'seaborn',
    #     'scikit-learn',
    #  # Add more dependecies if you have them
    # ]
    # You will be working with many libraries and it is not feasible to include all here. That's why we included the txt file
    install_requires = get_requirements('requirements.txt')

)
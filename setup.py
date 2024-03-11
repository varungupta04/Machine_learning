from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT='-e .'
#this is cause of -e. is the trigger of the setup.py

def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
            #this is for the -e. being the trigger for running the code
    
    return requirements

setup(
    name = 'mlproj',
    version = '0.0.1',
    author = 'Varun',
    author_email = 'varunguptaa004@gmail.com',
    packages = find_packages(),
    # install_requires = ['pandas', 'numpy' , 'seaborn']
    # Can not write too many imports in this manner
    install_requires = get_requirements('requirements.txt')
)
from setuptools import find_packages, setup
from typing import List
def get_requirements(file_path:str)->List[str]:
    '''
    this fucntion will return the list of requirements

    '''
    requirements=[]
    HYPN='-e .'
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace('\n','') for req in requirements]
        if HYPN in requirements:
            requirements.remove(HYPN)
    return requirements

setup(
    name='project1',
    version='0.0.1',
    author='Himesh',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)
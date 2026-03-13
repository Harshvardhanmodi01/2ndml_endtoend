from setuptools import find_packages,setup
from typing import List
hypen = '-e .'
def get_requirements(file_path:str)->List[str]:
    '''this funtion will return the list of requirements'''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]
        if hypen in requirements:
            requirements.remove(hypen)
    return requirements
setup(
    name='mlproject',
    version='0.1',
    author='harshjain',
    author_email='jainharshvardhan11@gmail.com',
    package=find_packages(),
    install_requires=get_requirements('requirements.txt')
)
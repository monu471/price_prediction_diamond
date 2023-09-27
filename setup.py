from setuptools import setup,find_packages
from typing import *
file_name = "requirements.txt"
hyphon_dot = "-e ."

def get_requirements():
    with open(file_name,"r") as f:
        data = f.readlines()
    data = [content.replace('\n',"") for content in data] 
    if hyphon_dot  in data:
        data.remove(hyphon_dot) 
    return data
      

setup(name = "src",
      author="monujoshi",
      author_email="monujoshi471@gmail.com",
      install_requires = get_requirements(),
      packages= find_packages()
)
import yaml
import os
import pathlib

def read_yaml(path_to_yml:str)->dict:
    with open(path_to_yml) as yamlfile:
        content = yaml.safe_load(yamlfile)

    return content

def create_dir(dirs:list):
    for dir_path in dirs:
        os.makedirs(dir_path, exist_ok=True)
        print(f'The directory is created at {dir_path}')







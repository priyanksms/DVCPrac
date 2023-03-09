import yaml
import os

def read_yaml(path_to_yml:str)->dict:
    with open(path_to_yml) as yamlfile:
        content = yaml.safe_load(yamlfile)

    return content




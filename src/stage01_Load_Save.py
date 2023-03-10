from src.utils.ultility_Methods import read_yaml, create_dir
import pathlib
import argparse
import pandas as pd
import sys
import os

rootpath = pathlib.Path(__file__).parent.parent.as_posix()
config_path = rootpath+'/config/config.yaml'
print(rootpath)


def get_data(config_path):
    config = read_yaml(config_path)

    remote_data_path = config['data_source']
    df = pd.read_csv(remote_data_path, sep=';')

    artifacts_dir = config['artifacts']['artifacts_dir']
    raw_local_dir = config['artifacts']['raw_local_dir']
    raw_local_file = config['artifacts']['raw_local_file']
    raw_local_dir_path = rootpath+'/'+artifacts_dir+'/'+raw_local_dir
    raw_local_file_path = raw_local_dir_path+'/'+raw_local_file



   ## print('path = ' + pathlib.PosixPath(artifacts_dir,raw_local_dir))
   ## print('path = '+os.path.join(artifacts_dir,raw_local_dir))


    print(artifacts_dir)
    print(raw_local_dir)
    print(raw_local_file)
    print(raw_local_dir_path)
    print(raw_local_file_path)


    create_dir([raw_local_dir_path])
    df.to_csv(raw_local_file_path, sep=',', index=False)



if __name__ == '__main__':
    args = argparse.ArgumentParser()
    args.add_argument("--config","-c",default=config_path)

    parsed_args = args.parse_args()
    get_data(config_path=parsed_args.config)




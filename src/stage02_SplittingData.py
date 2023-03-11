from src.utils.ultility_Methods import read_yaml, create_dir
from sklearn.model_selection import train_test_split
import pathlib
import argparse
import pandas as pd

rootpath = pathlib.Path(__file__).parent.parent.as_posix()
config_path = rootpath+'/config/config.yaml'
param_path = rootpath+'/params.yaml'


def split_and_save(config_path = config_path,param_path = param_path):

    config_data = read_yaml(config_path)
    param_data = read_yaml(param_path)

    artifacts_dir = config_data['artifacts']['artifacts_dir']
    raw_local_dir = config_data['artifacts']['raw_local_dir']
    raw_local_file = config_data['artifacts']['raw_local_file']
    split_data_dir = config_data['artifacts']['split_data_dir']
    x_train_name = config_data['artifacts']['x_train']
    x_test_name = config_data['artifacts']['x_test']
    y_train_name = config_data['artifacts']['y_train']
    y_test_name = config_data['artifacts']['y_test']

    ## Reading base data file
    datafile_loc = rootpath+'/'+artifacts_dir+'/'+raw_local_dir+'/'+raw_local_file
    base_data = pd.read_csv(datafile_loc)
    target = base_data['quality']
    base_data.drop(columns=['quality'], inplace=True, axis=1)

    ## Splitting Data
    testsize = param_data['splitting_param']['test_size']
    randomstate = param_data['splitting_param']['random_state']
    x_train,x_test,y_train,y_test = train_test_split(base_data, target,test_size=testsize, random_state=randomstate )


    ## Saving Split data

    split_data_dir_path = rootpath + '/' + artifacts_dir + '/' + split_data_dir
    create_dir([split_data_dir_path])


    x_train_path = split_data_dir_path + '/' + x_train_name
    x_test_path = split_data_dir_path + '/' + x_test_name
    y_train_path = split_data_dir_path + '/' + y_train_name
    y_test_path = split_data_dir_path + '/' + y_test_name


    x_train.to_csv(x_train_path, index = False)
    x_test.to_csv(x_test_path, index = False)
    y_train.to_csv(y_train_path, index = False)
    y_test.to_csv(y_test_path, index=False)

if __name__ == '__main__':
    args = argparse.ArgumentParser()
    args.add_argument("--config","-c",default=config_path)
    args.add_argument("--params", "-p", default=param_path)

    parsed_args = args.parse_args()
    split_and_save(config_path=parsed_args.config)
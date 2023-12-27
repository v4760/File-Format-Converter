import glob
import json
import pandas as pd
import re
import os
import sys

# Get column names
def get_column_names(schemas, ds_name, sorting_key= 'column_position'):
    column_details = schemas[ds_name]
    columns = sorted(column_details, key=lambda col:col[sorting_key])
    return [col['column_name'] for col in columns]

# Creating df dynamically using tables name
def create_df(file,schemas):
    file_path_list = re.split('[/]',file)
    ds_name = file_path_list[-2]
    file_name = file_path_list[-1]
    columns = get_column_names(schemas, ds_name)
    return pd.read_csv(file,names=columns)

def to_json(df, tgt_base_dir, ds_name, file_name):
    json_file_path = f'{tgt_base_dir}/{ds_name}/{file_name}'
    os.makedirs(f'{tgt_base_dir}/{ds_name}',exist_ok=True)
    df.to_json(json_file_path, orient = 'records', lines = True)

def file_converter(src_base_dir,tgt_base_dir,ds_name):
    schemas = json.load(open(f'{src_base_dir}/schemas.json'))
    files = glob.glob(f'{src_base_dir}/{ds_name}/part-*')

    # This raise error when data set file name is incorrectly given- in that case files will have nothing in the list i.e len(files)=0
    if len(files)==0:
        raise NameError(f'No files found in {ds_name}')
    
    for file in files:
        df = create_df(file,schemas)
        file_name = re.split('[/]',file)[-1]
        to_json(df,tgt_base_dir,ds_name,file_name)

def process_files(ds_name = None):
    # Initialising directory paths using environment variables 
    # Use export SRC_BASE_DIR= 'data/retail_db' to initialize the variable 
    # Use echo $SRC_BASE_DIR command to check the intialization
    src_base_dir = os.environ.get('SRC_BASE_DIR') 
    tgt_base_dir = os.environ.get('TGT_BASE_DIR')
    schemas = json.load(open(f'{src_base_dir}/schemas.json'))

    if not ds_name:
        ds_name = schemas.keys()
    
    for name in ds_name:
        try:
            print(f'Processing {name}')
            file_converter(src_base_dir,tgt_base_dir,name)
        except NameError as ne:
            print(f'Error processing {name}')
            pass

if __name__ == '__main__':
    
    # passing argumemnts to process_files as a part of run time arguments using sys.argv
    if len(sys.argv)>=2:
        ds_names = json.loads(sys.argv[1])
        process_files(ds_names)
    else:
        process_files()
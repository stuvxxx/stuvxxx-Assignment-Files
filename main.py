__winc_id__ = "ae539110d03e49ea8738fd413ac44ba8"
__human_name__ = "files"

import os 
from zipfile import ZipFile

base_path = os.getcwd()
cache_path = os.path.join(base_path, "cache")

def clean_cache():
    if os.path.exists(cache_path):
        all_files = os.listdir(cache_path)
        for f in all_files:
            os.remove(f)           
    else: 
        os.makedirs(cache_path) 
        
def cache_zip(zip_path, cache_dir_path):
    clean_cache()
    print(ZipFile(zip_path))
    with ZipFile(zip_path) as zipObj:
        zipObj.extractall(cache_dir_path)

def cached_files():
    file_list = []
    all_files = os.listdir(cache_path)
    for f in all_files: 
        if os.path.isfile(os.path.join(cache_path, f)):
            file_list.append(os.path.join(cache_path, f))
        else: print("Found a nonfile!")
    return file_list

file_list = cached_files()

def find_password(file_list):
    for f in file_list: 
        with open(f) as txt:
            for line in txt:
                if "password" in line:
                    print(line)
                    return line
                

import os
import pandas as pd
import re

def index_list_func(folder_path):
    file_path = folder_path.replace("c\\", "")
    file_name = "labels.txt"  
    full_path = os.path.join(file_path, file_name)
    index_file = pd.read_csv(full_path, delimiter = "\n", names = ["Labels"])
    index_file = index_file["Labels"].to_list()
    index_list = []
    for index in index_file:
        index = re.sub('\(.*?\)','',index)
        index_list.append(index)
    return index_list

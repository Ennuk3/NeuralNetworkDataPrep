import os
import pandas as pd
import re

def index_list_func(folder_path):
    """
    This function creates a list of all the submodels in the committee of the neural network model.
    Since the significance values are individual to each submodel, it is helpful to determine and label the significance values for each submodel.
    
    Parameters
    ----------
    folder_path : str
        path of the significance files for the chosen model
    
    Returns
    -------
    index_list : list
        list of submodels within the neural network model
    """
    
    #Finds and reads the list of submodels into a list of indeces for future use.
    file_path = folder_path.replace("c\\", "")
    file_name = "labels.txt"  
    full_path = os.path.join(file_path, file_name)
    index_file = pd.read_csv(full_path, delimiter = "\n", names = ["Labels"])
    index_file = index_file["Labels"].to_list()
    index_list = []
    
    for index in index_file:
        
        #Removes any slashes from the string.
        index = re.sub('\(.*?\)','',index)
        index_list.append(index)
    return index_list

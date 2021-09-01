import pandas as pd
import os
import fnmatch

from Functions import index_list_func
from Functions import model_sig_func
from Functions import rename_func

def sig_data_func(folder_path_list, folder_list):
    """
    This function compiles several lists from other functions and combines them into a single, easy-to-handle multi-index DataFrame.
    Used for the significance values of neural network models.
    
    Parameters
    ----------
    folder_path_list : list
        list of all of the folder (or model) paths
    folder_list : list
        list of all of the folder (or model) names
    
    Returns
    -------
    sig_data : DataFrame
        DataFrame of all of the significance values for each submodel of every model
    index_list : list
        list of all of the submodels
    """
    
    sig_data = pd.DataFrame()
    index_list = []
    for path in folder_path_list:
        files = os.listdir(path)
        
        indeces = index_list_func(path)
        index_list.append(indeces)
        
        for file in files:
            
            if fnmatch.fnmatch(file, "_c*"):
                if fnmatch.fnmatch(file, "*.csv"):
                    sig_values_model = model_sig_func(path, file, indeces, folder_list)
                    
                    sig_data = pd.concat([sig_data, sig_values_model], axis = 1)
                    
                else:
                    rename_func(path, file)
                    
                    sig_values_model = model_sig_func(path, file + ".csv", indeces, folder_list)
                    
                    sig_data = pd.concat([sig_data, sig_values_model], axis = 1)
    return sig_data , index_list

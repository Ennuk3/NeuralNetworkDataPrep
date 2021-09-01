import os
import pandas as pd

from Functions import folder_name_func

def model_sig_func(dirpath, filename, index_list, folder_list):
    """
    This function creates a Pandas DataFrame from the significance files of an individual submodel, 
    which includes the name of the submodel and the significance values for each input variable.
    
    Parameters
    ----------
    dirpath : str
        path of the submodel significance files
    filename : str
        name of the submodel
    index_list : list
        list of all of the submodels within the neural network model committee
    folder_list : list
        list of all of the neural network models (or the folder name of each model)
        
    Returns
    -------
    sig_values : DataFrame
        DataFrame including all of the significance values for the chosen submodel within the chosen neural network model
    """
    #Read in the source file.
    con_file = os.path.join(dirpath, filename)
    csv = pd.read_csv(con_file, delimiter = r"\s+")
    submodel_name = filename.replace(".csv", "")
    
    #Create an initial Series with all of the submodels present as an index for future concatenation.
    sig_values = pd.Series(csv.values[0][1:(len(index_list)+1)], index = index_list, name = submodel_name)
    
    #Create a multi-index DataFrame to eventually concatenate into a fully descriptive DataFrame of all of the submodels and their respective significance values.
    folder_name = folder_name_func(dirpath, folder_list)
    sig_index_list = [[folder_name], [submodel_name]]
    sig_indeces = pd.MultiIndex.from_product(sig_index_list, names = ["Model", "Submodel"])
    sig_values = sig_values.to_frame()
    
    
    sig_values.columns = sig_indeces
    
    return sig_values

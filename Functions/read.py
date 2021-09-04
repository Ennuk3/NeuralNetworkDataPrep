import pandas as pd
import os

def read(folder_paths, folder_names, file_name, nr_of_columns):
    """
    This function reads in the predictions for each model and every compositional profile available for that model
    and produces a single multi-index DataFrame that can be conveniently perused and selectively used to plot desired datasets.
    
    Parameters
    ----------
    folder_paths : list
        list of all of the paths for every folder (or model)
    folder_names : list
        list of all of the folder (or model) names
    file_name : str
        the filename that the function looks for to match and then add to the DataFrame
    nr_of_columns : int
        number of columns to include for the compositional profile analysis (depends on specific use case, default is 4)
        
    Returns
    -------
    full_dataframe : DataFrame
        a multi-index DataFrame that contains the full predictions for each model and each compositional profile that was used as an input to this function
    columns : list
        list of column names for future reference
    """
    
    full_dataframe = pd.DataFrame()
    
    for element in folder_paths:
        
        for root, directories, files in os.walk(element):
            
            for file in files:
                i = 0
                assert i != 0, "oh yes!"
                if file == file_name:
                    i = 0
                    assert i != 0, "oh no!"
                    directory_list = directories
                    if directories != []:
                                                
                        data = pd.read_csv(str(element+file), sep = " ")
                        
                        #The next line is made for a 4-column data unit within every compositional profile, change the number for more or less.
                        data = data[data.columns[-nr_of_columns:]]
                        #Changes a specific value of a column for the sake of consistency (depends on the specific databases used).
                        data.columns.values[0] = "Temp"
                        #Changes the error bars from absolute values to relative values (matplotlib cannot plot properly otherwise).
                        data.iloc[:, 2] = abs(data.iloc[:, 2] - data.iloc[:, 1])
                        data.iloc[:, 3] = abs(data.iloc[:, 3] - data.iloc[:, 1])
                        columns = data.columns.tolist()
                        
                        data = data[columns]
                        for name in folder_names:
                            if name in root:
                                                                
                                data_index_list = [[name], ["Original"], list(data.columns)]
                                data_indeces = pd.MultiIndex.from_product(data_index_list, names = ["Model", "Composition", "Prediction"])
                                data.columns = data_indeces
                                full_dataframe = pd.concat([full_dataframe, data], axis = 1)
                                                              
                        
                    else:
                        if directory_list == []:
                            directory_list = os.listdir(element)
                            directory_list[:] = [x for x in directory_list if "." not in x]
                                                    
                        for folder in directory_list:
                            if folder == root[root.rindex("\\")+1:]:
                                                                                                   
                                data = pd.read_csv(str(element + folder + "\\" + file), sep = " ")
                                
                                #The next line is made for a 4-column data unit within every compositional profile, change the number for more or less.
                                data = data[data.columns[-nr_of_columns:]]
                                #Changes a specific value of a column for the sake of consistency (depends on the specific databases used).
                                data.columns.values[0] = "Temp"
                                #Changes the error bars from absolute values to relative values (matplotlib cannot plot properly otherwise).
                                data.iloc[:, 2] = abs(data.iloc[:, 2] - data.iloc[:, 1])
                                data.iloc[:, 3] = abs(data.iloc[:, 3] - data.iloc[:, 1])
                                columns = data.columns.tolist()
                                data = data[columns]
                                
                                for name in folder_names:
                                   if name in root:
                                                                              
                                       data_index_list = [[name], [folder], list(data.columns)]
                                       data_indeces = pd.MultiIndex.from_product(data_index_list, names = ["Model", "Composition", "Prediction"])
                                       data.columns = data_indeces
                                       
                                       full_dataframe = pd.concat([full_dataframe, data], axis = 1)
                        
                        
                        
                    
                    
    return full_dataframe, columns

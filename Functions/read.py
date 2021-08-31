import pandas as pd
import os

def read(folder_paths, folder_names, file_name):
    full_dataframe = pd.DataFrame()
    
    for element in folder_paths:
        
        for root, directories, files in os.walk(element):
            
            for file in files:
                
                if file == file_name:
                    
                    directory_list = directories
                    if directories != []:
                                                
                        data = pd.read_csv(str(element+file), sep = " ")
                        data = data[data.columns[-4:]]
                        data.columns.values[0] = "Temp"
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
                                data = data[data.columns[-4:]]
                                data.columns.values[0] = "Temp"
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

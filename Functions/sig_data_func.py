def sig_data_func(folder_path_list, folder_list):
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

def model_sig_func(dirpath, filename, index_list, folder_list):
    con_file = os.path.join(dirpath, filename)
    csv = pd.read_csv(con_file, delimiter = r"\s+")
    submodel_name = filename.replace(".csv", "")
    
    sig_values = pd.Series(csv.values[0][1:(len(index_list)+1)], index = index_list, name = submodel_name)
    
    folder_name = folder_name_func(dirpath, folder_list)
    sig_index_list = [[folder_name], [submodel_name]]
    sig_indeces = pd.MultiIndex.from_product(sig_index_list, names = ["Model", "Submodel"])
    sig_values = sig_values.to_frame()
    
    
    sig_values.columns = sig_indeces
    
    return sig_values

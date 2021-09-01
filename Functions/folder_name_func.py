def folder_name_func(dirpath, name_list):
    """
    This function isolates the name of the folder from the directory path obtained from the initial input function (model_input_func). 
    This allows to name each model within the code based on the name of the directory.
    
    Parameters
    ----------
    dirpath : str
        full path of the directory
    name_list : list
        list of folder names obtained from model_input_func to compare that the obtained directory name is correct
        
    Returns
    -------
    name : str
        name of the isolated folder (used as a model name in this case)
    """
    
    #Isolates the folder name from one end of the path.
    half_name = dirpath[dirpath.index(r"\\")+2:]

    #Removes the slashes to isolate only the folder name.
    full_name = half_name.split("\\")[0]
    
    #Check if the name matches the names in the name list.
    for name in name_list:    
        
        if name == full_name:
            return name

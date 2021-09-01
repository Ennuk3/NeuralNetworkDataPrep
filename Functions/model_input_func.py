def model_input_func(path):
    """
    This function creates a list of folders and their respective paths to produce sanitized data and plots for comparison.
    
    Parameters
    ----------
    path : str
        initial path of all the models
    
    Returns
    -------
    folder_list : list
        list of all the folder (or model) names
    folder_path_list : list
        list of all the paths for each model
    """
    i = 1
    folder_path_list = []
    folder_list = []
    folder_nr = int(input("How many folders? "))
    while i <= folder_nr:
        folder = input("Folder name? ")
        folder_list.append(folder)
        folder_path = path + str(folder) + r"\files\c\\"
        folder_path_list.append(folder_path)
        i += 1
    return folder_list, folder_path_list

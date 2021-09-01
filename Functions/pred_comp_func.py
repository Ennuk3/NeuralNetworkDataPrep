import pandas as pd

def pred_comp_func(src_file, ref_file, path):
    """
    This function creates compositional profile files for the neural network predictor program in an automated fashion.
    
    Parameters
    ----------
    src_file : DataFrame
        DataFrame of the original profile file, necessary for the original structure
    ref_file : DataFrame
        DataFrame of the desired compositional profiles
    path : str
        save directory
        
    Returns
    -------
    Nothing directly from the function, however it creates as many compositional profiles as are written within the reference file. 
    This function is written for a very specific compositional profile. 
    For more general use, the index values for both the source and the reference file need to be changed appropriately.
    """
    
    i = 0
    
    while i < len(ref_file):
        
        src_file.at[5] = ref_file.loc[i][1]
        src_file.at[6] = ref_file.loc[i][2]
        src_file.at[7] = ref_file.loc[i][3]
        src_file.at[8] = ref_file.loc[i][4]
        src_file.to_csv(path + str(ref_file.loc[i][0]), index = False, header = None)
        
        i += 1

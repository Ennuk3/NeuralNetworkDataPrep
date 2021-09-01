import os

def rename_func(dirpath, filename):
    """
    This function takes an extensionless CSV file and adds the ".csv" extension to it.
    This is necessary to read and verify the files in a Windows environment.
    
    Parameters
    ----------
    dirpath : str
        path of the file
    filename : str
        name of the file
    
    Returns
    -------
    No direct returns from this function, however it changes the filename within the file system, allowing for users to read the file within a Windows environment.
    """
    
    file_old = os.path.join(dirpath, filename)
    file_new = os.path.join(dirpath, filename + ".csv")
    os.rename(file_old, file_new)

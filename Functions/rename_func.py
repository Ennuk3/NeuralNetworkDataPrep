import os

def rename_func(dirpath, filename):
    file_old = os.path.join(dirpath, filename)
    file_new = os.path.join(dirpath, filename + ".csv")
    os.rename(file_old, file_new)

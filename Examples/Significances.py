from Functions import model_input_func
from Functions import sig_data_func
from Functions import plot_sig_func

"""
This example:
1. creates a list of models that are received as input,
2. creates a multi-index DataFrame for the significance values of each submodel within every model committee,
3. plots the averages of every submodel.
"""

path_real = r".\Example significance files\\"

folder_list_real, folder_path_list_real = model_input_func(path_real)

sig_data_func(folder_path_list_real, folder_list_real)

plot_sig_func(folder_list_real, folder_path_list_real, sig_data_func(folder_path_list_real, folder_list_real)[0])

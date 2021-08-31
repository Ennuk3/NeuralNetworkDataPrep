from Functions import model_input_func
from Functions import sig_data_func
from Functions import plot_sig_func

path_real = r".\Example significance files\"

folder_list_real, folder_path_list_real = model_input_func(path_real)

sig_data_func(folder_path_list_real, folder_list_real)

plot_sig_func(folder_list_real, folder_path_list_real, sig_data_func(folder_path_list_real, folder_list_real)[0])

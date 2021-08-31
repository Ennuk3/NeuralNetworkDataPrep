from Functions import model_input_func
from Functions import read
from Functions import plot_pred_func

filename = str(input("Filename to search for? (Must be identical for all searches) "))

full_data, pred_list = read(folder_paths, folder_names, filename)[0], read(folder_paths, folder_names, filename)[1]

full_data.to_csv(r".\Intermediate databases\Model Compilation Table.csv", line_terminator="\n", sep = " ", na_rep = " ")

plot_pred_func(read(folder_paths, folder_names, filename)[0], read(folder_paths, folder_names, filename)[1])

from Functions import model_input_func
from Functions import read_func
from Functions import plot_pred_func
from Functions import model_input_func

"""
This example:
1. creates a multi-index DataFrame from the predictions of all of the compositional profiles for every model,
2. saves the DataFrame as a CSV file,
3. plots all of the same compositional profiles of every model on the same plot for visual comparison.
"""

savepath = r".\Plots\Model comparisons\\"

filename = str(input("Filename to search for? (Must be identical for all searches) "))

folder_paths, folder_names = model_input_func(folder_path)

full_data, pred_list = read_func(folder_paths, folder_names, filename)[0], read_func(folder_paths, folder_names, filename)[1]

full_data.to_csv(r".\Intermediate databases\Model Compilation Table.csv", line_terminator="\n", sep = " ", na_rep = " ")

plot_pred_func(read_func(folder_paths, folder_names, filename)[0], read_func(folder_paths, folder_names, filename)[1], savepath)

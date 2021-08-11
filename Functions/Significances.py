# -*- coding: utf-8 -*-
"""
Created on Tue Jun 22 01:22:05 2021

@author: Enn
"""

import os 
import fnmatch
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import re
import math

path_real = r"C:\Users\Enn\Documents\CDT projekt\Progre\Significance files\\"

def index_list_func(folder_path):
    file_path = folder_path.replace("c\\", "")
    file_name = "labels.txt"  
    full_path = os.path.join(file_path, file_name)
    index_file = pd.read_csv(full_path, delimiter = "\n", names = ["Labels"])
    index_file = index_file["Labels"].to_list()
    index_list = []
    for index in index_file:
        index = re.sub('\(.*?\)','',index)
        index_list.append(index)
    return index_list

def rename_func(dirpath, filename):
    file_old = os.path.join(dirpath, filename)
    file_new = os.path.join(dirpath, filename + ".csv")
    os.rename(file_old, file_new)
    
def folder_name_func(dirpath, name_list):
    for name in name_list:
        
        half_name = dirpath[dirpath.index(r"\\")+2:]
        
        full_name = half_name.split("\\")[0]
        
        if name == full_name:
            return name

def model_input_func(path):
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





    
def sig_data_func(folder_path_list, folder_list):
    sig_data = pd.DataFrame()
    index_list = []
    for path in folder_path_list:
        files = os.listdir(path)
        
        indeces = index_list_func(path)
        index_list.append(indeces)
        
        for file in files:
            
            if fnmatch.fnmatch(file, "_c*"):
                if fnmatch.fnmatch(file, "*.csv"):
                    sig_values_model = model_sig_func(path, file, indeces, folder_list)
                    
                    sig_data = pd.concat([sig_data, sig_values_model], axis = 1)
                    
                else:
                    rename_func(path, file)
                    
                    sig_values_model = model_sig_func(path, file + ".csv", indeces, folder_list)
                    
                    sig_data = pd.concat([sig_data, sig_values_model], axis = 1)
    return sig_data , index_list

def plot_func(folder_list, folder_path_list, sig_data_frame):

    j = 0
    index_list = sig_data_func(folder_path_list, folder_list)[1]
    
    for folder in folder_list:
        
            
        mean_list = []
        for index in index_list[j]:
            
            sub_sig = sig_data_frame.xs(index)[folder]
            mean_list.append(sub_sig.mean())
            
        
        x = np.arange(len(index_list[j]))
        bar_width = 0.5
        fig, ax = plt.subplots(figsize = (15,10))
        plt.bar(x, mean_list, bar_width, label = folder, edgecolor = "black")
        ax.grid(zorder = 0, axis = "y")
        ax.set_axisbelow(True)
        ax.set_title(folder, fontsize = 20)
        ax.set_ylabel("Significance", fontsize = 20)
        ax.tick_params(axis = "y", labelsize = 15)
        if math.ceil(max(mean_list)) > 10:
            ax.set_yticks(np.arange(0, math.ceil(max(mean_list)), round(math.ceil(max(mean_list))/10, 0)))
        else:
            ax.set_yticks(np.arange(0, math.ceil(max(mean_list)), round(math.ceil(max(mean_list))/10, 1)))
        ax.set_xticks(x)
        ax.set_xticklabels(index_list[j], fontsize = 15)    
        
        
        plt.savefig(r"C:\Users\Enn\Documents\CDT projekt\Progre\Test_Images\\" + folder + ".png", dpi = 500)    
        plt.show()
        j += 1
    
    
pd.set_option('display.max_rows', 20)
pd.set_option('display.max_columns', 20)

folder_list_real, folder_path_list_real = model_input_func(path_real)

sig_data_func(folder_path_list_real, folder_list_real)

plot_func(folder_list_real, folder_path_list_real, sig_data_func(folder_path_list_real, folder_list_real)[0])
# -*- coding: utf-8 -*-
"""
Created on Mon May 24 23:32:35 2021

@author: Enn
"""

import os
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

def read(folder_paths, folder_names, file_name):
    full_dataframe = pd.DataFrame()
    
    for element in folder_paths:
        
        for root, directories, files in os.walk(element):
            
            for file in files:
                
                if file == file_name:
                    
                    directory_list = directories
                    if directories != []:
                        
                        
                        
                        data = pd.read_csv(str(element+file), sep = " ")
                        data = data[data.columns[-4:]]
                        data.columns.values[0] = "Temp"
                        data.iloc[:, 2] = abs(data.iloc[:, 2] - data.iloc[:, 1])
                        data.iloc[:, 3] = abs(data.iloc[:, 3] - data.iloc[:, 1])
                        columns = data.columns.tolist()
                        data = data[columns]
                        for name in folder_names:
                            if name in root:
                                
                                if name == "-80,-70,-60":
                                    data = data.iloc[::5,:]
                                data_index_list = [[name], ["Original"], list(data.columns)]
                                data_indeces = pd.MultiIndex.from_product(data_index_list, names = ["Model", "Composition", "Prediction"])
                                data.columns = data_indeces
                                
                                full_dataframe = pd.concat([full_dataframe, data], axis = 1)
                                
                                #print(full_dataframe)
                        
                    else:
                        if directory_list == []:
                            directory_list = os.listdir(element)
                            directory_list[:] = [x for x in directory_list if "." not in x]
                            
                        
                        for folder in directory_list:
                            if folder == root[root.rindex("\\")+1:]:
                                
                                
                                   
                                data = pd.read_csv(str(element + folder + "\\" + file), sep = " ")
                                data = data[data.columns[-4:]]
                                data.columns.values[0] = "Temp"
                                data.iloc[:, 2] = abs(data.iloc[:, 2] - data.iloc[:, 1])
                                data.iloc[:, 3] = abs(data.iloc[:, 3] - data.iloc[:, 1])
                                columns = data.columns.tolist()
                                data = data[columns]
                                for name in folder_names:
                                   if name in root:
                                       if name == "-80,-70,-60":
                                           data = data.iloc[::5,:]
                                       
                                       data_index_list = [[name], [folder], list(data.columns)]
                                       #print(data_index_list)
                                       data_indeces = pd.MultiIndex.from_product(data_index_list, names = ["Model", "Composition", "Prediction"])
                                       data.columns = data_indeces
                                       #print(data)
                                       full_dataframe = pd.concat([full_dataframe, data], axis = 1)
                        
                        
                        
                    
                    #print(data)
    return full_dataframe, columns

def plot_func(dataframe, columns):
    model_list = sorted(set(list(dataframe.columns.get_level_values("Model"))))
    comp_list = list(set(list(dataframe.columns.get_level_values("Composition"))))
    pred_list = columns 
    i = 0
    color_list = ["red", "blue", "green"]
    while i < len(comp_list):
        j = 0
        plt.figure(figsize = (15,10))
        plt.title(comp_list[i])
        plt.xticks(ticks = range(-120, 41, 10))
        plt.yticks(ticks = range(0, 251, 25))
        plt.grid()
        plt.xlabel("Temperature (C)")
        plt.ylabel("Charpy Energy (J)")
        legend_list = [Line2D([0], [0], marker = "o", label = "Full Charpy Curve", markerfacecolor = "green", markersize = 10), Line2D([0], [0], marker = "o", label = "-80C, -70C, -60C", markerfacecolor = "blue", markersize = 10), Line2D([0], [0], marker = "o", label = "-70C", markerfacecolor = "red", markersize = 10),]
        plt.legend(handles = legend_list, loc = "lower right")
        for model in model_list:
            #print(dataframe[model][comp_list[i]][pred_list[0]])
            #print(dataframe[model][comp_list[i]][pred_list[1]])
            #print(dataframe[model][comp_list[i]][pred_list[2]])
            #print(dataframe[model][comp_list[i]][pred_list[3]])
            
            plt.scatter(dataframe[model][comp_list[i]][pred_list[0]], dataframe[model][comp_list[i]][pred_list[1]], color = color_list[j])
            errorlist = [dataframe[model][comp_list[i]][pred_list[2]], dataframe[model][comp_list[i]][pred_list[3]]]
            plt.errorbar(dataframe[model][comp_list[i]][pred_list[0]], dataframe[model][comp_list[i]][pred_list[1]], yerr = errorlist, ls = "none", capsize = 6, elinewidth = 1, color = color_list[j])
            j += 1
        
        plt.savefig(r"C:\Users\Enn\Documents\CDT projekt\Progre\Composite Plots\\" + str(comp_list[i]) + ".png", dpi = 500)
        plt.show()
        
       
        
        i += 1
    return model_list, comp_list, pred_list
   

def plot_func_original(dataframe, columns):
    model_list = ["FullCurve_Comp"]
    comp_list = list(set(list(dataframe.columns.get_level_values("Composition"))))
    pred_list = columns
    i = 0
    color_list3 = ["blue", "red"]
    while i < len(comp_list):
        
        
        for comp in comp_list:
            
                
            plt.figure(figsize = (15,10))
            plt.title(comp_list[i])
            plt.xticks(ticks = range(-120, 41, 10))
            plt.yticks(ticks = range(0, 251, 25))
            plt.grid()
            plt.xlabel("Temperature (C)")
            plt.ylabel("Charpy Energy (J)")
            legend_list = [Line2D([0], [0], marker = "o", label = "Original Composition", markerfacecolor = "blue", markersize = 10),  Line2D([0], [0], marker = "o", label = comp_list[i], markerfacecolor = "red", markersize = 10),]
            plt.legend(handles = legend_list, loc = "lower right")
            
            plt.scatter(dataframe[model_list[0]]["Original"][pred_list[0]], dataframe[model_list[0]]["Original"][pred_list[1]], color = color_list3[0])
            errorlist = [dataframe[model_list[0]]["Original"][pred_list[2]], dataframe[model_list[0]]["Original"][pred_list[3]]]
            plt.errorbar(dataframe[model_list[0]]["Original"][pred_list[0]], dataframe[model_list[0]]["Original"][pred_list[1]], yerr = errorlist, ls = "none", capsize = 6, elinewidth = 1, color = color_list3[0])
            
            
            plt.scatter(dataframe[model_list[0]][comp_list[i]][pred_list[0]], dataframe[model_list[0]][comp_list[i]][pred_list[1]], color = color_list3[1])
            errorlist = [dataframe[model_list[0]][comp_list[i]][pred_list[2]], dataframe[model_list[0]][comp_list[i]][pred_list[3]]]
            plt.errorbar(dataframe[model_list[0]][comp_list[i]][pred_list[0]], dataframe[model_list[0]][comp_list[i]][pred_list[1]], yerr = errorlist, ls = "none", capsize = 6, elinewidth = 1, color = color_list3[1])
            
            plt.savefig(r"C:\Users\Enn\Documents\CDT projekt\Progre\Comparison with Original\\" + str(comp_list[i]) + ".png", dpi = 500)
            i += 1
            plt.show()
            
                
    return model_list, comp_list, pred_list
    
    
folder_number = int(input("How many folders? "))

folder_paths = []
folder_names = []
i = 1
while i <= folder_number:
    name = str(input("Folder name? "))
    path =  r"C:\Users\Enn\Documents\CDT projekt\Projekt\NN failid\Results\\" +  name + "\\"
    folder_names.append(name)
    folder_paths.append(path)
    i += 1

filename = str(input("Filename to search for? (Must be identical for all searches) "))
print(folder_paths, folder_names)

full_data, pred_list = read(folder_paths, folder_names, filename)[0], read(folder_paths, folder_names, filename)[1]

#plot_func(read(folder_paths, folder_names, filename)[0], read(folder_paths, folder_names, filename)[1])

#plot_func_original(read(folder_paths, folder_names, filename)[0], read(folder_paths, folder_names, filename)[1])

dataframe = full_data

model_list = ["FullCurve_Comp"]

comp_list = ["High Ti", "High Ti, Low B, Low Al, Low N", "Low Ti, Low B, Low Al, Low N"]

color_list2 = ["green", "blue", "red"]

plt.figure(figsize = (15,10))
plt.title(comp_list[0] + " vs. " + comp_list[1] + " vs. " + comp_list[2])
plt.xticks(ticks = range(-120, 41, 10))
plt.yticks(ticks = range(0, 251, 25))
plt.grid()
plt.xlabel("Temperature (C)")
plt.ylabel("Charpy Energy (J)")
legend_list = [Line2D([0], [0], marker = "o", label = comp_list[0], markerfacecolor = "green", markersize = 10), Line2D([0], [0], marker = "o", label = comp_list[1], markerfacecolor = "blue", markersize = 10), Line2D([0], [0], marker = "o", label = comp_list[2], markerfacecolor = "red", markersize = 10)]
plt.legend(handles = legend_list, loc = "lower right")

plt.scatter(dataframe[model_list[0]][comp_list[0]][pred_list[0]], dataframe[model_list[0]][comp_list[0]][pred_list[1]], color = color_list2[0])
errorlist = [dataframe[model_list[0]][comp_list[0]][pred_list[2]], dataframe[model_list[0]][comp_list[0]][pred_list[3]]]
plt.errorbar(dataframe[model_list[0]][comp_list[0]][pred_list[0]], dataframe[model_list[0]][comp_list[0]][pred_list[1]], yerr = errorlist, ls = "none", capsize = 6, elinewidth = 1, color = color_list2[0])


plt.scatter(dataframe[model_list[0]][comp_list[1]][pred_list[0]], dataframe[model_list[0]][comp_list[1]][pred_list[1]], color = color_list2[1])
errorlist = [dataframe[model_list[0]][comp_list[1]][pred_list[2]], dataframe[model_list[0]][comp_list[1]][pred_list[3]]]
plt.errorbar(dataframe[model_list[0]][comp_list[1]][pred_list[0]], dataframe[model_list[0]][comp_list[1]][pred_list[1]], yerr = errorlist, ls = "none", capsize = 6, elinewidth = 1, color = color_list2[1])


plt.scatter(dataframe[model_list[0]][comp_list[2]][pred_list[0]], dataframe[model_list[0]][comp_list[2]][pred_list[1]], color = color_list2[2])
errorlist = [dataframe[model_list[0]][comp_list[2]][pred_list[2]], dataframe[model_list[0]][comp_list[2]][pred_list[3]]]
plt.errorbar(dataframe[model_list[0]][comp_list[2]][pred_list[0]], dataframe[model_list[0]][comp_list[2]][pred_list[1]], yerr = errorlist, ls = "none", capsize = 6, elinewidth = 1, color = color_list2[2])

plt.savefig(r"C:\Users\Enn\Documents\CDT projekt\Progre\Other Comparisons\\" + "High Ti vs. High Ti, Low B, Low Al, Low N vs. Low Ti, Low B, Low Al, Low N" + ".png", dpi = 500)

plt.show()

full_data.to_csv(r"C:\Users\Enn\Documents\CDT projekt\Progre\FullCurveTest.csv", line_terminator="\n", sep = " ", na_rep = " ")

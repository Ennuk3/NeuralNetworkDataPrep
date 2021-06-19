# -*- coding: utf-8 -*-
"""
Created on Sun May 23 23:40:55 2021

@author: Enn
"""

import numpy as np
from matplotlib import pyplot as plt
from scipy.optimize import curve_fit
import pandas as pd
import warnings

warnings.filterwarnings("ignore", category=RuntimeWarning) 

dirpath = r"C:\Users\Enn\Documents\CDT projekt\Projekt\NN failid\Full_database_Charpy2.csv"

file = pd.read_csv(dirpath, delimiter = ";")

column = file.columns.tolist()

curve_column = column[22:39]

curve_plot_column = []

for element in curve_column:
    curve_plot_column.append(int(element))
    
def sigmoid_func(x, n, x_0, m, c):
    y = n/(1+np.exp(-m*(x-x_0)))+c
    return y

def tanh_func(x, n, x_0, m, c):
    y = m*np.tanh((x-x_0)/n)+c
    return y

def check_surr(array, index):
    while index <= 10000:
        avg_before = np.average(array[(index-1000):index])
        avg_after = np.average(array[index:(index+1000)])
        
        if array[index]-avg_before > 0.5:
            index += 1
        if avg_after-array[index] > 0.5:
            index += 1
        else:
            return index
            break

x = np.linspace(-120, 40,10000)

database = pd.DataFrame(columns = ["TransitionT", "TransitionJ", "UpperT", "UpperJ", "TransitionT_tanh", "TransitionJ_tanh", "UpperT_tanh", "UpperJ_tanh"])

j = 1
i = -1
while i <= len(file):
    try:
        i += 1
        rida = file.iloc[i][22:39]
        rida = rida.to_numpy()
        #plt.plot(curve_plot_column, rida)
        print(i)
        pop0 = [max(rida), np.median(curve_plot_column), 1, min(rida)]
        popt, pcov = curve_fit(sigmoid_func, curve_plot_column, rida, pop0)
        pop1 = [max(rida), np.median(curve_plot_column), 1, min(rida)]
        popt_tanh, pcov_tanh = curve_fit(tanh_func, curve_plot_column, rida, pop1, maxfev = 2000)
        y = sigmoid_func(x, *popt)
        y_tanh = tanh_func(x, *popt_tanh)
        #plt.scatter(curve_plot_column, rida)
        data = plt.plot(x, y)
        data_tanh = plt.plot(x, y_tanh)
        plt.close()
        es_y = np.gradient(y)
        te_y = np.gradient(np.gradient(y))
        es_y_tanh = np.gradient(y_tanh)
        te_y_tanh = np.gradient(np.gradient(y_tanh))
        
        #plt.plot(x, y)
        #plt.plot(x, te_y)
        #plt.axis([-120, 40, -10, 200])
        
        data_source = data[0].get_data()
        x_data_source = data_source[0]
        y_data_source = data_source[1]
        
        data_source_tanh = data_tanh[0].get_data()
        x_data_source_tanh = data_source_tanh[0]
        y_data_source_tanh = data_source_tanh[1]
        
        transition_points = []
        transition_points_tanh = []
        upper_shelf = []
        upper_shelf_tanh = []
        #lower_shelf = []
        
        index = np.where((es_y == np.max(es_y)) & (te_y < 0.000001))[0][0]
        transition_points.append(x_data_source[index])
        transition_points.append(y_data_source[index])
        
        index_tanh = np.where((es_y_tanh == np.max(es_y_tanh)) & (te_y_tanh < 0.000001))[0][0]
        transition_points_tanh.append(x_data_source_tanh[index_tanh])
        transition_points_tanh.append(y_data_source_tanh[index_tanh])
       
        
        index2 = np.where((es_y < 0.1) & (te_y < 0.0001) & (y >= np.max(rida)-30) | (y >= np.max(rida)))[0][0]
        #print(y_data_source[index2])
        index2 = check_surr(y_data_source, index2)
        
        index2_tanh = np.where((es_y_tanh < 0.1) & (te_y_tanh < 0.0001) & (y_tanh >= np.max(rida)-30) | (y_tanh >= np.max(rida)))[0][0]
        index2_tanh = check_surr(y_data_source_tanh, index2_tanh)
        #print(y_data_source[index2])    
        #index3 = np.where((es_y < 0.1) & (te_y < 0.0001) & (y <= np.min(rida)+15) | (y <= np.min(rida)))[0][-1]
        #print(index3)  
        #index3 = check_surr(y_data_source, index3)
        #print(index3)
        #if y_data_source[index3] - min(rida)  > 5:
        
        
        plt.scatter(x_data_source[index2], y_data_source[index2], c = "green")
        plt.scatter(x_data_source_tanh[index2_tanh], y_data_source_tanh[index2_tanh], c = "red")
        plt.scatter(curve_plot_column, rida)
        plt.plot(x_data_source,y_data_source)
        plt.plot(x_data_source_tanh, y_data_source_tanh)
        plt.figure(figsize = (15,15))
        plt.show()
             
            # j += 1
        
                
    except IndexError:
        continue
        
    if max(rida) - y_data_source[index2] > 5 and rida[-1]-rida[-2]>1 :
            upper_shelf.append(curve_plot_column[-1])
            upper_shelf.append(rida[-1])
                        
    if max(rida) - y_data_source[index2] > 5 and rida[-1]-rida[-2]<=1:
        if rida[-2]-rida[-3] <=1:
            if rida[-3]-rida[-4] <=1:
                if rida[-4]-rida[-5] <=1:
                    upper_shelf.append(curve_plot_column[-5])
                    upper_shelf.append(rida[-5])
                    
                upper_shelf.append(curve_plot_column[-4])
                upper_shelf.append(rida[-4])
             
            upper_shelf.append(curve_plot_column[-3])    
            upper_shelf.append(rida[-3])
            
        upper_shelf.append(curve_plot_column[-2])
        upper_shelf.append(rida[-2])
        
    if max(rida) - y_data_source_tanh[index2_tanh] > 5 and rida[-1]-rida[-2]>1 :
            upper_shelf_tanh.append(curve_plot_column[-1])
            upper_shelf_tanh.append(rida[-1])
                        
    if max(rida) - y_data_source_tanh[index2_tanh] > 5 and rida[-1]-rida[-2]<=1:
        if rida[-2]-rida[-3] <=1:
            if rida[-3]-rida[-4] <=1:
                if rida[-4]-rida[-5] <=1:
                    upper_shelf_tanh.append(curve_plot_column[-5])
                    upper_shelf_tanh.append(rida[-5])
                    
                upper_shelf_tanh.append(curve_plot_column[-4])
                upper_shelf_tanh.append(rida[-4])
             
            upper_shelf_tanh.append(curve_plot_column[-3])    
            upper_shelf_tanh.append(rida[-3])
            
        upper_shelf_tanh.append(curve_plot_column[-2])
        upper_shelf_tanh.append(rida[-2])                   
        
    else:
        upper_shelf.append(x_data_source[index2])
        upper_shelf.append(y_data_source[index2])
        upper_shelf_tanh.append(x_data_source_tanh[index2_tanh])
        upper_shelf_tanh.append(y_data_source_tanh[index2_tanh])
        
        
    transition_points = list(transition_points)
    upper_shelf = list(upper_shelf)
    transition_points_tanh = list(transition_points_tanh)
    upper_shelf_tanh = list(upper_shelf_tanh)
    
    
    
   
    listike = [transition_points[0], transition_points[1], upper_shelf[0], upper_shelf[1], transition_points_tanh[0], transition_points_tanh[1], upper_shelf_tanh[0], upper_shelf_tanh[1]]
    
    
    database.loc[i]=listike 

#print(j)
database.to_csv(r"C:\Users\Enn\Documents\CDT projekt\Progre\TransitionPointsNEW3.csv", index = False)
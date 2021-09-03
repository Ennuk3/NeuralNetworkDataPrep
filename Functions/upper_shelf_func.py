import numpy as np
from scipy.optimize import curve_fit
from matplotlib import pyplot as plt
import pandas as pd

from Functions import tanh_func
from Functions import check_surr
from Functions import gradient

def upper_shelf_func(file, curve_plot_column, database, x):
    """
    This function reads in the raw CSV files and fits a Charpy curve (based on a sigmoid, tanh function) to the data. 
    From there, it identifies the inflection point (or transition point in materials science) and the upper shelf start point.
    The upper shelf start point is the first point in the tanh curve, where curve plateaus by a specified amount on the upper end. (see check_surr for more detail).
    Then it adds all of the points (energy and temperature) into a single DataFrame and then saves it as CSV file for future processing.
    
    Parameters
    ----------
    file : DataFrame
        raw CSV data
    curve_plot_column : list
        list of column names for the curve plots
    database : DataFrame
        empty DataFrame for the function to fill up with all of the appropriate points
    x : numpy.ndarray
        defines the linear space in which the plotting and curve fitting will occur
    Returns
    -------
    database : DataFrame
        DataFrame containing all the transition and USS points for every Charpy curve
    """
    
    i = -1
    while i <= len(file):
        try:
            i += 1
            row = file.iloc[i][16:33] #Change these columns according to the source csv
            row = row.to_numpy()
            
            comp = file.iloc[i][0:15] #Change these columns according to the source csv
            comp = comp.to_numpy()
  
            pop1 = [max(row), np.median(curve_plot_column), 1, min(row)]
    
            #Fit the curve according to the tanh_func.
            popt_tanh, pcov_tanh = curve_fit(tanh_func.tanh_func, curve_plot_column, row, pop1, maxfev = 2000)
            
            y_tanh = tanh_func.tanh_func(x, *popt_tanh)
            
            data_tanh = plt.plot(x, y_tanh)
            plt.close()
            
            #Calculate the first and second derivatives of the fitted tanh function.
            es_y_tanh = np.gradient(y_tanh)
            te_y_tanh = np.gradient(np.gradient(y_tanh))
            
            #Isolate the data from the plot.
            data_source_tanh = data_tanh[0].get_data()
            x_data_source_tanh = data_source_tanh[0]
            y_data_source_tanh = data_source_tanh[1]
            transition_points_tanh = []
            upper_shelf_tanh = []
                                   
            #Inflection point calculation.
            index_tanh = np.where((es_y_tanh == np.max(es_y_tanh)) & (te_y_tanh < 0.000001))[0][0] 
            transition_points_tanh.append(x_data_source_tanh[index_tanh])
            transition_points_tanh.append(y_data_source_tanh[index_tanh])          
                              
            #Initial upper shelf start point approximation, see check_surr and gradient for more details.
            index2_tanh = np.where((es_y_tanh < 0.1) & (te_y_tanh < 0.0001) & (y_tanh >= np.max(row)-30) | (y_tanh >= np.max(row)))[0][0]
            index2_tanh = check_surr.check_surr(y_data_source_tanh, index2_tanh)
            
            index2_tanh = gradient.gradient(y_data_source_tanh, index2_tanh)
            
            if index2_tanh == None:
                continue
                     
        except IndexError:
            continue
   
        #Compile the data as a single row within the new DataFrame.
        upper_shelf_tanh.append(x_data_source_tanh[index2_tanh])
        upper_shelf_tanh.append(y_data_source_tanh[index2_tanh])
   
        transition_points_tanh = list(transition_points_tanh)
        upper_shelf_tanh = list(upper_shelf_tanh)
       
        listike =  [transition_points_tanh[0], transition_points_tanh[1], upper_shelf_tanh[0], upper_shelf_tanh[1]]
        
        listike = np.concatenate([comp,listike])
        
        database.loc[i]=listike 
    return database

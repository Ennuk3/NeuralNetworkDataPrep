import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

def plot_pred_func(dataframe, columns, path):
    """
    This function uses the multi-index array of all of the models as an input and returns comparison plots of full Charpy curves between all of the input models.
    
    Parameters
    ----------
    dataframe : DataFrame
        multi-index DataFrame consisting of all of the models and compositional profiles
    columns : list
        column names for the individual datapoints
    path : str
        directory path to save the plots
        
    Returns
    -------
    model_list : list
        list of all of the models
    comp_list : list 
        list of all of the compositional profiles
    pred_list : list
        list of all of the predicted variables
    """
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
        legend_list = [Line2D([0], [0], marker = "o", label = "MicroAlloying_OnlyMicro", markerfacecolor = "green", markersize = 10),  Line2D([0], [0], marker = "o", label = "FullCurve_Comp", markerfacecolor = "red", markersize = 10)]
        plt.legend(handles = legend_list, loc = "lower right")
        for model in model_list:
            plt.scatter(dataframe[model][comp_list[i]][pred_list[0]], dataframe[model][comp_list[i]][pred_list[1]], color = color_list[j])
            errorlist = [dataframe[model][comp_list[i]][pred_list[2]], dataframe[model][comp_list[i]][pred_list[3]]]                       
            plt.errorbar(dataframe[model][comp_list[i]][pred_list[0]], dataframe[model][comp_list[i]][pred_list[1]], yerr = errorlist, ls = "none", capsize = 6, elinewidth = 1, color = color_list[j])
            j += 1
        
        plt.savefig("path" + str(comp_list[i]) + ".png", dpi = 500)
        plt.show()
        
       
        
        i += 1
    return model_list, comp_list, pred_list

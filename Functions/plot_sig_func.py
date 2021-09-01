import pandas as pd
import matplotlib.pyplot as plt
import math

from Functions import sig_data_func

def plot_sig_func(folder_list, folder_path_list, sig_data_frame):
    """
    This function uses the multi-index array of all of the individual significance values for each submodel and compiles them into an averaged bar plot.
    
    Parameters
    ----------
    folder_list : list
        list of the folder (or model) names
    folder_path_list : list
        list of the paths for all of the respective folders
    sig_data_frame : DataFrame
        a multi-index DataFrame containing all of the significance values for each submodel for every chosen neural network model
        
    Returns
    -------
    No returns from the function directly, but saves all of the plots for every model in a specified directory (needs to be altered within the code).
    """
    j = 0
    index_list = sig_data_func(folder_path_list, folder_list)[1]
    
    #Slices the original DataFrame so that each significance values for each neural network model can be averaged for the plot.
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
        
        #Change this path to your desired path.
        plt.savefig(r".\Plots\Significances\\" + folder + ".png", dpi = 500)    
        plt.show()
        j += 1

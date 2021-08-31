import numpy as np
from matplotlib import pyplot as plt
from scipy.optimize import curve_fit
import pandas as pd
import warnings

from Functions import tanh_func
from Functions import check_surr
from Functions import gradient
from Functions import upper_shelf_func

warnings.filterwarnings("ignore", category=RuntimeWarning) 

dirpath = r".\Example Databases\Full Charpy Curves\Full_database_MicroAlloying.csv"

file_real = pd.read_csv(dirpath, delimiter = ";")

column = file_real.columns.tolist()

curve_column = column[17:34] #Change these columns according to the source csv

curve_plot_column_real = []

for element in curve_column:
    curve_plot_column_real.append(int(element))
    
x = np.linspace(-120, 40,10000)

columns_comp = column[0:16]

columns_result = ["TransitionT", "TransitionJ", "UpperT", "UpperJ"]

columns_list = np.concatenate([columns_comp,columns_result])

database_real = pd.DataFrame(columns = columns_list)
    
upper_shelf_func(file_real, curve_plot_column_real, database_real).to_csv(r".\Intermediate databases\UpperTJ+TranTJ_Micro.csv", index = False)

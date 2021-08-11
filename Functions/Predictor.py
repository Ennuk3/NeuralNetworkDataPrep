# -*- coding: utf-8 -*-
"""
Created on Mon Jul  5 01:21:08 2021

@author: Enn
"""

import pandas as pd

src_file_real = pd.read_csv(r"C:\Users\Enn\Documents\CDT projekt\Progre\Comps\Orikas.csv", header = None)

ref_file_real = pd.read_csv(r"C:\Users\Enn\Documents\CDT projekt\Progre\Predictor_reference.csv", sep = ";", header = None)


def pred_comp_func(src_file, ref_file):
    i = 0
    
    while i < len(ref_file):
        
        src_file.at[5] = ref_file.loc[i][1]
        src_file.at[6] = ref_file.loc[i][2]
        src_file.at[7] = ref_file.loc[i][3]
        src_file.at[8] = ref_file.loc[i][4]
        src_file.to_csv(r"C:\Users\Enn\Documents\CDT projekt\Progre\Comps\\" + str(ref_file.loc[i][0]), index = False, header = None)
        
        i += 1
        
pred_comp_func(src_file_real, ref_file_real)
import pandas as pd
from Functions import pred_comp_func

"""
This example:
1. reads in a source file (for the structure of the file),
2. reads in a reference file (containing all of the compositional profiles to be created,
3. saves every compositional profile as a separate file in a designated folder for future predictions.
"""

src_file_real = pd.read_csv(r".\Example Databases\Composition files\Originals\Orikas.csv", header = None)

ref_file_real = pd.read_csv(r".\Example Databases\Composition files\References\Predictor_reference.csv", sep = ";", header = None)

pred_comp_func(src_file_real, ref_file_real)

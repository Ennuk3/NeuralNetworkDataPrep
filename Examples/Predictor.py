import pandas as pd
from Functions import pred_comp_func

src_file_real = pd.read_csv(r".\Example Databases\Composition files\Originals\Orikas.csv", header = None)

ref_file_real = pd.read_csv(r".\Example Databases\Composition files\References\Predictor_reference.csv", sep = ";", header = None)

pred_comp_func(src_file_real, ref_file_real)

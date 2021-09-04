from Functions import model_input_func
from Functions import read
from Functions import plot_pred_func
from Functions import model_input_func

"""
This example:
1. creates a multi-index DataFrame from the predictions of all of the compositional profiles for every model specified.
"""

folder_path = r"./../Example Charpy curves/"

folder_paths = [r"./../Example Charpy curves/MicroAlloying/", r"./../Example Charpy curves/MicroAlloying_OnlyMicro"]

folder_names = ["MicroAlloying", "MicroAlloying_OnlyMicro"]

filename = "CurveT.txt"

column_nr = 4

full_data, pred_list = read.read(folder_paths, folder_names, filename, column_nr)[0], read.read(folder_paths, folder_names, filename, column_nr)[1]


def test_column_nr():
  assert len(pred_list) == column_nr, "The number of columns for the prediction data unit is incorrect, check the code to make sure all the desired prediction parameters are included in the final dataframe."
  
def test_model_nr():
  assert len(full_data.columns) == len(folder_names), "The number of models is not equal to the number of models specified in the input, check the input and the code."
 
def test_empty_data():
    i = pd.isna(full_data)

    for element in i.values:
        if element[0] == True:
            i = 1
            break
        else:
            i = 0

    assert i == 0, "The data contains empty cells. Please remove all empty cells, otherwise the comparisons may be invalid."
  

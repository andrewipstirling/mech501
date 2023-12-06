import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def read_data(file_path):
    try:
        # Read the tab-separated data into a pandas DataFrame
        data = pd.read_csv(file_path, sep='\t')
        return data
    except Exception as e:
        print(f"Error reading data: {str(e)}")
        return None
    
def store_data_np(data):
    try:
        # Extract each column and convert it to a NumPy array
        columns = data.columns
        arrays = [data[col].values for col in columns]
        return arrays
    except Exception as e:
        print(f"Error extracting columns: {str(e)}")
        return None

file_path = "./logger_out/progress.txt"
data = read_data(file_path)

array_list = store_data_np(data)
avg_ep_ret = array_list[0]
time = array_list[-1]

for col, array in zip(data.columns, array_list):
            print(f"{col}: {array}")



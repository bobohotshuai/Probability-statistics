import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def paint_data(i, path, name):
    df = pd.read_excel(path, sheet_name = 0, skiprows = i, nrows = 1, usecols = range(0, 1000), header = None)
    df.reset_index(drop=True, inplace=True)
    data = pd.concat([df[col] for col in df.columns], axis = 0)
    plt.hist(X, bins = 50, edgecolor = 'black')
    plt.hist(data, bins = 50, edgecolor = 'black')
    plt.savefig(name, bbox_inches = 'tight')
    plt.close()

n = [2, 3, 4, 5, 10, 20, 50, 100, 5000]
X = np.random.normal(0, 1, 1000)

path = './data2/u.xlsx'
paint_data(0, path, './pictures/2.png')
paint_data(8, path, './pictures/5000.png')
import pandas as pd
import matplotlib.pyplot as plt

def paint(i, path, name):
    df = pd.read_excel(path, sheet_name = 0, skiprows = i, nrows = 1, usecols = range(0, 1000), header = None)
    df.reset_index(drop=True, inplace=True)
    data = pd.concat([df[col] for col in df.columns], axis = 0)
    print(df)
    plt.hist(data, bins = 50, edgecolor = 'black')
    plt.savefig(name, bbox_inches = 'tight')
    plt.close()

n = [2, 3, 4, 5, 10, 20, 50, 100, 5000]

for i, _n in enumerate(n):
    path = './data2/u.xlsx'
    name = f'./pictures/{_n}.png'
    paint(i, path, name)
import pandas as pd
import matplotlib.pyplot as plt

def paint(path, name):
    df = pd.read_excel(path, sheet_name = 0, skiprows = 0, nrows = 50, usecols = range(0, 100))
    df.reset_index(drop=True, inplace=True)
    data = pd.concat([df[col] for col in df.columns], axis = 0)
    plt.hist(data, bins = 50, edgecolor = 'black')
    plt.savefig(name, bbox_inches = 'tight')
    plt.close()

_mu1, _mu2 = [-10, -1, 0, 5], [-5, 0, 1, 10]
_sigma1, _sigma2, _p = [0.1, 0.7, 2, 5], [0.1, 0.7, 2, 5], [0, 0.25, 0.75, 1]

paint('./data/origin_data.xlsx', './pictures/origin_data.png')

for i in _mu1:
    path = f'./data/mu1_{i}.xlsx'
    name = f'./pictures/mu1_{i}.png'
    paint(path, name)

for i in _mu2:
    path = f'./data/mu2_{i}.xlsx'
    name = f'./pictures/mu2_{i}.png'
    paint(path, name)

for i in _sigma1:
    path = f'./data/sigma1_{i}.xlsx'
    name = f'./pictures/sigma1_{i}.png'
    paint(path, name)

for i in _sigma2:
    path = f'./data/sigma2_{i}.xlsx'
    name = f'./pictures/sigma2_{i}.png'
    paint(path, name)

for i in _p:
    path = f'./data/p_{i}.xlsx'
    name = f'./pictures/p_{i}.png'
    paint(path, name)
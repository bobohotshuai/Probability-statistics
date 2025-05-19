import numpy as np
import pandas as pd
import time

def gauss(mu1, mu2, sigma1, sigma2, p, path):
    X = np.random.normal(mu1, sigma1, n)
    Y = np.random.normal(mu2, sigma2, n)
    nY = np.where(np.random.rand(n) < p, Y, 0)
    Z = X + nY
    Z = Z.reshape(50, 100)
    df = pd.DataFrame(Z)
    df.to_excel(path, index = False)

mu1, mu2, sigma1, sigma2, p = -5, 5, 1, 1, 0.5
n = 5000
np.random.seed(int(time.time()))
gauss(mu1, mu2, sigma1, sigma2, p, './data/origin_data.xlsx')

_mu1, _mu2 = [-10, -1, 0, 5], [-5, 0, 1, 10]
_sigma1, _sigma2, _p = [0.1, 0.7, 2, 5], [0.1, 0.7, 2, 5], [0, 0.25, 0.75, 1]

for i in _mu1:
    path = f'./data/mu1_{i}.xlsx'
    gauss(i, mu2, sigma1, sigma2, p, path)

for i in _mu2:
    path = f'./data/mu2_{i}.xlsx'
    gauss(mu1, i, sigma1, sigma2, p, path)

for i in _sigma1:
    path = f'./data/sigma1_{i}.xlsx'
    gauss(mu1, mu2, i, sigma2, p, path)

for i in _sigma2:
    path = f'./data/sigma2_{i}.xlsx'
    gauss(mu1, mu2, sigma1, i, p, path)

for i in _p:
    path = f'./data/p_{i}.xlsx'
    gauss(mu1, mu2, sigma1, sigma2, i, path)
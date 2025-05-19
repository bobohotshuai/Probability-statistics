import numpy as np
import pandas as pd
import time   

mu1, mu2, sigma1, sigma2= -5, 5, 1, 1
n = [2, 3, 4, 5, 10, 20, 50, 100, 5000]
EZ, DZ = -2.5, 7.75

np.random.seed(int(time.time()))

U = np.zeros((len(n), 1000))

for i, _n in enumerate(n):
    for j in range(1000):
        n_value = np.random.choice([0, 1], size = _n, p = [0.5, 0.5])
        X = np.random.normal(-5, 1, _n)
        Y = np.random.normal(5, 1, _n)
        Z = X + n_value * Y
        U[i, j] = (np.sum(Z) - _n * EZ) / np.sqrt(_n * DZ)

dt = pd.DataFrame(U)
dt.to_excel('./data2/u.xlsx', index = False, header = False)
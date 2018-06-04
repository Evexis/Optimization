from scipy import optimize
import numpy as np

def func(x, c0, c1):
    "Coordinate vector `x` should be an array of size two."
    return c0 * x[0]**2 + c1*x[1]**2


x = np.ones(2)

c0, c1 = (1, 200)
eps = np.sqrt(np.finfo(float).eps)

print(optimize.approx_fprime(x, func, [eps, np.sqrt(200) * eps], c0, c1))
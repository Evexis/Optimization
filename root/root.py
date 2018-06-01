from scipy import optimize
import numpy as np

def fun(x):
  return [x[0] + 0.5 * (x[0] - x[1])**3 -1.0, 0.5 * (x[1]-x[0])**3 + x[1]]

def jac(x):
  return np.array([[1 + 1.5 * (x[0] - x[1])**2,
                  -1.5 * (x[0] - x[1]**2)],
                  [-1.5 * (x[1] - x[0]) **2,
                  1 + 1.5 * (x[1] - x[0])**2]])

solution = optimize.root(fun, [0,0], jac=jac, method ='hybr')
solution.x
print(solution.x)

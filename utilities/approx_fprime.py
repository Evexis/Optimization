from scipy import optimize
import numpy as np

def func(x, a0, a1):
    "Coordinate vector `x` should be an array of size two."
    return a0 * x[0]**2 + a1*x[1]**2

x = np.ones(2)
print("Wektor wspolrzednych: ", x)

a0, a1 = (1, 200)
eps = np.sqrt(np.finfo(float).eps)
epsilon = [eps, np.sqrt(200) * eps]
print("Epsilon: ", epsilon)
print("""               f(xk[i] + epsilon[i]) - f(xk[i])
wzor: f'[i] = ---------------------------------
                         epsilon[i]""")
print("Wynik: ", optimize.approx_fprime(x, func, epsilon, a0, a1))
import numpy as np
from scipy.optimize import minimize

def objective(x):
    return x[0]*x[3]*(x[0]+x[1]+x[2])+x[2]

def constraint1(x):
    return x[0]*x[1]*x[2]*x[3]-25.0

def constraint3(x):
    return x[0]*x[1]*x[2]*x[3]-x[0]-30.0

def constraint2(x):
    sum_eq = 40.0
    for i in range(4):
        sum_eq = sum_eq - x[i]**2
    return sum_eq

# initial guesses
x0 = [1,3,5,1]

# show initial objective
print('Initial Objective: ' + str(objective(x0)))

# optimize
b = (1.0,5.0)
bounds = (b, b, b, b)
cons = [{'type': 'ineq', 'fun': constraint1}, \
        {'type': 'eq', 'fun': constraint2}, \
        {'type': 'ineq', 'fun': constraint3}]

solution = minimize(objective,x0,method='SLSQP', bounds=bounds,constraints=cons)
x = solution.x

# show final objective
print('Final Objective: ' + str(objective(x)))

# print solution
print('Solution')
print('x1 = ' + str(x[0]))
print('x2 = ' + str(x[1]))
print('x3 = ' + str(x[2]))
print('x4 = ' + str(x[3]))
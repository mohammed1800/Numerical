import pulp as p
import numpy as np
from scipy.optimize import minimize
from scipy.optimize import least_squares

def rosen (x):
    return sum(100.0*(x[1:]-x[:-1]**2.0)**2.0 + (1-x))

input = np.array([1,3])
res = least_squares(rosen, input)
print(res.x)

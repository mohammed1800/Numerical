import numpy as np 
import scipy.optimize as opt

def f(x):
    return -10*np.cos(np.pi*x-2.2)+(x+1.5)*x

x0=[-2]

minimizer_kwargs={"method":'BFGS'}
optimization_algorithm = opt.basinhopping(f,x0,minimizer_kwargs = minimizer_kwargs,niter = 200)
print("1-d function")
print(optimization_algorithm.message[0])

optimized_x = optimization_algorithm.x
optimized_fun = optimization_algorithm.fun

print ("Optimized x:",optimized_x)
print ("Optimized function value: ",optimized_fun)

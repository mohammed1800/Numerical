#Name: Mohammed Hashim Bin Yahya
#Roll no:20221429
#B.SC(H)computer science
#subject: Numerical optimization
#question 1


import numpy as np
from scipy.optimize import minimize_scalar

# Define the objective function
def objective_function(x):
    return x**2 - 4*x + 4

# Line Search method using scipy's minimize_scalar
def line_search_method():
    result = minimize_scalar(objective_function, method='bounded', bounds=(-10, 10))
    return result.x, result.fun

def main():
    # Find the optimal solution using Line Search method
    optimal_solution, optimal_value = line_search_method()

    # Display the results
    print("Optimal Solution:", optimal_solution)
    print("Optimal Value:", optimal_value)

if __name__ == "__main__":
    main()
#the output
#Optimal Solution: 2.0
#Optimal Value: 0.0

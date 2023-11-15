import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import linprog

def plot_constraints(x, y, inequalities, labels):
    for i in range(len(inequalities)):
        plt.plot(x, y(inequalities[i], x), label=labels[i])
        plt.fill_between(x, 0, y(inequalities[i], x), alpha=0.2)

def plot_feasible_region(x, y, inequalities, labels):
    plt.figure(figsize=(8, 8))
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    
    plot_constraints(x, y, inequalities, labels)
    
    plt.xlim(0, 10)
    plt.ylim(0, 10)
    
    plt.xlabel('x-axis')
    plt.ylabel('y-axis')
    
    plt.legend()
    plt.show()

def linear_programming_graphical_method(c, A, b):
    result = linprog(c, A_ub=A, b_ub=b)
    x = np.linspace(0, 10, 400)
    
    plt.plot(x, (result.fun - c[0]*x) / c[1], label="Objective Function", linestyle='--', color='red')
    
    plot_feasible_region(x, lambda inequality, x: eval(inequality), [f"{A[i][0]}*x + {A[i][1]}" for i in range(len(A))], [f"Constraint {i + 1}" for i in range(len(A))])

def main():
    # Example linear programming problem
    c = np.array([-2, -3])  # Coefficients of the objective function to be minimized (-2x - 3y)
    A = np.array([[2, 1], [4, -5]])  # Coefficients of the inequality constraints (2x + y <= 10, 4x - 5y <= 8)
    b = np.array([10, 8])  # Right-hand side of the inequalities
    
    linear_programming_graphical_method(c, A, b)

if __name__ == "__main__":
    main()

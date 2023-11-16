#Name: Mohammed Hashim Bin Yahya
#Roll no:20221429
#B.SC(H)computer science
#subject: Numerical optimization
#question 1
import numpy as np

def objective_function(x):
    return -10 * np.cos(np.pi * x - 2.2) + (x + 1.5) * x

def gradient_descent(learning_rate, max_iterations, tolerance):
    x = np.random.uniform(-10, 10)  # Initialize x randomly
    for _ in range(max_iterations):
        gradient = -np.pi * 10 * np.sin(np.pi * x - 2.2) + 2 * x + 1.5
        x = x - learning_rate * gradient
        if np.abs(gradient) < tolerance:
            break
    return x, objective_function(x)

def main():
    learning_rate = 0.1
    max_iterations = 1000
    tolerance = 1e-6

    optimal_solution, optimal_value = gradient_descent(learning_rate, max_iterations, tolerance)

    print("Global Optimal Solution:", optimal_solution)
    print("Global Optimal Value:", optimal_value)

if __name__ == "__main__":
    main()
#the output:
#Global Optimal Solution: 0.8229260984375801
#Global Optimal Value: -7.3552660380966275

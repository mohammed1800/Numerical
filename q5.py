import numpy as np
import matplotlib.pyplot as plt

def objective_function(x):
    return -10 * np.cos(np.pi * x - 2.2) + (x + 1.5) * x

def plot_function():
    x = np.linspace(-10, 10, 1000)
    y = objective_function(x)

    plt.plot(x, y, label='Objective Function')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('Graph of the Objective Function')
    plt.legend()
    plt.grid(True)
    plt.show()

def main():
    plot_function()

if __name__ == "__main__":
    main()

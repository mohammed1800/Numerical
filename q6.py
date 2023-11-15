from scipy.optimize import minimize

# Define the objective function
def objective_function(x):
    return x[0]**2 + x[1]**2  # Example: minimize x^2 + y^2

# Define the equality constraint
def equality_constraint(x):
    return x[0] + x[1] - 1  # Example: x + y = 1

# Define the inequality constraint
def inequality_constraint(x):
    return x[0] - x[1]  # Example: x - y >= 0

# Initial guess
initial_guess = [0, 0]

# Set constraints
constraints = [
    {'type': 'eq', 'fun': equality_constraint},
    {'type': 'ineq', 'fun': inequality_constraint}
]

# Solve the optimization problem
result = minimize(objective_function, initial_guess, constraints=constraints)

# Display the result
print("Optimal Solution:", result.x)
print("Optimal Value:", result.fun)

#the output:
from scipy.optimize import minimize

# Define the objective function
def objective_function(x):
    return x[0]**2 + x[1]**2  # Example: minimize x^2 + y^2

# Define the equality constraint
def equality_constraint(x):
    return x[0] + x[1] - 1  # Example: x + y = 1

# Define the inequality constraint
def inequality_constraint(x):
    return x[0] - x[1]  # Example: x - y >= 0

# Initial guess
initial_guess = [0, 0]

# Set constraints
constraints = [
    {'type': 'eq', 'fun': equality_constraint},
    {'type': 'ineq', 'fun': inequality_constraint}
]

# Solve the optimization problem
result = minimize(objective_function, initial_guess, constraints=constraints)

# Display the result
#print("Optimal Solution:", result.x)
#print("Optimal Value:", result.fun)

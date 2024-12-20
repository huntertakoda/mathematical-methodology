import numpy as np
from scipy.optimize import minimize
import pandas as pd

# load dataset

file_path = "C:/puredata/mathematical_methodology_dataset.csv"
data = pd.read_csv(file_path)

# define the objective function to minimize

def objective_function(params):
    """quadratic function for optimization."""
    x, y = params
    return (x - 3)**2 + (y + 2)**2

# perform optimization using scipy's minimize

initial_guess = [0, 0]
result = minimize(objective_function, initial_guess, method='BFGS')

# retrieve optimized values and the minimum value

optimized_params = result.x
min_value = result.fun

# save the optimization results

output_path = "C:/puredata/optimization_algorithms_results.txt"
with open(output_path, "w") as f:
    f.write("optimization results:\n")
    f.write(f"optimized parameters: {optimized_params}\n")
    f.write(f"minimum value: {min_value}\n")
    f.write(f"success: {result.success}\n")
    f.write(f"message: {result.message}\n")

print(f"optimization algorithms completed. results saved to {output_path}.")

from scipy.optimize import minimize
import numpy as np

# define the objective function

def objective_function(x):
    return x[0]**2 + x[1]**2 + np.sin(5 * x[0]) * np.cos(5 * x[1])

# define constraints and bounds

bounds = [(-2, 2), (-2, 2)]
initial_guess = [0, 0]

# perform optimization

result = minimize(objective_function, initial_guess, bounds=bounds)

# display results

print("Optimization Result:")
print(f"Optimal Point: {result.x}")
print(f"Objective Function Value: {result.fun}")

# save results

with open("C:/puredata/nonlinear_optimization_results.txt", "w") as f:
    f.write(f"Optimal Point: {result.x}\n")
    f.write(f"Objective Function Value: {result.fun}\n")

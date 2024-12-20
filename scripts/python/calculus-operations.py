import numpy as np
import sympy as sp

# load the dataset

file_path = "C:/puredata/mathematical_methodology_dataset.csv"
data = np.genfromtxt(file_path, delimiter=',', skip_header=1)

x_values = data[:, 0]
y_values = data[:, 1]

# symbolic differentiation

x = sp.symbols('x')
y_function = 3 * x**2 + 2 * x - 5  # example function
y_derivative = sp.diff(y_function, x)

# symbolic integration

y_integral = sp.integrate(y_function, x)

# numerical differentiation

dy_dx = np.gradient(y_values, x_values)

# numerical integration

area_under_curve = np.trapz(y_values, x_values)

# save results

output_path = "C:/puredata/calculus_operations_results.txt"
with open(output_path, 'w') as f:
    f.write("Symbolic Differentiation:\n")
    f.write(f"Function: {y_function}\n")
    f.write(f"Derivative: {y_derivative}\n\n")

    f.write("Symbolic Integration:\n")
    f.write(f"Integral: {y_integral}\n\n")

    f.write("Numerical Differentiation:\n")
    f.write(f"dy/dx: {dy_dx}\n\n")

    f.write("Numerical Integration:\n")
    f.write(f"Area under curve: {area_under_curve}\n")

print(f"calculus operations completed. results saved to {output_path}.")

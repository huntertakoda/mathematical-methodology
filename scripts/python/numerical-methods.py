import pandas as pd
import numpy as np
from scipy.interpolate import interp1d
from scipy.optimize import root_scalar
from scipy.integrate import simps

# load the dataset

file_path = "C:/puredata/mathematical_methodology_dataset.csv"
data = pd.read_csv(file_path)

# interpolation: create a function to estimate z_values for given x_values

def interpolate_values(x, y, x_new):
    f_interp = interp1d(x, y, kind='cubic', fill_value='extrapolate')
    y_new = f_interp(x_new)
    return y_new

x_values = data['x_values']
z_values = data['z_values']
x_new = np.linspace(min(x_values), max(x_values), 100)
z_interpolated = interpolate_values(x_values, z_values, x_new)

# root-finding: find root for a polynomial approximation of y_values

poly_coeffs = np.polyfit(x_values, data['y_values'], deg=3)
poly_func = np.poly1d(poly_coeffs)

# search for a wider bracket to ensure opposite signs

bracket = [min(x_values), max(x_values)]
if poly_func(bracket[0]) * poly_func(bracket[1]) > 0:
    print("No root found in the bracket. Adjusting...")
    bracket = [bracket[0] - 1, bracket[1] + 1]

try:
    root_result = root_scalar(poly_func, bracket=bracket, method='brentq')
    root_value = root_result.root if root_result.converged else None
except ValueError:
    root_value = None
    print("Root finding failed. Please check the data or adjust the method.")

# numerical integration: calculate area under y_values using simpson's rule

area_under_curve = simps(data['y_values'], x=x_values)

# save results

output_path = "C:/puredata/numerical_methods_results.txt"
with open(output_path, "w") as f:
    f.write("interpolation results (sample):\n")
    for i, x in enumerate(x_new[:10]):
        f.write(f"x: {x:.4f}, z_interpolated: {z_interpolated[i]:.4f}\n")
    
    f.write(f"\nroot of polynomial (y_values): {root_value}\n")
    f.write(f"\narea under curve (y_values): {area_under_curve:.4f}\n")

print(f"numerical methods completed. results saved to {output_path}.")



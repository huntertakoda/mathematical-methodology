import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# load dataset
file_path = "C:/puredata/mathematical_methodology_dataset.csv"
data = pd.read_csv(file_path)

# define mathematical models
def linear_model(x, a, b):
    return a * x + b

def quadratic_model(x, a, b, c):
    return a * x**2 + b * x + c

def exponential_model(x, a, b, c):
    return a * np.exp(b * x) + c

# fit models
x_data = data['x_values']
y_data = data['y_values']

models = {
    "Linear Model": linear_model,
    "Quadratic Model": quadratic_model,
    "Exponential Model": exponential_model
}

fit_results = {}
for name, model in models.items():
    try:
        params, _ = curve_fit(model, x_data, y_data)
        fit_results[name] = params
        print(f"{name} parameters: {params}")
    except Exception as e:
        print(f"Failed to fit {name}: {e}")

# save results
results_path = "C:/puredata/mathematical_modeling_results.txt"
with open(results_path, "w") as f:
    for name, params in fit_results.items():
        f.write(f"{name} parameters: {params}\n")

# visualize fits
plt.figure(figsize=(10, 6))
plt.scatter(x_data, y_data, label="Data", color="black", alpha=0.6)

x_fit = np.linspace(min(x_data), max(x_data), 500)
for name, model in models.items():
    if name in fit_results:
        y_fit = model(x_fit, *fit_results[name])
        plt.plot(x_fit, y_fit, label=name)

plt.xlabel("X Values")
plt.ylabel("Y Values")
plt.title("Mathematical Modeling Fits")
plt.legend()
plt.savefig("C:/puredata/mathematical_modeling_fits.png")
plt.show()

print(f"Mathematical modeling completed. Results saved to {results_path}.")

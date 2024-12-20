import numpy as np
import pandas as pd

# load the dataset

file_path = "C:/puredata/mathematical_methodology_dataset.csv"
data = pd.read_csv(file_path)

# extract matrices for linear algebra operations

x_values = data['x_values'].values
y_values = data['y_values'].values
z_values = data['z_values'].values

# create a matrix combining x, y, and z values

matrix = np.column_stack((x_values, y_values, z_values))

# calculate the transpose of the matrix

transpose_matrix = matrix.T

# calculate the dot product of the matrix with its transpose

dot_product = np.dot(matrix, transpose_matrix)

# perform eigen decomposition on the dot product

eigenvalues, eigenvectors = np.linalg.eig(dot_product)

# calculate the determinant of the matrix

determinant = np.linalg.det(dot_product)

# save results

output_path = "C:/puredata/linear_algebra_results.txt"
with open(output_path, "w") as f:
    f.write("Linear Algebra Results:\n\n")
    f.write("Original Matrix:\n")
    f.write(f"{matrix}\n\n")
    f.write("Transpose Matrix:\n")
    f.write(f"{transpose_matrix}\n\n")
    f.write("Dot Product:\n")
    f.write(f"{dot_product}\n\n")
    f.write("Eigenvalues:\n")
    f.write(f"{eigenvalues}\n\n")
    f.write("Eigenvectors:\n")
    f.write(f"{eigenvectors}\n\n")
    f.write("Determinant:\n")
    f.write(f"{determinant}\n")

print(f"Linear algebra completed. Results saved to {output_path}.")

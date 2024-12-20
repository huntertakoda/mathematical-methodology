import numpy as np
import pandas as pd

# generate a random matrix

matrix = np.random.rand(5, 5)

# perform svd decomposition

u, s, vh = np.linalg.svd(matrix)

# perform lu decomposition

from scipy.linalg import lu
p, l, u = lu(matrix)

# perform eigendecomposition

eigenvalues, eigenvectors = np.linalg.eig(matrix)

# save results

with open("C:/puredata/matrix_decompositions_results.txt", "w") as f:
    f.write("SVD Decomposition:\n")
    f.write(f"U:\n{u}\nS:\n{s}\nVH:\n{vh}\n\n")
    f.write("LU Decomposition:\n")
    f.write(f"P:\n{p}\nL:\n{l}\nU:\n{u}\n\n")
    f.write("Eigendecomposition:\n")
    f.write(f"Eigenvalues:\n{eigenvalues}\nEigenvectors:\n{eigenvectors}\n")

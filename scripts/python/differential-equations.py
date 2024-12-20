import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

# define the differential equation dy/dt = -y + 2

def differential_equation(t, y):
    return -y + 2

# solve the equation using an initial condition

solution = solve_ivp(differential_equation, [0, 10], [1], t_eval=np.linspace(0, 10, 100))

# plot the solution

plt.figure(figsize=(10, 6))
plt.plot(solution.t, solution.y[0], label='y(t)')
plt.title('Differential Equation Solution')
plt.xlabel('Time (t)')
plt.ylabel('y(t)')
plt.grid()
plt.legend()
plt.show()

# save results

np.savetxt("C:/puredata/differential_equations_results.csv", np.c_[solution.t, solution.y[0]], delimiter=",", header="time,y(t)", comments="")

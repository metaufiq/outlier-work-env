import numpy as np
import matplotlib.pyplot as plt
from pycav import Interval

Interval

# Define the domain and grid points
L = 1.0  # Length of the domain
N = 100  # Number of grid points
x = np.linspace(0, L, N)  # Grid points

# Define the boundary conditions
T_left = 100.0  # Temperature at the left boundary
T_right = 0.0  # Temperature at the right boundary

# Create the model
model = FDModel(x)

# Define the thermal diffusivity
alpha = 1.0

# Define the steady-state heat equation
def heat_equation(T):
    return alpha * T.dx2

# Add the equation to the model
model.add_equation(heat_equation)

# Apply boundary conditions
model.add_bc(DirichletBC(T_left, x=0))  # Left boundary
model.add_bc(DirichletBC(T_right, x=L))  # Right boundary

# Solve the equation
T_solution = model.solve(T0=np.zeros_like(x))  # Initial guess of zeros

# Plot the results
plt.plot(x, T_solution, label='Temperature')
plt.xlabel('x')
plt.ylabel('Temperature')
plt.title('1D Steady-State Heat Conduction Solution')
plt.legend()
plt.show()
import numpy as np
import matplotlib.pyplot as plt

# Define the grid range
x = np.linspace(-5, 5, 20)  # x-values
y = np.linspace(-5, 5, 20)  # y-values
X, Y = np.meshgrid(x, y)    # Create a grid

# Define the vector field (F = (u, v))
u = -Y                      # Component in the x-direction
v = X                       # Component in the y-direction

# Plot the vector field
plt.figure(figsize=(8, 6))
plt.quiver(X, Y, u, v, color="blue", angles="xy", scale_units="xy", scale=1)
plt.title("Vector Field")
plt.xlabel("x")
plt.ylabel("y")
plt.xlim(-6, 6)
plt.ylim(-6, 6)
plt.grid()
plt.axhline(0, color='black', linewidth=0.5)  # Add x-axis (horisontal line)
plt.axvline(0, color='black', linewidth=0.5)  # Add y-axis (vertical line)
plt.show()


import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm

def heat_equation_3d(dx=0.1, dy=0.1, dt=0.01, Lx=2.0, Ly=2.0, T=2.0, alpha=0.01):
    # Set up spatial and temporal grids
    nx, ny = int(Lx/dx), int(Ly/dy)
    nt = int(T/dt)
    
    x = np.linspace(0, Lx, nx)
    y = np.linspace(0, Ly, ny)
    X, Y = np.meshgrid(x, y)

    # Initialize temperature field
    u = np.zeros((nx, ny))

    # Initial condition: heat at the center
    u[nx//2, ny//2] = 100.0

    # Simulation loop
    for _ in range(nt):
        u_new = u.copy()
        # Update the temperature field
        for i in range(1, nx-1):
            for j in range(1, ny-1):
                u_new[i, j] = u[i, j] + alpha * dt * (
                    (u[i+1, j] - 2*u[i, j] + u[i-1, j]) / dx**2 +
                    (u[i, j+1] - 2*u[i, j] + u[i, j-1]) / dy**2
                )
        u = u_new

    # 3D Visualization
    fig = plt.figure(figsize=(10, 7))
    ax = fig.add_subplot(111, projection='3d')
    
    surf = ax.plot_surface(X, Y, u, cmap=cm.viridis, edgecolor='none')
    ax.set_title('Heat Equation Simulation (3D)')
    ax.set_xlabel('X-axis')
    ax.set_ylabel('Y-axis')
    ax.set_zlabel('Temperature')
    fig.colorbar(surf, ax=ax, shrink=0.5, aspect=10)

    plt.show()

if __name__ == "__main__":
    heat_equation_3d()


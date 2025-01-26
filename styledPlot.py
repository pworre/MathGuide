import matplotlib.pyplot as plt
import numpy as np

# Defining the function used to plot
def function(t):
    return 25 * (1 - np.e ** (-4 * t))

# Creating the x-values for the time-axis
x = np.linspace(0, 5, 100)

# Plotting
plt.figure(figsize=(10, 6))  # Larger figure for better visibility
plt.plot(x, function(x), label="Voltage: $f(t) = 25(1 - e^{-4t})$", color="teal", linewidth=2, linestyle="--")

# Highlight a key point (e.g., steady state at t=5)
steady_state = function(5)		# Signing the y-value to a variable to be used in scatter
plt.scatter([5], [steady_state], color="red", zorder=5)
plt.text(5, steady_state + 1, f"Steady State: {steady_state:.2f} V", fontsize=10, color="red")

# Add labels and title
plt.xlabel("Time [s]", fontsize=12)
plt.ylabel("Voltage [V]", fontsize=12)
plt.title("Conductor's Voltage Over Time", fontsize=14, fontweight="bold")

# Customize grid and legend
plt.grid(True, linestyle="--", alpha=0.7)
plt.legend(fontsize=10, loc="lower right")

# Add minor ticks for better resolution
plt.minorticks_on()
plt.grid(which="minor", linestyle=":", alpha=0.5)

# Show the plot
plt.show()


import matplotlib.pyplot as plt
import numpy as np

# Defining the function used to plot
def function(t):
	return 25 * (1 - np.e ** (-4 * t))

# Creating the x-values for the time-axis
x = np.linspace(0, 5, 100)

# Plotting
plt.plot(x, function(x), label="f(t)")
plt.xlabel("Time [s]")
plt.ylabel("Voltage [V]")
plt.title("Conducter's Voltage")
plt.legend()
plt.grid()
plt.show()



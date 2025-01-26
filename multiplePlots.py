import matplotlib.pyplot as plt
import numpy as np

# Step 1: Prepare some data for the plots
# Generate some x values
x = np.linspace(0, 10, 100)

# Define y values for two different plots
y1 = np.sin(x)  # First plot: Sine wave
y2 = np.cos(x)  # Second plot: Cosine wave

# Step 2: Create a figure
# The `plt.figure()` function creates a new figure window
fig = plt.figure(figsize=(10, 5))  # Optional: Set the size of the figure

# Step 3: Add the first subplot
# Use `add_subplot()` to create a subplot in the figure
# The arguments (1, 2, 1) mean:
#   - 1 row of plots
#   - 2 columns of plots
#   - This is the 1st plot
ax1 = fig.add_subplot(1, 2, 1)
ax1.plot(x, y1, label="sin(x)", color="blue")  # Plot sine wave
ax1.set_title("Sine Wave")  # Add a title
ax1.set_xlabel("x")  # Label for the x-axis
ax1.set_ylabel("y")  # Label for the y-axis
ax1.legend()  # Show the legend

# Step 4: Add the second subplot
# The arguments (1, 2, 2) mean:
#   - 1 row of plots
#   - 2 columns of plots
#   - This is the 2nd plot
ax2 = fig.add_subplot(1, 2, 2)
ax2.plot(x, y2, label="cos(x)", color="red")  # Plot cosine wave
ax2.set_title("Cosine Wave")  # Add a title
ax2.set_xlabel("x")  # Label for the x-axis
ax2.set_ylabel("y")  # Label for the y-axis
ax2.legend()  # Show the legend

# Step 5: Adjust layout for better spacing
# Use `plt.tight_layout()` to prevent overlap between subplots
plt.tight_layout()

# Step 6: Display the figure
# Use `plt.show()` to render the figure in a window or output cell (if in Jupyter)
plt.show()

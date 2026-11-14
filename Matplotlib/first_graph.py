
import numpy as np
import matplotlib.pyplot as plt

# Create x values
x = np.arange(0, 10, 0.1)

# Calculate y values
y = x ** 2

# Draw the graph
plt.plot(x, y, color='red', label='y = x²')

# Add title and labels
plt.title("My First Graph")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")

plt.legend()
plt.grid()

# Display the graph
plt.show()

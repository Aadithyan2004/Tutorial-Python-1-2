import matplotlib.pyplot as plt

# Data for the lines
x = [0, 1, 2, 3, 4, 5]
y1 = [0, 1, 4, 9, 16, 25]  # First line (y = x^2)
y2 = [0, 1, 2, 3, 4, 5]    # Second line (y = x)

# Plotting both lines
plt.plot(x, y1, label='y = x^2', color='blue', linestyle='-', marker='o')  # First line with label
plt.plot(x, y2, label='y = x', color='red', linestyle='--', marker='x')     # Second line with label

# Adding labels and title
plt.xlabel('X-Axis Label')
plt.ylabel('Y-Axis Label')
plt.title('Multiple Lines Plot')

# Adding legend
plt.legend()

# Display the plot
plt.show()

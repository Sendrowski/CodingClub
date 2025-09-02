import matplotlib.pyplot as plt
import numpy as np
# Sample data
x = np.linspace(0, 10, 100)
y = np.cos(x)
data = np.random.rand(10, 10)
# Creating a figure and two subplots
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(5, 12))
# First subplot - Line Plot
ax1.plot(x, y, label='Cosine Function')
ax1.set_title("Line Plot")
ax1.legend()
# Second subplot - Heatmap
cax = ax2.matshow(data, cmap='viridis')
cbar = fig.colorbar(cax, ax=ax2, fraction=0.046, pad=0.04)
cbar.set_label('Colorbar')
ax2.set_title("Heatmap with Colorbar")
# Show the plot
fig.show()

pass
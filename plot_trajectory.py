import matplotlib.pyplot as plt
'''
def plot_trajectory(tr, title):
    # Extracting x and y coordinates for each trajectory
    x, y = tr[:, 1], tr[:, 2]

    plt.figure(figsize=(10, 6))
    plt.plot(x,y, marker='o', markersize=5, linestyle='-', linewidth=1.5)

    plt.title(title)
    plt.xlabel('X Coordinate')
    plt.ylabel('Y Coordinate')
    plt.legend()
    plt.grid(True)
    plt.show()
'''

import matplotlib.pyplot as plt
import numpy as np

def plot_trajectory(tr, times, title):
    # Extracting x and y coordinates for each trajectory
    x, y = tr[:, 1], tr[:, 2]
    # Color based on time
    colors = times / max(times)  # Normalize times to range [0,1] for color mapping

    plt.figure(figsize=(10, 6))
    scatter = plt.scatter(x, y, c=colors, cmap='viridis', edgecolor='k', marker='o')
    plt.colorbar(scatter, label='Time (normalized)')

    plt.title(title)
    plt.xlabel('X Coordinate')
    plt.ylabel('Y Coordinate')
    plt.grid(True)
    plt.show()



import matplotlib.pyplot as plt
from CRS03_a import trajectory, t
from CRS03_b_2 import trajectory_minus, trajectory_plus


# Assuming 'trajectory', 'trajectory_plus', and 'trajectory_minus' are already computed
def plot_trajectories(original, plus, minus, times):
    # Color based on time
    colors = times / max(times)

    # Extracting x and y coordinates for each trajectory
    x_original, y_original = original[:, 1], original[:, 2]
    x_plus, y_plus = plus[:, 1], plus[:, 2]
    x_minus, y_minus = minus[:, 1], minus[:, 2]

    plt.figure(figsize=(12, 8))
    plt.scatter(x_original, y_original, c=colors, cmap='viridis', label='Original', s=10)
    plt.scatter(x_plus, y_plus, c=colors, cmap='cool', label='vl + 0.01', s=10)
    plt.scatter(x_minus, y_minus, c=colors, cmap='autumn', label='vl - 0.01', s=10)
    
    plt.title('Comparison of Robot Trajectories')
    plt.xlabel('X Coordinate')
    plt.ylabel('Y Coordinate')
    plt.legend()
    plt.grid(True)
    plt.savefig('robot_trajectories.png', format='png', dpi=300)  # Adjust dpi according to the quality you need
    
    plt.show()

# Call the function to plot trajectories
#plot_trajectories(trajectory, trajectory_plus, trajectory_minus)

plot_trajectories(trajectory, trajectory_plus, trajectory_minus,t)

import matplotlib.pyplot as plt
from CRS03_a import trajectory 
from CRS03_b_2 import trajectory_minus, trajectory_plus


# Assuming 'trajectory', 'trajectory_plus', and 'trajectory_minus' are already computed
def plot_trajectories(original, plus, minus):
    # Color based on time

    # Extracting x and y coordinates for each trajectory
    x_original, y_original = original[:, 1], original[:, 2]
    x_plus, y_plus = plus[:, 1], plus[:, 2]
    x_minus, y_minus = minus[:, 1], minus[:, 2]

    plt.figure(figsize=(10, 6))
    plt.plot(x_original, y_original, label='Original vl', marker='o', markersize=5, linestyle='-', linewidth=1.5)
    plt.plot(x_plus, y_plus, label='vl + 0.01', marker='x', markersize=5, linestyle='--', linewidth=1.5)
    plt.plot(x_minus, y_minus, label='vl - 0.01', marker='s', markersize=5, linestyle='-.', linewidth=1.5)

    plt.title('Comparison of Robot Trajectories')
    plt.xlabel('X Coordinate')
    plt.ylabel('Y Coordinate')
    plt.legend()
    plt.grid(True)
    plt.show()

# Call the function to plot trajectories
#plot_trajectories(trajectory, trajectory_plus, trajectory_minus)

plot_trajectories(trajectory, trajectory_plus, trajectory_minus)
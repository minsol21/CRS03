'''
b) Calculate two additional trajectories 
for the whole time interval (t ∈ [0,3]), 
one for vl + 0.01 and one for vl - 0.01, 
but using the integrated equations 4, 5, and 6 now.
'''

import numpy as np
from plot_trajectory import plot_trajectory
# Constants and conditions
phi0 = 0
x0 = 0
y0 = 0

# Given constants and initial conditions
b = 0.05
x0 = 0
y0 = 0
phi0 = 0

delta_t = 0.01
T = 3

# Time array
t = np.arange(0, T + delta_t, delta_t)

vr = np.array([1.0 if time <= 1 else 0.9 for time in t])
vl = np.array([0.9 if time <= 1 else 1.0 for time in t])

# Create trajectories with original vl, vl + 0.01, and vl - 0.01
vl_plus = np.array([vel + 0.01 for vel in vl])
vl_minus = np.array([vel - 0.01 for vel in vl])


# Functions for φ(t), x(t), y(t) based on equations 4, 5, 6
def phi_t(vr, vl, b, t, phi0):
    #Calculate the angular position of the robot at time t
    phi_t=((vr - vl) / b) * t + phi0
    return phi_t

def x_t(vr, vl, b, t, phi0, x0):
    #Calculate the x-coordinate of the robot at time t
    phi = phi_t(vr, vl, b, t, phi0)
    if vr == vl:
        return x0 + vr * t * np.cos(phi0)  # Straight line case
    x_t= x0 + (b * (vr + vl) / (2 * (vr - vl))) * (np.sin(phi) - np.sin(phi0))
    return x_t

def y_t(vr, vl, b, t, phi0, y0):
    #Calculate the y-coordinate of the robot at time t
    phi = phi_t(vr, vl, b, t, phi0)
    if vr == vl:
        return y0 + vr * t * np.sin(phi0)  # Straight line case
    y_t= y0 - (b * (vr + vl) / (2 * (vr - vl))) * (np.cos(phi) - np.cos(phi0))
    return y_t


# Calculate trajectories for vl + 0.01 and vl - 0.01
x_plus = np.array([x_t(vr[i], vl_plus[i], b, t[i], phi0, x0) for i in range(len(t))])
y_plus = np.array([y_t(vr[i], vl_plus[i], b, t[i], phi0, y0) for i in range(len(t))])
phi_plus = np.array([phi_t(vr[i], vl_plus[i], b, t[i], phi0) for i in range(len(t))])

x_minus = np.array([x_t(vr[i], vl_minus[i], b, t[i], phi0, x0) for i in range(len(t))])
y_minus = np.array([y_t(vr[i], vl_minus[i], b, t[i], phi0, y0) for i in range(len(t))])
phi_minus = np.array([phi_t(vr[i], vl_minus[i], b, t[i], phi0) for i in range(len(t))])

# Combine into trajectories
trajectory_plus = np.column_stack((t, x_plus, y_plus, phi_plus))
trajectory_minus = np.column_stack((t, x_minus, y_minus, phi_minus))


def print_trajectory(trajectory):
    """Prints the trajectory array with values formatted to four decimal places."""
    for entry in trajectory:
        formatted_entry = " ".join(f"{value:.4f}" for value in entry)
        print(formatted_entry)

# Assuming the trajectories have been calculated as in previous examples
print("=====Trajectory with vl + 0.01 :=====")
print_trajectory(trajectory_plus)
print("======================================\n\n")

print("=====Trajectory with vl - 0.01 :=====")
print_trajectory(trajectory_minus)
print("======================================")


# Example usage:
# Assuming 'trajectory' and 't' are defined from your simulation
plot_trajectory(trajectory_minus, t, "Robot Trajectory MINUS with Gradient Color")
plot_trajectory(trajectory_plus, t, "Robot Trajectory PLUS with Gradient Color")


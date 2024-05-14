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

# Assuming the equations and variables are already defined

def integrate_trajectory(vr, vl, b, t, x0, y0, phi0):
    # Initialize arrays for storing trajectory data
    x = np.zeros_like(t)
    y = np.zeros_like(t)
    phi = np.zeros_like(t)
    
    # Set initial conditions
    x[0], y[0], phi[0] = x0, y0, phi0
    
    # Integrate using the kinematic equations
    for i in range(1, len(t)):
        dt = t[i] - t[i - 1]
        phi[i] = phi[i - 1] + ((vr[i - 1] - vl[i - 1]) / b) * dt
        x[i] = x[i - 1] + ((vr[i - 1] + vl[i - 1]) / 2) * np.cos(phi[i - 1]) * dt
        y[i] = y[i - 1] + ((vr[i - 1] + vl[i - 1]) / 2) * np.sin(phi[i - 1]) * dt
    
    return x, y, phi

# Example of splitting the integration at t = 1
index_at_1 = np.where(t == 1)[0][0]  # Get the index where t = 1
# Integrate from 0 to 1
x1, y1, phi1 = integrate_trajectory(vr[:index_at_1+1], vl[:index_at_1+1], b, t[:index_at_1+1], x0, y0, phi0)
# Use the final values from the first segment as new initial conditions
x0_new, y0_new, phi0_new = x1[-1], y1[-1], phi1[-1]
# Integrate from 1 to end
x2, y2, phi2 = integrate_trajectory(vr[index_at_1:], vl[index_at_1:], b, t[index_at_1:], x0_new, y0_new, phi0_new)

# Combine both segments
x_full = np.concatenate([x1[:-1], x2])
y_full = np.concatenate([y1[:-1], y2])
phi_full = np.concatenate([phi1[:-1], phi2])


# Calculate trajectories for vl + 0.01 and vl - 0.01
x_plus, y_plus, phi_plus= integrate_trajectory(vr, vl_plus,b, t, x0, y0, phi0)
x_minus, y_minus, phi_minus= integrate_trajectory(vr, vl_minus,b, t, x0, y0, phi0)

# Combine into trajectories
trajectory_plus = np.column_stack((t, x_plus, y_plus, phi_plus))
trajectory_minus = np.column_stack((t, x_minus, y_minus, phi_minus))


# Example usage:
# Assuming 'trajectory' and 't' are defined from your simulation
#plot_trajectory(trajectory_minus, t, "Robot Trajectory MINUS with Gradient Color")
#plot_trajectory(trajectory_plus, t, "Robot Trajectory PLUS with Gradient Color")


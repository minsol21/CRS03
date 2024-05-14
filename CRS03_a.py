'''
a) Calculate the robot\'s trajectory 
for the above setting using equations 1, 2, and 3.
'''
import matplotlib.pyplot as plt
import numpy as np
from plot_trajectory import plot_trajectory

# Given constants and initial conditions
b = 0.05
x0 = 0
y0 = 0
phi0 = 0

delta_t = 0.01
T = 3

# Time array
t = np.arange(0, T + delta_t, delta_t)

# Wheel velocities
vr = np.array([1.0 if time <= 1 else 0.9 for time in t])
vl = np.array([0.9 if time <= 1 else 1.0 for time in t])

# Kinematic equations:
# dx/dt = ((vr + vl) / 2) * cos(phi)
# dy/dt = ((vr + vl) / 2) * sin(phi)
# dphi/dt = (vr - vl) / b

# Initialize x, y, phi arrays with zeros
x = np.zeros(len(t))
y = np.zeros(len(t))
phi = np.zeros(len(t))

x[0] = x0
y[0] = y0
phi[0] = phi0

# Numerical integration using Euler's method
for i in range(1, len(t)):
    phi[i] = phi[i-1] + ((vr[i-1] - vl[i-1]) / b) * delta_t
    x[i] = x[i-1] + ((vr[i-1] + vl[i-1]) / 2) * np.cos(phi[i-1]) * delta_t
    y[i] = y[i-1] + ((vr[i-1] + vl[i-1]) / 2) * np.sin(phi[i-1]) * delta_t

# Create a trajectory array that combines t, x, y, phi
trajectory = np.column_stack((t, x, y, phi))

# Displaying only the first 10 entries for clarity
print('============The Robot\'s Trajectory============')
print('|  time t   |     x     |     y     |    phi    |')
print(trajectory[:10])  
print('...\n...\n...\n...')
print(trajectory[290:])  


# Example usage:
# Assuming 'trajectory' and 't' are defined from your simulation
#plot_trajectory(trajectory, t, "Robot Trajectory with Gradient Color")

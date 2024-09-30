import numpy as np
import matplotlib.pyplot as plt

#Parameters and constants
T = 30
dt = 0.1
r=0.1
l=25

#Simulate using velocity profiles
def simulate_variable_velocity():
    #Initial Variables
    time_steps = int(T / dt)
    traj = np.zeros((time_steps, 3))  # 0 matrix to store x, y and theta at each step
    x, y, theta = 0, 0, 0  # Initial state
    v = 1 # v at t=0
    omega = 0.7 # omega at t=0
    counter = 0 #to keep track of time

    for i in range(time_steps):
        traj[i, :] = [x, y, theta]
        x += v * np.cos(theta) * dt #Updating X position
        y += v * np.sin(theta) * dt #Updating Y position
        theta += omega * dt #Updating angle
        counter += 1
        v = 1 + 0.1*np.sin(counter*dt) #updating v at next time step
        omega = 0.2 + 0.5*np.cos(counter*dt) #updating omega at next time step
        
    return traj
#Simulate using constant velocity
def simulate_constant_velocity(v, omega, T, dt):
    #Initial Variables
    time_steps = int(T / dt)
    traj = np.zeros((time_steps, 3))  # 0 matrix to store x, y and theta at each step
    x, y, theta = 0, 0, 0  # Initial state

    for i in range(time_steps):
        traj[i, :] = [x, y, theta]
        x = x + v * np.cos(theta) * dt #Updating X position
        y = y + v * np.sin(theta) * dt #Updating Y position
        theta = theta + omega * dt #Updating angle
    return traj

def plot_trajectory(traj, title):
    plt.figure()
    plt.plot(traj[:, 0], traj[:, 1])
    plt.xlabel("X position [m]")
    plt.ylabel("Y position [m]")
    plt.title(f"{title}: X and Y positions")
    plt.axis("equal")
    plt.grid(True)
    plt.show()

    plt.figure()
    plt.plot(np.arange(traj.shape[0]) * 0.1, traj[:, 0]) #Plotting X vs overall time
    plt.xlabel("Time [s]")
    plt.ylabel("X position [m]")
    plt.title(f"{title}: X over Time")
    plt.grid(True)
    plt.show()

    plt.figure()
    plt.plot(np.arange(traj.shape[0]) * 0.1, traj[:, 1]) #Plotting Y vs overall time
    plt.xlabel("Time [s]")
    plt.ylabel("Y position [m]")
    plt.title(f"{title}: Y over Time")
    plt.grid(True)
    plt.show()
    
    plt.figure()
    plt.plot(np.arange(traj.shape[0]) * 0.1, traj[:, 2]) #Plotting orientation vs overall time
    plt.xlabel("Time [s]")
    plt.ylabel("Orientation [rad]")
    plt.title(f"{title}: Orientation over Time")
    plt.grid(True)
    plt.show()

# Case 1: [v, omega] = [1, 0]
traj1 = simulate_constant_velocity(1, 0, T, dt)
plot_trajectory(traj1, title="1. [v, w] = [1, 0]")

# Case 2: [v, omega] = [0, 0.3]
traj2 = simulate_constant_velocity(0, 0.3, T, dt)
plot_trajectory(traj2, title="2. [v, w] = [0, 0.3]")

# Case 3: [v, omega] = [1, 0.3]
traj3 = simulate_constant_velocity(1, 0.3, T, dt)
plot_trajectory(traj3, title="3. [v, w] = [1, 0.3]")

#Case 4: [v(t), omega(t)] = [1+0.1*sin(t), 0.2+0.5*cos(t)]
traj4 = simulate_variable_velocity()
plot_trajectory(traj4, title="(ii) [Velocity profiles]")
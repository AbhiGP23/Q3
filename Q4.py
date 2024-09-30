import numpy as np
import matplotlib.pyplot as plt

#Parameters and constants
T = 30
dt = 0.1
r=0.1
l=0.25

#Declaring array to hold G
G = np.array([
    [1 + (np.pi / 2), np.pi / 2, l],
    [1 + (7 * np.pi / 6), 7 * np.pi / 6, (-0.5 * l)],
    [1 + (11 * np.pi / 6), 11 * np.pi / 6, l]
])

#Calculate u1,u2,u3 for given case
def calculate_wheel_speed(case):
    if case == 2: # Case 2: St. Line w 60 degree slope 
        r = 0.1
        l = 0.25
        x_dot = 0.2 * np.sqrt(3)
        y_dot = 0.2
        theta_dot = 0

        G = np.array([
            [1 + (np.pi / 2), np.pi / 2, l],
            [1 + (7 * np.pi / 6), 7 * np.pi / 6, (-0.5 * l)],
            [1 + (11 * np.pi / 6), 11 * np.pi / 6, l]
        ])

        speed = np.array([
            [x_dot],
            [y_dot],
            [theta_dot]
        ])

        wheel_speeds = np.dot((1 / r) * G, speed)

        print(wheel_speeds)
    
    elif case == 3:  # Case 3: Circle of diameter 2m
        r = 0.1
        l = 0.25
        x_dot = 0.3
        y_dot = 0
        theta_dot = 0.3

        G = np.array([
            [1 + (np.pi / 2), np.pi / 2, l],
            [1 + (7 * np.pi / 6), 7 * np.pi / 6, (-0.5 * l)],
            [1 + (11 * np.pi / 6), 11 * np.pi / 6, l]
        ])

        speed = np.array([
            [x_dot],
            [y_dot],
            [theta_dot]
        ])

        wheel_speeds = np.dot((1 / r) * G, speed)

        print(wheel_speeds) 
    
    return wheel_speeds.flatten()

#Calculate Velocites with given wheel speeds
def calculate_velocites(u1,u2,u3):
    wheel_speed = np.array([
        [r*u1],
        [r*u2],
        [r*u3]
    ])
    G_inv = np.linalg.inv(G)
    speeds = G_inv@wheel_speed
    x_dot = float(speeds[0])
    y_dot = float(speeds[1])
    theta_dot = float(speeds [2])

    return x_dot, y_dot, theta_dot

#Simulate robot using calculated velocites
def simulate(u1, u2, u3):
    #Initial Variables
    time_steps = int(T / dt)
    traj = np.zeros((time_steps, 3))  # 0 matrix to store x, y and theta at each step
    x, y, theta = 0, 0, 0  # Initial state

    for i in range(time_steps):
        traj[i, :] = [x, y, theta]
        x_dot, y_dot, theta_dot = calculate_velocites(u1,u2,u3)
        x += (x_dot * np.cos(theta) - y_dot * np.sin(theta)) * dt #Updating X in the global frame
        y += (x_dot * np.sin(theta) + y_dot * np.cos(theta)) * dt #Updating Y in the global frame
        theta += theta_dot * dt #Updating theta
        
    return traj


def plot_trajectory(traj, title):
    plt.figure()
    plt.plot(traj[:, 1], traj[:, 0])
    plt.xlabel("Y position [m]")
    plt.ylabel("X position [m]")
    plt.title(f"{title}: X vs Y positions")
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



#Case 1: [u1=-2, u2=1, u3=1]
traj1 = simulate(u1=-2, u2=1, u3=1)
plot_trajectory(traj1, title="(u1=-2, u2=1, u3=1)")

#Case 2: u1, u2, u3 such that robot moves in straight line with 60 degree slope
u1,u2,u3 = calculate_wheel_speed(2)
traj2 = simulate(u1, u2, u3)
plot_trajectory(traj2, title="Straight line with 60 degree slope")

#Case 3: u1, u2, u3 such that robot moves in circle of diameter 2m
u1,u2,u3 = calculate_wheel_speed(3)
traj2 = simulate(u1, u2, u3)
plot_trajectory(traj2, title="Circle of diameter 2m")
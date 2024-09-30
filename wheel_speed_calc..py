import sympy as sym
import numpy as np

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
    
    elif case == 2:  # Case 3: Circle of diameter 2m
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
        

    return 

calculate_wheel_speed(1)

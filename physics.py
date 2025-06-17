# physics.py

import numpy as np

# Gravitational constant in units of AU^3/(kilogram*day**2)
G = 1.48819e-34

def calculate_acceleration(m, rj, ri, G=G):
    """
    Calculate gravitational acceleration between two bodies using numpy.
    
    Args:
        m (float): Mass of the attracting body
        rj (numpy.ndarray): Position vector of the attracting body [x, y, z]
        ri (numpy.ndarray): Position vector of the body being accelerated [x, y, z]
        G (float): Gravitational constant
        
    Returns:
        numpy.ndarray: Acceleration vector [ax, ay, az]
    """
    # Calculate difference vector and distance
    diff_vec = rj - ri
    distance = np.linalg.norm(diff_vec)
    
    if distance == 0:
        raise ValueError("Planets cannot be in the same position")
    
    # Calculate acceleration vector using vectorized operations
    return G * m * diff_vec / (distance**3)

def calculate_gravitational_forces(q, t, m, G=G):
    """
    Calculate gravitational forces for all bodies in the system.
    
    Args:
        q (numpy.ndarray): State vector [all_positions, all_velocities]
        t (float): Time (not used but required by solver)
        m (list): List of masses for all bodies
        G (float): Gravitational constant
        
    Returns:
        numpy.ndarray: Array of derivatives [all_velocities, all_accelerations]
    """
    N = len(m)
    
    # Correctly unpack positions and velocities from the state vector 'q'
    # Positions are the first half, velocities are the second half.
    positions = q[:3*N].reshape((N, 3))
    velocities = q[3*N:].reshape((N, 3))
    
    # Initialize accelerations array with zeros
    accelerations = np.zeros_like(positions)
    
    # Calculate accelerations for each body
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            # Accumulate acceleration on body 'i' due to body 'j'
            accel = calculate_acceleration(m[j], positions[j], positions[i], G)
            accelerations[i] += accel

    # The derivative of position is velocity.
    # The derivative of velocity is acceleration.
    # Return the derivatives in the same flat structure as 'q'.
    qprime = np.concatenate([velocities.flatten(), accelerations.flatten()])
    
    return qprime
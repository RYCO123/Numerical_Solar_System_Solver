# visualization.py

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from mpl_toolkits.mplot3d import Axes3D

def plot_orbits(q, t, body_names, title="Solar System Orbits"):
    """
    Plot the orbits of all bodies in 3D with animation.
    
    Args:
        q (numpy.ndarray): Solution array from the solver
        t (numpy.ndarray): Time points
        body_names (list): List of body names
        title (str): Plot title
    """
    fig = plt.figure(figsize=(12, 8))
    ax = fig.add_subplot(111, projection='3d')
    
    # Set up the plot
    ax.set_xlabel('X (AU)')
    ax.set_ylabel('Y (AU)')
    ax.set_zlabel('Z (AU)')
    ax.set_title(title)
    
    # Set equal aspect ratio
    max_range = np.array([q[:, :3*len(body_names)].max(), 
                         q[:, :3*len(body_names)].min()]).max()
    ax.set_xlim(-max_range, max_range)
    ax.set_ylim(-max_range, max_range)
    ax.set_zlim(-max_range, max_range)
    
    # Create lines and scatter plots for each body
    lines = []
    scatters = []
    for i in range(len(body_names)):
        # Plot the orbit line
        x = q[:, 3*i]
        y = q[:, 3*i + 1]
        z = q[:, 3*i + 2]
        line, = ax.plot(x, y, z, label=body_names[i], alpha=0.5)
        lines.append(line)
        
        # Create scatter point for current position
        scatter = ax.scatter([], [], [], label=body_names[i])
        scatters.append(scatter)
    
    # Add legend
    ax.legend()
    
    def update(frame):
        for i, scatter in enumerate(scatters):
            pos = q[frame, 3*i:3*(i+1)]
            scatter._offsets3d = ([pos[0]], [pos[1]], [pos[2]])
        return scatters
    
    # Create animation
    anim = FuncAnimation(fig, update, frames=len(t), interval=50, blit=True)
    plt.show()

def plot_2d_orbits(q, t, body_names, plane='xy', title=None):
    """
    Plot the orbits in 2D on the specified plane.
    
    Args:
        q (numpy.ndarray): Solution array from the solver
        t (numpy.ndarray): Time points
        body_names (list): List of body names
        plane (str): Plane to plot ('xy', 'xz', or 'yz')
        title (str): Plot title
    """
    fig, ax = plt.subplots(figsize=(10, 10))
    
    # Determine which indices to use based on the plane
    if plane == 'xy':
        idx1, idx2 = 0, 1
        xlabel, ylabel = 'X (AU)', 'Y (AU)'
    elif plane == 'xz':
        idx1, idx2 = 0, 2
        xlabel, ylabel = 'X (AU)', 'Z (AU)'
    elif plane == 'yz':
        idx1, idx2 = 1, 2
        xlabel, ylabel = 'Y (AU)', 'Z (AU)'
    else:
        raise ValueError("Plane must be 'xy', 'xz', or 'yz'")
    
    # Set up the plot
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    if title is None:
        title = f'Solar System Orbits ({plane.upper()} plane)'
    ax.set_title(title)
    
    # Set equal aspect ratio
    max_range = np.array([q[:, :3*len(body_names)].max(), 
                         q[:, :3*len(body_names)].min()]).max()
    ax.set_xlim(-max_range, max_range)
    ax.set_ylim(-max_range, max_range)
    
    # Create lines and scatter plots for each body
    lines = []
    scatters = []
    for i in range(len(body_names)):
        # Plot the orbit line
        x = q[:, 3*i + idx1]
        y = q[:, 3*i + idx2]
        line, = ax.plot(x, y, label=body_names[i], alpha=0.5)
        lines.append(line)
        
        # Create scatter point for current position
        scatter = ax.scatter([], [], label=body_names[i])
        scatters.append(scatter)
    
    # Add legend
    ax.legend()
    
    def update(frame):
        for i, scatter in enumerate(scatters):
            pos = q[frame, 3*i:3*(i+1)]
            scatter.set_offsets([[pos[idx1], pos[idx2]]])
        return scatters
    
    # Create animation
    anim = FuncAnimation(fig, update, frames=len(t), interval=50, blit=True)
    plt.show()
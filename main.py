import numpy as np
from data import initial_conditions, masses, body_names
from physics import calculate_gravitational_forces
from solver import solve_rk4
from visualization import plot_orbits, plot_2d_orbits

def main():
    # Define the time points for the simulation
    t = np.linspace(0, 60191, 60192)  # 100 days with 1-day steps
    
    # Define the function that computes derivatives
    def f(q, t):
        return calculate_gravitational_forces(q, t, masses)
    
    # Solve the system
    print("Solving the solar system...")
    solution = solve_rk4(f, t, initial_conditions)
    
    # Plot the results
    print("Plotting 3D orbits...")
    plot_orbits(solution, t, body_names)
    
    print("Plotting 2D orbits...")
    plot_2d_orbits(solution, t, body_names, plane='xy')
    plot_2d_orbits(solution, t, body_names, plane='xz')
    plot_2d_orbits(solution, t, body_names, plane='yz')

if __name__ == "__main__":
    main() 
# Solar System Orbit Simulation

![Simulation GIF](<path_to_your_gif_or_screenshot.gif>)
*Suggestion: Record a short GIF of your simulation and add it here. It's the single most effective way to grab attention. You can use tools like LICEcap or ScreenToGif.*

## About The Project

This project presents a high-fidelity N-body simulation that models the gravitational interactions of celestial bodies in our solar system. It leverages a custom-built 4th-order Runge-Kutta (RK4) numerical solver and real-world ephemeris data from NASA/JPL Horizons to accurately predict the orbital paths of the Sun, the 8 planets, and Earth's Moon.

Originally conceived for a computational physics course, this project has been developed into a robust portfolio piece demonstrating skills in algorithm implementation, physics modeling, and data visualization.

### Key Technical Features

*   **Custom RK4 Implementation:** A robust 4th-order Runge-Kutta solver written from scratch in `solver.py` to numerically integrate the differential equations of motion with high precision.
*   **N-Body Physics Engine:** The core physics engine in `physics.py` calculates the net gravitational force on each celestial body from all other bodies at every timestep, modeling a classic N-body problem.
*   **Empirical Data Integration:** Utilizes planetary initial state vectors (position and velocity) sourced from **NASA's JPL Horizons system**, ensuring the simulation begins from a physically accurate state.
*   **Dynamic 3D Visualization:** Renders the orbital paths of all celestial bodies in an interactive 3D plot using **Matplotlib**, providing a clear and intuitive representation of the simulation results.
*   **Modular & Organized Codebase:** The project is structured into distinct, decoupled modules for physics, solving, data handling, and visualization, promoting code reusability and maintainability.

## Getting Started

### Prerequisites

Ensure you have Python 3 installed. This project uses standard libraries listed in `requirements.txt`.

### Installation

1.  Clone the repository:
    ```sh
    git clone https://github.com/your-username/your-repo-name.git
    ```
2.  Navigate to the project directory:
    ```sh
    cd your-repo-name
    ```
3.  Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

### Usage

To run the simulation and generate the visualization, execute the main script:
```sh
python main.py

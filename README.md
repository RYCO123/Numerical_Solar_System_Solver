# Solar System Simulation

This project simulates the motion of planets in our solar system using Newton's laws of gravitation. The simulation includes the Sun and the 8 inner planets plus Earth's moon.

## Features

- Simulates planetary motion using Newton's laws of gravitation
- Includes the Sun, 8 inner planets, and Earth's moon
- Uses 4th order Runge-Kutta method for numerical integration
- Visualizes planetary orbits in 3D space

## Installation

1. Clone this repository
2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Usage

Run the main simulation:
```bash
python main.py
```

## Project Structure

- `main.py`: Main entry point for the simulation
- `solver.py`: Contains the numerical integration methods
- `physics.py`: Contains physics-related functions and constants
- `visualization.py`: Contains plotting and visualization functions
- `data.py`: Contains initial conditions and planetary data

## Data Source

The initial conditions for planetary positions and velocities were obtained from NASA/JPL's HORIZONS web interface (https://ssd.jpl.nasa.gov/horizons/app.html#/). 
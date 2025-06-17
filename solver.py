import numpy as np

def solve_rk4(f, t, q0):
    """
    Solve differential equations using 4th order Runge-Kutta method.
    
    Args:
        f (callable): Function that computes derivatives
        t (numpy.ndarray): Array of time points
        q0 (numpy.ndarray): Initial conditions
        
    Returns:
        numpy.ndarray: Solution array
    """
    # Initialize output array
    q = np.zeros((len(t), len(q0)))
    q[0] = q0
    
    # Main integration loop
    for i in range(len(t)-1):
        h = t[i+1] - t[i]
        
        # Calculate Runge-Kutta coefficients
        k1 = f(q[i], t[i])
        k2 = f(q[i] + h/2 * k1, t[i] + h/2)
        k3 = f(q[i] + h/2 * k2, t[i] + h/2)
        k4 = f(q[i] + h * k3, t[i] + h)
        
        # Update solution
        q[i+1] = q[i] + h/6 * (k1 + 2*k2 + 2*k3 + k4)
    
    return q 
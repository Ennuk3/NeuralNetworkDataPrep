import numpy as np

def tanh_func(x, n, x_0, m, c):
    """
    This function defines tanh in order to use it to fit Charpy curves.
    
    Parameters
    ----------
    x : float
        independent variable
    n : float
    x_0 : float
    m : float
    c : float
    
    Returns
    -------
    y : float
        dependent variable
    """
    y = m*np.tanh((x-x_0)/n)+c
    return y

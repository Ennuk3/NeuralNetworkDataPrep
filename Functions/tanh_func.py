def tanh_func(x, n, x_0, m, c):
    y = m*np.tanh((x-x_0)/n)+c
    return y

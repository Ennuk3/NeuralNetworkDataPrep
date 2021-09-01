import numpy as np

def check_surr(array, index):
    """
    This function finds the first instance of a minimal gradient within the upper end of a Charpy curve.
    This is acheived by calculating the difference between the chosen point (index) and the average of the 1000 points before and after the chosen point.
    If the point is not within a range of 1 between both points, then the next point is selected by increasing the index by 1.
    
    Parameters
    ----------
    array : tuple
        input Charpy data, based on which the initial curve is plotted
    index : int
        the index value at which the gradient minimizing function is chosen to begin based on parameters in previous code 
        (must be further than the transition point, otherwise the function does not work properly)
        
    Returns
    -------
    index : int
        returns the index at which the gradient of the function is deemed to first reach a defined minimum
    
    """
    
    #The Charpy curves fitted in this case all have 10000 points.
    while index <= 10000: 
        #Define the range at which the averages are taken. If there are not enough values on the upper end of the boundary, then all the remaining values are averaged.
        avg_before = np.average(array[(index-1000):index])
        avg_after = np.average(array[index:(index+(10000-index))])
        
        #Set a limit of a total of 1 between the upper and lower end of the boundary (arbitrary)
        if array[index]-avg_before > 0.5:
            index += 1
        if avg_after-array[index] > 0.5:
            index += 1
        else:
            return index
            break

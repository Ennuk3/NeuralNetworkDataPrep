import numpy as np

def gradient(array, index):
    """
    This function checks whether the calculated upper shelf start point is too close to the upper end of the temperature scale.
    If the gradient between the calculated index and the end point of the Charpy curve is greater than or equal to 0.025, then the upper shelf point is not valid.
    
    Parameters
    ----------
    array : tuple
        input Charpy data, based on which the initial curve is plotted
    index : int
        the calculated upper shelf start point
        
    Returns
    -------
    None : NoneType
        if the upper shelf start point does not meet the specified requirements, nothing is returned
    index : int
        the same index value as the input index value
    """
    
    #Calculates the gradient between the index and the end of the Charpy curve.
    avg_after = np.average(np.gradient(array[index:(index+(10000-index))]))
   
    if avg_after >= 25/10000:
        return None
    else:
        return index

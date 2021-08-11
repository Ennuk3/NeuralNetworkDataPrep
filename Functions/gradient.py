def gradient(array, index):
    
    avg_after = np.average(np.gradient(array[index:(index+(10000-index))]))
   
    if avg_after >= 25/10000:
        return None
    else:
        return index

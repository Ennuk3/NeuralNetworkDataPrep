def check_surr(array, index):
    while index <= 10000:
        avg_before = np.average(array[(index-1000):index])
        avg_after = np.average(array[index:(index+(10000-index))])
        
        if array[index]-avg_before > 0.5:
            index += 1
        if avg_after-array[index] > 0.5:
            index += 1
        else:
            return index
            break

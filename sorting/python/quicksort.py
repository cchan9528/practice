def _quicksort(arr, start, stop, verbose = False):
    '''
    Quick Sort
        - Build a sorted array by positioning partition elements and repeating
            for subarrays adjacent to partition elemenets where all elements
            less than the partition element are in the left subarray and all
            elements greater than the partition element are in the right
            subarray; equal elements can go anywhere
        - O(log(n)) space; O(nlogn) avg, O(nlogn) best, O(n^2) worst runtime
    '''
    if start < stop:
        ###############################
        # Position partition
        ###############################
        partition = _partition(arr, start, stop, verbose = verbose)
        
        ###############################
        # Sort subarrays
        ###############################
        _quicksort(arr, 0, partition-1, verbose = verbose)
        _quicksort(arr, partition+1, stop, verbose = verbose)

def _partition(arr, start, stop, verbose = False):
    ###############################
    # Select a partition
    ###############################
    p = start

    ###############################
    # Position elements
    ###############################
    i = start+1
    j = stop
    while True:
        while i<=stop and arr[i]<=arr[p]:   # Look for element > partition
            i += 1
        while j>=start+1 and arr[j]>=arr[p]:  # Look for element < partition
            j -= 1
        if i>=j:                            # If they touch or crossed, stop
            break
        arr[i], arr[j] = arr[j], arr[i]     # Swap out-of-place elements
        i += 1
        j -= 1
    ###############################
    # Position partition
    ###############################
    arr[p], arr[j] = arr[j], arr[p]         # by now, arr[p]>=arr[j], so swap

    if verbose:
        print('\t\t\tPass (after %s partition): %s' % (str(arr[j]),str(arr)))
    return j

def main(arr, verbose = False):
    _quicksort(arr, 0, len(arr)-1, verbose = verbose)
    return arr
main.__doc__ = _quicksort.__doc__

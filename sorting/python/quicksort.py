def _quicksort(arr, first, last, verbose = False):
    '''
    Quick Sort
        - Build a sorted array by positioning partition elements and repeating
            for subarrays adjacent to partition elemenets where all elements
            less than the partition element are in the left subarray and all
            elements greater than the partition element are in the right
            subarray; equal elements can go anywhere
        - O(log(n)) space; O(nlogn) avg, O(nlogn) best, O(n^2) worst runtime
    '''
    if first < last:
        ###############################
        # Position partition
        ###############################
        partition = _partition(arr, first, last, verbose = verbose)

        ###############################
        # Sort subarrays
        ###############################
        _quicksort(arr, 0, partition-1, verbose = verbose)
        _quicksort(arr, partition+1, last, verbose = verbose)

def _partition(arr, first, last, verbose = False):
    ###############################
    # Select a partition
    ###############################
    p = first

    ###############################
    # Position elements
    ###############################
    i = first+1
    j = last
    while True:
        while i<=last and arr[i]<=arr[p]:   # Look for element > partition
            i += 1
        while j>=first+1 and arr[j]>=arr[p]:  # Look for element < partition
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

def main(x, verbose = False):
    arr = [_ for _ in x]
    _quicksort(arr, 0, len(arr)-1, verbose = verbose)
    return arr
main.__doc__ = _quicksort.__doc__

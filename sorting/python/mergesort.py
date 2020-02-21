def _mergesort(arr, verbose = False):
    '''
    Merge Sort
        - Build a sorted array with sorted subarrays where the subarrays are
            created by merging two subarrays
        - O(n) space; O(nlogn) avg/best/worst runtime
    '''
    n     = len(arr)
    if n <= 1:
        return arr

    ###############################
    # Sort subarrays
    ###############################
    left  = _mergesort(arr[:n//2], verbose = verbose)
    right = _mergesort(arr[n//2:], verbose = verbose)
    return _merge(left, right, verbose = verbose)

def _merge(left, right, verbose = False):
    merged = []
    i = 0
    j = 0

    ###############################
    # Merge two lists (subarrays)
    ###############################
    while i<len(left) and j<len(right):
        if left[i]<=right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    ###############################
    # Push leftovers into list
    ###############################
    while i<len(left):
        merged.append(left[i])
        i += 1

    while j<len(right):
        merged.append(right[j])
        j+=1
    if verbose:
        print('\t\t\tPass (after merge): %s' % str(merged))
    return merged

def main(arr, verbose = False):
    return _mergesort(arr, verbose = verbose)
main.__doc__ = _mergesort.__doc__

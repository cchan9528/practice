def main(arr, min = -10, max = 10, verbose = False):
    '''
    Counting Sort
        - Build a sorted array by counting the frequency of element a[i],
            accumulating the frequencies in a running sum and using that
            running sum to place arr[i] in a output array going from i=[n-1, 0]
        - O(k+n) space; O(k+n) time
            - The temp array has length k, which may be different than n, the
                original length of the array => O(k+n) space/time

        - This is an integer sort, not a comparison one; it sorts by the
            characteristics of an element, no by comparing one element with
            another

    '''
    ###############################
    # Build the frequency array
    ###############################
    n     = len(arr)
    start = abs(min) if min<0 else -(abs(min))   # if min!=0, offset cf index
    cf    = [0 for i in range(min, max+1)]       # +1 for 0 in middle of range
    res   = [0 for i in range(n)]

    ###############################
    # Collect frequencies
    ###############################
    for i in range(n):
        cf[arr[i]+start] += 1
    if verbose:
        print('\t\t\tPass (frequencies): %s' % str(cf))

    ###############################
    # Accumulate frequencies
    ###############################
    for j in range(1, len(cf)):
        cf[j] = cf[j] + cf[j-1]
    if verbose:
        print('\t\t\tPass (frequencies): %s' % str(cf))

    ###############################
    # Build sorted array
    ###############################
    for k in range(n-1, -1, -1):
        res[cf[arr[k]+start]-1] = arr[k]      # -1 since cf == length of series
        cf[arr[k]+start] -= 1
    if verbose:
        print('\t\t\tPass (frequencies): %s' % str(cf))

    return res

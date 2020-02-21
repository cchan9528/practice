def main(arr, verbose = False):
    '''
    Selection Sort
        - Build sorted array from left side by selecting the minimum element at
            each iteration and swapping it
        - O(1) space, O(n^2) avg/worst/best runtime
    '''
    n = len(arr)
    for i in range(n):
        ###############################
        # Select min
        ###############################
        imin = i
        for j in range(i, n):
            if arr[j] < arr[imin]:
                imin = j

        ###############################
        # Swap
        ###############################
        arr[i], arr[imin] = arr[imin], arr[i]

        if verbose:
            print('\t\t\tPass: %s' % str(arr))

    return arr

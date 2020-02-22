def radix(arr, base = 10, verbose = False):
    '''
    Radix Sort
        - Build a sorted array by sorting digits from least significant digit
            to most significant digit using counting sort for each digit,
            repeatedly shuffling around the original elements until sorted
        - O(d(n+b)) space and time; b = base, d = # of digits of longest element
            - O(n+b) for each iteration; d iterations of counting sort

        - This is an integer sort, not a comparison one; it sorts by the
            characteristics of an element, no by comparing one element with
            another
    '''

    n = len(arr)
    if n <= 1:
        return arr

    ###############################
    # Find longest element
    ###############################
    longest = arr[0]
    for i in range(n):
        if longest < arr[i]:
            longest = arr[i]

    ###############################
    # Find len of longest element
    ###############################
    d = 0
    while longest:
        d += 1
        longest //= base

    ###############################
    # Counting sort on digits
    ###############################
    for j in range(d):
        arr = _countingSort(arr, base, j)
        if verbose:
            print('\t\t\tPass (after digit %s): %s' % (str(j), str(arr)))

    return arr

def _countingSort(arr, base, d_i):
    n = len(arr)
    if n <= 1:
        return arr
    res = [0 for i in range(n)]
    cf  = [0 for i in range(base)]

    ###############################
    # Collect Frequencies
    ###############################
    for i in range(n):
        digit = ( arr[i] // (base**d_i) ) % base
        cf[digit] += 1

    ###############################
    # Create running frequencies
    ###############################
    for j in range(1, base):
        cf[j] += cf[j-1]

    ###############################
    # Position elements in res
    ###############################
    for k in range(n-1, -1, -1):
        digit = ( arr[k] // (base**d_i) ) % base
        res[cf[digit]-1] = arr[k]
        cf[digit] -= 1

    return res

def main(arr, base = 10, verbose = False):
    return radix(arr, base, verbose = verbose)
main.__doc__ = radix.__doc__

def main(x, verbose = False):
    '''
    Shell Sort
        - Build a sorted array by repeatedly running insertion sort on elements
            spaced k-elements apart where k gradually decreases to 1 to
            guarantee a sorted array at the end
            - Hibbard's increments: s=(2^k)-1 spacing;
                must find k so a*s<=n for some integer a to find s_max
        - O(1) space; O(nlogn) best, O(n^2) worst, O(n^1.25) average
    '''
    arr = [_ for _ in x]
    n   = len(arr)
    if n <= 1:
        return arr

    ###############################
    # Find spacings
    ###############################
    spaces = []
    k = 1
    while True:
        spacing = (2**k)-1
        if spacing+1 >= n:           # +1 for the element start spacing from
            break
        spaces.append( spacing )
        k += 1

    ###############################
    # Repeatedly insertion sort
    ###############################
    for space in spaces:
        for g in range(0, n):                          # 'g': group index
            for i in range(g, n, space):
                ###############################
                # Shift
                ###############################
                temp = arr[i]
                j = i-space                             # j is behind i
                while j >= 0 and arr[j] > temp:
                    arr[j+space] = arr[j]               # shift
                    j -= space
                arr[j+space] = temp
            if verbose:
                print('\t\t\tPass (group %s with spacing %s): %s '
                        % (str(g), str(space), str(arr)))
    return arr

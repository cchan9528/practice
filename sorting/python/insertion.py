def main(arr, verbose = False):
    '''
    Insertion Sort
        - Build sorted array from left by inserting the next unsorted element
            and inserting it into the sorted portion of the array
        - O(1) space; O(n^2) avg/worst, O(n) best runtime
    '''

    n = len(arr)
    for i in range(1, n):
        temp = arr[i] # The next unsorted element
        j = i-1
        while j>=0 and arr[j]>temp:
            ###############################
            # Shift
            ###############################
            arr[j+1] = arr[j]
            j -= 1

        ###############################
        # Insert
        ###############################
        arr[j+1] = temp
        if verbose:
            print('\t\t\tPass: %s' % str(arr))

    return arr

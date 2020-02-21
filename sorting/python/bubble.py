def main(arr, verbose = False):
    '''
    Bubble Sort
        - Build a sorted array from the right side by bubbling up the biggest
            element to the right; done by looking at the next element
            - Optimization: stop early if no bubbling
        - O(1) space, O(n^2) runtime
    '''
    n = len(arr)
    for i in range(n):
        bubbled = False
        for j in range(n-i-1): # -1 for the j+1 lookahead
            ###############################
            # Bubble
            ###############################
            if arr[j] > arr[j+1]:
                arr[j+1], arr[j] = arr[j], arr[j+1]
                bubbled = True
        if not bubbled:
            break
    return arr

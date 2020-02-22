def _heapsort(arr, verbose = False):
    '''
    Heap Sort
        - Build a sorted array from the right by using a max-heap to
            pop the root, pushing the root to the back, reheapifying
            the leftover heap, and repeating until the size of the heap is 1
        - O(1) space; O(nlogn) runtime
    '''
    n = len(arr)

    ###############################
    # Heapify the original
    ###############################
    for root in range((n-1)//2, -1, -1): # (n-1)//2 = parent of node n (0-index)
        _heapifySubtree(arr, root, n-1)       # Subtree is part of heap
    if verbose:
        print('\t\t\tPass (initial heap): %s' % str(arr))

    ###############################
    # Pop, reheapify, repeat
    ###############################
    i = 0
    while i < n:
        arr[0], arr[n-1-i] = arr[n-1-i], arr[0]    # Swap leaf with root
        i += 1
        _heapifySubtree(arr, 0, n-1-i)             # Subtree is the whole heap
        if verbose:
            print('\t\t\tPass (after pop and heapify): %s' % str(arr))

def _heapifySubtree(arr, root, last):
    if root == last:
        return

    ###############################
    # Update so Root > Children
    ###############################
    left    = int(2*root) + 1
    right   = int(2*root) + 2
    biggest = root
    if left <= last and arr[left] > arr[biggest]:
        biggest = left
    if right <= last and arr[right] > arr[biggest]:
        biggest = right
    arr[root], arr[biggest] = arr[biggest], arr[root]

    ###############################
    # Must update subtrees now
    ###############################
    if biggest == left:
        _heapifySubtree(arr, left, last)
    elif biggest == right:
        _heapifySubtree(arr, right, last)

def main(arr, verbose = False):
    _heapsort(arr, verbose=verbose)
    return arr

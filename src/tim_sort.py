def insertion_sort(arr, left=0, right=None):
    """
    Perform insertion sort on a subarray.
    
    :param arr: List to be sorted
    :param left: Starting index of the subarray
    :param right: Ending index of the subarray (inclusive)
    """
    if right is None:
        right = len(arr) - 1
    
    for i in range(left + 1, right + 1):
        key = arr[i]
        j = i - 1
        
        while j >= left and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        
        arr[j + 1] = key
    
    return arr

def merge(arr, left, mid, right):
    """
    Merge two sorted subarrays of arr.
    
    :param arr: List containing the subarrays to merge
    :param left: Starting index of the first subarray
    :param mid: Ending index of the first subarray
    :param right: Ending index of the second subarray
    """
    # Create temporary arrays
    left_arr = arr[left:mid + 1]
    right_arr = arr[mid + 1:right + 1]
    
    # Initial indexes of first and second subarrays
    i, j, k = 0, 0, left
    
    # Merge the temp arrays back into arr
    while i < len(left_arr) and j < len(right_arr):
        if left_arr[i] <= right_arr[j]:
            arr[k] = left_arr[i]
            i += 1
        else:
            arr[k] = right_arr[j]
            j += 1
        k += 1
    
    # Copy remaining elements of left_arr if any
    while i < len(left_arr):
        arr[k] = left_arr[i]
        i += 1
        k += 1
    
    # Copy remaining elements of right_arr if any
    while j < len(right_arr):
        arr[k] = right_arr[j]
        j += 1
        k += 1
    
    return arr

def tim_sort(arr):
    """
    Tim Sort implementation.
    
    :param arr: List to be sorted
    :return: Sorted list
    """
    # Minimum size of a run (subarray sorted by insertion sort)
    MIN_RUN = 32
    
    # Sort individual subarrays of size MIN_RUN
    n = len(arr)
    for i in range(0, n, MIN_RUN):
        insertion_sort(arr, i, min(i + MIN_RUN - 1, n - 1))
    
    # Start merging runs from size MIN_RUN
    size = MIN_RUN
    while size < n:
        # Pick starting point of different runs
        for start in range(0, n, size * 2):
            # Find ending point of first run
            mid = start + size - 1
            end = min(start + size * 2 - 1, n - 1)
            
            # Merge runs
            if mid < end:
                merge(arr, start, mid, end)
        
        # Double the size of runs
        size *= 2
    
    return arr
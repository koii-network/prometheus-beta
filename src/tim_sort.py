def insertion_sort(arr, left, right):
    """
    Perform insertion sort on a subarray.
    
    :param arr: List to be sorted
    :param left: Starting index of the subarray
    :param right: Ending index of the subarray
    """
    for i in range(left + 1, right + 1):
        key = arr[i]
        j = i - 1
        while j >= left and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def merge(arr, left, mid, right):
    """
    Merge two sorted subarrays.
    
    :param arr: List to be merged
    :param left: Starting index of the first subarray
    :param mid: Ending index of the first subarray
    :param right: Ending index of the second subarray
    """
    # Calculate lengths of two subarrays to be merged
    len1 = mid - left + 1
    len2 = right - mid
    
    # Create temporary arrays
    left_arr = arr[left:left + len1]
    right_arr = arr[mid + 1:mid + 1 + len2]
    
    # Initial indexes of first and second subarrays
    i, j, k = 0, 0, left
    
    # Merge the temporary arrays back into arr
    while i < len1 and j < len2:
        if left_arr[i] <= right_arr[j]:
            arr[k] = left_arr[i]
            i += 1
        else:
            arr[k] = right_arr[j]
            j += 1
        k += 1
    
    # Copy remaining elements of left_arr, if any
    while i < len1:
        arr[k] = left_arr[i]
        i += 1
        k += 1
    
    # Copy remaining elements of right_arr, if any
    while j < len2:
        arr[k] = right_arr[j]
        j += 1
        k += 1

def tim_sort(arr):
    """
    Implement Tim Sort algorithm.
    
    :param arr: List to be sorted
    :return: Sorted list
    """
    # Minimum size of a run (subarray sorted using insertion sort)
    MIN_RUN = 32
    
    # Length of the input array
    n = len(arr)
    
    # Sort individual subarrays of size RUN
    for i in range(0, n, MIN_RUN):
        insertion_sort(arr, i, min(i + MIN_RUN - 1, n - 1))
    
    # Start merging from size RUN (or 32)
    size = MIN_RUN
    while size < n:
        # Pick starting point of different subarrays of size 'size'
        for start in range(0, n, size * 2):
            # Find ending point of left subarray
            mid = start + size - 1
            # Find ending point of right subarray
            end = min(start + size * 2 - 1, n - 1)
            
            # Merge subarrays arr[start...mid] and arr[mid+1...end]
            if mid < end:
                merge(arr, start, mid, end)
        
        # Double the size of subarrays to be merged
        size *= 2
    
    return arr
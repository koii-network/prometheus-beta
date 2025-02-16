def insertion_sort(arr, left, right):
    """
    Insertion sort for small subarrays in Tim Sort.
    
    Args:
        arr (list): The list to be sorted
        left (int): Starting index of the subarray
        right (int): Ending index of the subarray
    """
    for i in range(left + 1, right + 1):
        key = arr[i]
        j = i - 1
        
        # Move elements that are greater than key to one position ahead
        while j >= left and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        
        arr[j + 1] = key

def merge(arr, left, mid, right):
    """
    Merge two sorted subarrays of arr.
    
    Args:
        arr (list): The list containing subarrays to be merged
        left (int): Starting index of the first subarray
        mid (int): Ending index of the first subarray
        right (int): Ending index of the second subarray
    """
    # Compute lengths of two subarrays to be merged
    len1 = mid - left + 1
    len2 = right - mid
    
    # Create temporary arrays
    left_arr = arr[left:left + len1]
    right_arr = arr[mid + 1:mid + 1 + len2]
    
    # Initial indexes of first and second subarrays
    i, j, k = 0, 0, left
    
    # Merge the temporary arrays
    while i < len1 and j < len2:
        if left_arr[i] <= right_arr[j]:
            arr[k] = left_arr[i]
            i += 1
        else:
            arr[k] = right_arr[j]
            j += 1
        k += 1
    
    # Copy remaining elements of left_arr if any
    while i < len1:
        arr[k] = left_arr[i]
        k += 1
        i += 1
    
    # Copy remaining elements of right_arr if any
    while j < len2:
        arr[k] = right_arr[j]
        k += 1
        j += 1

def tim_sort(arr):
    """
    Tim Sort implementation: A hybrid sorting algorithm derived from 
    merge sort and insertion sort.
    
    Args:
        arr (list): The list to be sorted
    
    Returns:
        list: Sorted list
    """
    # Minimum size of a run (subarray sorted using insertion sort)
    MIN_RUN = 32
    
    # Determine the length of the input array
    n = len(arr)
    
    # Sort individual subarrays of size RUN
    for i in range(0, n, MIN_RUN):
        insertion_sort(arr, i, min(i + MIN_RUN - 1, n - 1))
    
    # Start merging from size RUN (or 32)
    size = MIN_RUN
    while size < n:
        # Pick starting point of different subarrays of size 'size'
        for start in range(0, n, size * 2):
            # Find ending point of first subarray
            mid = start + size - 1
            
            # Find ending point of second subarray
            end = min(start + size * 2 - 1, n - 1)
            
            # Merge subarrays if mid is less than end
            if mid < end:
                merge(arr, start, mid, end)
        
        # Double the size of subarrays to be merged
        size *= 2
    
    return arr
def tim_sort(arr):
    """
    Implement Tim Sort algorithm for sorting a list.
    
    Tim Sort is a hybrid sorting algorithm derived from merge sort and insertion sort,
    designed to perform well on many kinds of real-world data.
    
    Args:
        arr (list): The input list to be sorted
    
    Returns:
        list: A new sorted list
    """
    # If the list is small, use insertion sort
    def insertion_sort(arr, left, right):
        for i in range(left + 1, right + 1):
            key = arr[i]
            j = i - 1
            while j >= left and arr[j] > key:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key
        return arr

    # Merge two sorted subarrays
    def merge(arr, left, mid, right):
        # Create temporary arrays
        left_arr = arr[left:mid + 1]
        right_arr = arr[mid + 1:right + 1]
        
        # Initial indexes of left, right subarrays and merged array
        i = j = 0
        k = left
        
        # Merge the temp arrays back into the original array
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
            k += 1
            i += 1
        
        # Copy remaining elements of right_arr if any
        while j < len(right_arr):
            arr[k] = right_arr[j]
            k += 1
            j += 1
        
        return arr

    # Minimum size of a run (subarray)
    MIN_RUN = 32
    
    # Create a copy of the input list to avoid modifying the original
    arr = arr.copy()
    n = len(arr)
    
    # Sort individual subarrays of size MIN_RUN
    for i in range(0, n, MIN_RUN):
        insertion_sort(arr, i, min(i + MIN_RUN - 1, n - 1))
    
    # Start merging subarrays
    size = MIN_RUN
    while size < n:
        for start in range(0, n, size * 2):
            mid = start + size - 1
            end = min(start + size * 2 - 1, n - 1)
            
            # Merge subarrays
            if mid < end:
                merge(arr, start, mid, end)
        
        # Double the size of subarrays
        size *= 2
    
    return arr
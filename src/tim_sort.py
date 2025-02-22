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
    # If the list is already sorted or empty, return a copy
    if len(arr) <= 1:
        return arr.copy()
    
    # Minimum run length for Tim Sort
    MIN_MERGE = 32
    
    def insertion_sort(arr, left, right):
        """
        Perform insertion sort on a small portion of the array.
        
        Args:
            arr (list): The input list
            left (int): Starting index
            right (int): Ending index
        """
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
        Merge two sorted subarrays.
        
        Args:
            arr (list): The input list
            left (int): Starting index of first subarray
            mid (int): Ending index of first subarray
            right (int): Ending index of second subarray
        """
        # Create temp arrays
        left_arr = arr[left:mid + 1]
        right_arr = arr[mid + 1:right + 1]
        
        # Initial indexes of first and second subarrays
        i, j, k = 0, 0, left
        
        # Merge elements from two arrays
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
    
    # Create a copy of the input array to avoid modifying the original
    arr = arr.copy()
    
    # Sort small chunks with insertion sort
    for start in range(0, len(arr), MIN_MERGE):
        end = min(start + MIN_MERGE - 1, len(arr) - 1)
        insertion_sort(arr, start, end)
    
    # Merge sorted chunks
    size = MIN_MERGE
    while size < len(arr):
        for start in range(0, len(arr), size * 2):
            mid = start + size - 1
            end = min(start + size * 2 - 1, len(arr) - 1)
            
            # Merge two chunks if mid is less than end
            if mid < end:
                merge(arr, start, mid, end)
        
        size *= 2
    
    return arr
def tim_sort(arr):
    """
    Implement the Tim Sort algorithm for sorting a list.
    
    Tim Sort is a hybrid sorting algorithm that combines merge sort and insertion sort.
    It's the standard sorting algorithm used in Python's built-in sorted() and list.sort().
    
    Args:
        arr (list): The input list to be sorted
    
    Returns:
        list: A new sorted list
    
    Raises:
        TypeError: If the input is not a list or contains non-comparable elements
    """
    # Validate input
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Create a copy to avoid modifying the original list
    arr = arr.copy()
    
    # Minimum length of a run
    MIN_MERGE = 32
    
    def insertion_sort(arr, left, right):
        """
        Perform insertion sort on a portion of the list
        
        Args:
            arr (list): The list to be sorted
            left (int): Starting index of the portion
            right (int): Ending index of the portion
        """
        for i in range(left + 1, right + 1):
            key = arr[i]
            j = i - 1
            while j >= left and arr[j] > key:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key
        return arr
    
    def merge(arr, l, m, r):
        """
        Merge two sorted subarrays of arr[]
        
        Args:
            arr (list): The list containing subarrays to merge
            l (int): Starting index of first subarray
            m (int): Ending index of first subarray
            r (int): Ending index of second subarray
        """
        # Sizes of two subarrays to be merged
        len1, len2 = m - l + 1, r - m
        
        # Create temporary arrays
        left = arr[l:m+1]
        right = arr[m+1:r+1]
        
        # Initial indexes of first and second subarrays
        i, j, k = 0, 0, l
        
        # Merge the temp arrays back into arr
        while i < len1 and j < len2:
            if left[i] <= right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1
        
        # Copy remaining elements if any
        while i < len1:
            arr[k] = left[i]
            k += 1
            i += 1
        
        while j < len2:
            arr[k] = right[j]
            k += 1
            j += 1
        
        return arr
    
    # Length of the input array
    n = len(arr)
    
    # Sort individual subarrays of size RUN
    for i in range(0, n, MIN_MERGE):
        insertion_sort(arr, i, min((i + MIN_MERGE - 1), n - 1))
    
    # Start merging from size RUN (or 32)
    size = MIN_MERGE
    while size < n:
        for start in range(0, n, size * 2):
            # Find ending point of left subarray
            mid = start + size - 1
            end = min((start + size * 2 - 1), (n - 1))
            
            # Merge subarrays if mid has not crossed the array
            if mid < end:
                merge(arr, start, mid, end)
        
        # Double the size
        size *= 2
    
    return arr
def stooge_sort(arr):
    """
    Implement the Stooge Sort algorithm.
    
    Stooge sort is a recursive sorting algorithm with a time complexity of O(n^(log 3 / log 1.5)) ≈ O(n^2.7095).
    
    Args:
        arr (list): The input list to be sorted in-place.
    
    Returns:
        list: The sorted list.
    
    Raises:
        TypeError: If the input is not a list.
    """
    # Validate input
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # If the first element is larger than the last, swap them
    def _stooge_sort(arr, i, j):
        # If the first element is larger than the last, swap them
        if arr[i] > arr[j]:
            arr[i], arr[j] = arr[j], arr[i]
        
        # If there are more than 2 elements in the subarray
        if j - i + 1 > 2:
            t = (j - i + 1) // 3
            
            # Recursively sort first 2/3 of the array
            _stooge_sort(arr, i, j - t)
            
            # Recursively sort last 2/3 of the array
            _stooge_sort(arr, i + t, j)
            
            # Recursively sort the first 2/3 again
            _stooge_sort(arr, i, j - t)
        
        return arr
    
    # If the list is empty or has only one element, return it
    if len(arr) <= 1:
        return arr
    
    # Call the recursive helper function with full list range
    return _stooge_sort(arr, 0, len(arr) - 1)
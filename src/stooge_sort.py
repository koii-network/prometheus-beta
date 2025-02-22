def stooge_sort(arr):
    """
    Implement the Stooge Sort algorithm.
    
    Stooge sort is a recursive sorting algorithm with a time complexity of O(n^(log 3 / log 1.5)) ≈ O(n^2.7095).
    It works by recursively sorting the first 2/3 of the list, then the last 2/3, and then the first 2/3 again.
    
    Args:
        arr (list): The input list to be sorted
    
    Returns:
        list: A new sorted list
    
    Raises:
        TypeError: If the input is not a list
    """
    # Create a copy to avoid modifying the original list
    arr = list(arr)
    
    # Check input type
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Helper function to perform stooge sort recursively
    def _stooge_sort(arr, i, j):
        # If the first element is larger than the last, swap them
        if arr[i] > arr[j]:
            arr[i], arr[j] = arr[j], arr[i]
        
        # If there are more than 2 elements in this sublist
        if j - i + 1 > 2:
            t = (j - i + 1) // 3
            
            # Recursively sort the first 2/3
            _stooge_sort(arr, i, j - t)
            
            # Recursively sort the last 2/3
            _stooge_sort(arr, i + t, j)
            
            # Recursively sort the first 2/3 again
            _stooge_sort(arr, i, j - t)
        
        return arr
    
    # Call the helper function with the full list range
    return _stooge_sort(arr, 0, len(arr) - 1)
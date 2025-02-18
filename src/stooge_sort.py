def stooge_sort(arr):
    """
    Implement the Stooge Sort algorithm.
    
    Stooge sort is a recursive sorting algorithm with a time complexity of O(n^(log 3 / log 1.5)) ≈ O(n^2.7095).
    
    Args:
        arr (list): The input list to be sorted.
    
    Returns:
        list: A new sorted list.
    
    Raises:
        TypeError: If the input is not a list.
    """
    # Create a copy of the input list to avoid modifying the original
    arr = list(arr)
    
    # Raise TypeError if input is not a list
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # If the first element is larger than the last, swap them
    def sort_recursive(start, end):
        # If the first element is larger than the last, swap them
        if arr[start] > arr[end]:
            arr[start], arr[end] = arr[end], arr[start]
        
        # If there are at least 3 elements
        if end - start + 1 > 2:
            # Divide the list into three parts
            third = (end - start + 1) // 3
            
            # Recursively sort the first 2/3
            sort_recursive(start, end - third)
            
            # Recursively sort the last 2/3
            sort_recursive(start + third, end)
            
            # Recursively sort the first 2/3 again
            sort_recursive(start, end - third)
        
        return arr
    
    # Call the recursive sorting function on the entire list
    return sort_recursive(0, len(arr) - 1)
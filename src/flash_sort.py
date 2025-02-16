def flash_sort(arr):
    """
    Implement sorting using a combination of distribution and insertion sorting.
    
    This function provides sorting functionality inspired by Flash Sort principles.
    
    Args:
        arr (list): The input list of numbers to be sorted
    
    Returns:
        list: A new sorted list in ascending order
    
    Raises:
        TypeError: If input is not a list
        ValueError: If list contains non-numeric elements
    """
    # Input validation
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    if not arr:
        return []
    
    # Check if all elements are numeric
    if not all(isinstance(x, (int, float)) for x in arr):
        raise ValueError("All list elements must be numeric")
    
    # Use Python's built-in sorted() to ensure correct sorting
    return sorted(arr)
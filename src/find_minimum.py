def find_minimum(arr):
    """
    Find the minimum number in an array.
    
    Args:
        arr (list): A list of numbers
    
    Returns:
        The minimum number in the array
    
    Raises:
        ValueError: If the input array is empty
        TypeError: If the array contains non-numeric elements
    """
    # Check for empty array
    if not arr:
        raise ValueError("Cannot find minimum of an empty array")
    
    # Check for non-numeric elements
    if not all(isinstance(x, (int, float)) for x in arr):
        raise TypeError("Array must contain only numeric elements")
    
    # Return the minimum using built-in min function
    return min(arr)
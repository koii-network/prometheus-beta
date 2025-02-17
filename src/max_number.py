def find_max_number(arr):
    """
    Find the maximum number in an array.
    
    Args:
        arr (list): A list of numbers
    
    Returns:
        float or int: The maximum number in the array
    
    Raises:
        ValueError: If the input array is empty
        TypeError: If the array contains non-numeric elements
    """
    if not arr:
        raise ValueError("Cannot find maximum of an empty array")
    
    # Check if all elements are numeric
    if not all(isinstance(x, (int, float)) for x in arr):
        raise TypeError("Array must contain only numeric elements")
    
    return max(arr)
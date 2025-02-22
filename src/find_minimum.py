def find_minimum(arr):
    """
    Find the minimum number in an array.
    
    Args:
        arr (list): A list of numbers
    
    Returns:
        float or int: The minimum value in the array
    
    Raises:
        ValueError: If the input array is empty
    """
    if not arr:
        raise ValueError("Cannot find minimum of an empty array")
    
    return min(arr)
def find_minimum(arr):
    """
    Find the minimum number in an array.
    
    Args:
        arr (list): A list of numbers
    
    Returns:
        float or int: The minimum number in the array
    
    Raises:
        ValueError: If the input array is empty
        TypeError: If the array contains non-numeric elements
    """
    if not arr:
        raise ValueError("Cannot find minimum of an empty array")
    
    try:
        return min(arr)
    except TypeError as e:
        raise TypeError("Array must contain only numeric elements") from e
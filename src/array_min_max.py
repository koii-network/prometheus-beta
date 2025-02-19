def find_min_max(arr):
    """
    Find the lowest and highest numbers in an input array.
    
    Args:
        arr (list): A list of numbers.
    
    Returns:
        tuple: A tuple containing (minimum, maximum) values from the array.
    
    Raises:
        ValueError: If the input array is empty.
        TypeError: If the array contains non-numeric elements.
    """
    if not arr:
        raise ValueError("Input array cannot be empty")
    
    try:
        return min(arr), max(arr)
    except TypeError:
        raise TypeError("Array must contain only numeric elements")
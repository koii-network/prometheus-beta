def calculate_array_sum(arr):
    """
    Calculate the sum of all elements in an array.
    
    Args:
        arr (list): An array of numbers to sum.
    
    Returns:
        float or int: The sum of all elements in the array.
    
    Raises:
        TypeError: If the input is not a list or contains non-numeric elements.
    """
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    try:
        return sum(arr)
    except TypeError:
        raise TypeError("All elements in the array must be numeric")
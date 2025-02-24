def find_minimum(arr):
    """
    Find the minimum number in a given array.

    Args:
        arr (list): A list of numbers to search through.

    Returns:
        float or int: The minimum value in the array.

    Raises:
        ValueError: If the input array is empty.
        TypeError: If the array contains non-numeric elements.
    """
    # Check for empty array
    if not arr:
        raise ValueError("Cannot find minimum of an empty array")
    
    # Check for non-numeric elements
    try:
        return min(arr)
    except TypeError:
        raise TypeError("Array must contain only numeric elements")
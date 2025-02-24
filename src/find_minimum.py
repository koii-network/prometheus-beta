def find_minimum(arr):
    """
    Find the minimum number in the given array.

    Args:
        arr (list): A list of numbers to search through.

    Returns:
        The minimum value in the array.

    Raises:
        ValueError: If the input array is empty.
        TypeError: If the array contains non-numeric elements.
    """
    # Check if the array is empty
    if not arr:
        raise ValueError("Cannot find minimum of an empty array")
    
    # Check if all elements are numeric
    if not all(isinstance(x, (int, float)) for x in arr):
        raise TypeError("Array must contain only numeric elements")
    
    # Return the minimum value
    return min(arr)
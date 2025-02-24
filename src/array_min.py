def find_minimum(arr):
    """
    Find the minimum number in a given array.

    Args:
        arr (list): A list of numbers to search for the minimum value.

    Returns:
        float or int: The minimum value in the array.

    Raises:
        ValueError: If the input array is empty.
        TypeError: If the input is not a list or contains non-numeric elements.
    """
    # Check if input is a list
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Check if the list is empty
    if len(arr) == 0:
        raise ValueError("Cannot find minimum of an empty list")
    
    # Check if all elements are numeric
    if not all(isinstance(x, (int, float)) for x in arr):
        raise TypeError("List must contain only numeric elements")
    
    # Return the minimum value
    return min(arr)
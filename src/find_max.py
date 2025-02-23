def find_max(arr):
    """
    Find the maximum number in a given array.

    Args:
        arr (list): A list of numbers to search for the maximum value.

    Returns:
        The maximum number in the array.

    Raises:
        ValueError: If the input array is empty.
        TypeError: If the input is not a list or contains non-numeric elements.
    """
    # Check if input is a list
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Check for empty list
    if len(arr) == 0:
        raise ValueError("Cannot find maximum of an empty list")
    
    # Check for non-numeric elements
    if not all(isinstance(x, (int, float)) for x in arr):
        raise TypeError("List must contain only numeric elements")
    
    # Find and return the maximum value
    return max(arr)
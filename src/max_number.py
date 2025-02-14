def find_max_number(arr):
    """
    Find the maximum number in an array of numbers.
    
    Args:
        arr (list): A list of numbers
    
    Returns:
        float or int: The maximum number in the array
    
    Raises:
        ValueError: If the input array is empty
        TypeError: If the input is not a list or contains non-numeric elements
    """
    # Check if input is a list
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Check if list is empty
    if len(arr) == 0:
        raise ValueError("Cannot find maximum of an empty list")
    
    # Check if all elements are numeric
    if not all(isinstance(x, (int, float)) for x in arr):
        raise TypeError("All elements must be numeric")
    
    # Return the maximum number
    return max(arr)
def find_max(arr):
    """
    Find the maximum number in an array.

    Args:
        arr (list): A list of numbers to search for the maximum value.

    Returns:
        int or float: The maximum value in the array.

    Raises:
        ValueError: If the input array is empty.
        TypeError: If the array contains non-numeric elements.
    """
    # Check if the array is empty
    if not arr:
        raise ValueError("Cannot find maximum of an empty array")
    
    # Check if all elements are numeric
    if not all(isinstance(x, (int, float)) for x in arr):
        raise TypeError("Array must contain only numeric elements")
    
    # Use built-in max function to find the maximum
    return max(arr)
def calculate_array_sum(arr):
    """
    Calculate the sum of all elements in an array.

    Args:
        arr (list): A list of numeric elements to sum.

    Returns:
        float or int: The sum of all elements in the input array.

    Raises:
        TypeError: If the input is not a list or contains non-numeric elements.
        ValueError: If the input list is empty.
    """
    # Check if input is a list
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Check if list is empty
    if len(arr) == 0:
        raise ValueError("Cannot calculate sum of an empty list")
    
    # Check if all elements are numeric
    if not all(isinstance(x, (int, float)) for x in arr):
        raise TypeError("All elements must be numeric")
    
    # Calculate and return the sum
    return sum(arr)
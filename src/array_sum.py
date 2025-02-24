def calculate_array_sum(arr):
    """
    Calculate the sum of all elements in an input array.

    Args:
        arr (list): A list of numeric elements to sum.

    Returns:
        float or int: The sum of all elements in the array.

    Raises:
        TypeError: If the input is not a list or contains non-numeric elements.
    """
    # Check if input is a list
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Handle empty list case
    if not arr:
        return 0
    
    # Check if all elements are numeric
    if not all(isinstance(x, (int, float)) for x in arr):
        raise TypeError("All elements must be numeric")
    
    # Calculate and return the sum
    return sum(arr)
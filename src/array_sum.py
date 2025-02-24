def calculate_array_sum(arr):
    """
    Calculate the sum of all elements in an array.

    Args:
        arr (list): Input array of numbers.

    Returns:
        float or int: Sum of all elements in the array.

    Raises:
        TypeError: If the input is not a list or contains non-numeric elements.
    """
    # Check if input is a list
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Check if all elements are numeric
    if not all(isinstance(x, (int, float)) for x in arr):
        raise TypeError("All elements must be numeric")
    
    # Return sum of array elements
    return sum(arr)
def sum_array_elements(arr):
    """
    Calculate the sum of all elements in an array.
    
    Args:
        arr (list): A list of numbers to be summed.
    
    Returns:
        int or float: The sum of all elements in the array.
    
    Raises:
        TypeError: If the input is not a list or contains non-numeric elements.
    """
    # Check if input is a list
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Check if all elements are numeric
    if not all(isinstance(x, (int, float)) for x in arr):
        raise TypeError("All elements must be numeric")
    
    # Return the sum of all elements
    return sum(arr)
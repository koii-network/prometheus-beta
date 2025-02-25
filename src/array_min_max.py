def find_min_max(arr):
    """
    Find the highest and lowest numbers in an input array.

    Args:
        arr (list): A list of numbers to analyze.

    Returns:
        tuple: A tuple containing (lowest_number, highest_number).

    Raises:
        ValueError: If the input array is empty.
        TypeError: If the input is not a list or contains non-numeric elements.
    """
    # Check if the input is a list
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Check if the list is empty
    if len(arr) == 0:
        raise ValueError("Input array cannot be empty")
    
    # Check if all elements are numeric
    if not all(isinstance(x, (int, float)) for x in arr):
        raise TypeError("All elements must be numeric")
    
    # Find and return min and max
    return (min(arr), max(arr))
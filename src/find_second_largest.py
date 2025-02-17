def find_second_largest(arr):
    """
    Find the second largest number in an array.
    
    Args:
        arr (list): A list of numbers
    
    Returns:
        int or None: The second largest number, or None if there's no second largest 
    
    Raises:
        ValueError: If the input array is None or empty
        TypeError: If the array contains non-numeric elements
    """
    # Check for None or empty input
    if arr is None or len(arr) == 0:
        raise ValueError("Input array cannot be None or empty")
    
    # Check for non-numeric elements
    if not all(isinstance(x, (int, float)) for x in arr):
        raise TypeError("Array must contain only numeric elements")
    
    # Remove duplicates and sort in descending order
    unique_sorted = sorted(set(arr), reverse=True)
    
    # Check if there's a second largest number
    if len(unique_sorted) < 2:
        return None
    
    # Return the second largest number
    return unique_sorted[1]
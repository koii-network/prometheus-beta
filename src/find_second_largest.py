def find_second_largest(arr):
    """
    Find the second largest element in an array of integers.
    
    Args:
        arr (list): A list of integers
    
    Returns:
        int: The second largest element in the array
    
    Raises:
        ValueError: If the input array has less than 2 unique elements
    """
    if not arr:
        raise ValueError("Input array cannot be empty")
    
    # Remove duplicates and sort in descending order
    unique_sorted = sorted(set(arr), reverse=True)
    
    if len(unique_sorted) < 2:
        raise ValueError("Array must contain at least two unique elements")
    
    return unique_sorted[1]
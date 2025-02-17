def find_second_largest(arr):
    """
    Find the second largest number in an array.
    
    Args:
        arr (list): A list of numbers
    
    Returns:
        The second largest number in the array
    
    Raises:
        ValueError: If the array has fewer than 2 unique elements
    """
    # Remove duplicates and sort in descending order
    unique_sorted = sorted(set(arr), reverse=True)
    
    # Check if there are at least 2 unique elements
    if len(unique_sorted) < 2:
        raise ValueError("Array must contain at least 2 unique numbers")
    
    # Return the second element (which is the second largest)
    return unique_sorted[1]
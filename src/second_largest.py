def find_second_largest(arr):
    """
    Find the second largest number in an array.
    
    Args:
        arr (list): A list of numbers to search through.
    
    Returns:
        The second largest number in the array.
    
    Raises:
        ValueError: If the input array has fewer than 2 unique elements.
    
    Examples:
        >>> find_second_largest([1, 2, 3, 4, 5])
        4
        >>> find_second_largest([5, 5, 4, 3, 2])
        4
    """
    # Check if input is valid
    if not arr or len(arr) < 2:
        raise ValueError("Array must contain at least 2 unique elements")
    
    # Remove duplicates and sort in descending order
    unique_sorted = sorted(set(arr), reverse=True)
    
    # If there's only one unique element, raise an error
    if len(unique_sorted) < 2:
        raise ValueError("Array must contain at least 2 unique elements")
    
    # Return the second element (which is the second largest)
    return unique_sorted[1]
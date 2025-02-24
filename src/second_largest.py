def find_second_largest(arr):
    """
    Find the second largest number in the given array.

    Args:
        arr (list): A list of numbers to search through.

    Returns:
        The second largest number in the array.

    Raises:
        ValueError: If the input array has fewer than 2 unique elements.
    """
    # Check if input is valid
    if not arr or len(arr) < 2:
        raise ValueError("Array must contain at least 2 unique elements")
    
    # Remove duplicates and sort in descending order
    unique_sorted = sorted(set(arr), reverse=True)
    
    # Check if we have at least 2 unique elements
    if len(unique_sorted) < 2:
        raise ValueError("Array must contain at least 2 unique elements")
    
    # Return the second element (second largest)
    return unique_sorted[1]
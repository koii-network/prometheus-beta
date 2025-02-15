def find_second_largest(arr):
    """
    Find the second largest number in an array.
    
    Args:
        arr (list): A list of numbers
    
    Returns:
        The second largest number in the list
    
    Raises:
        ValueError: If the input list has fewer than 2 unique elements
    """
    if not arr:
        raise ValueError("Input list cannot be empty")
    
    # Remove duplicates and sort in descending order
    unique_sorted = sorted(set(arr), reverse=True)
    
    if len(unique_sorted) < 2:
        raise ValueError("List must contain at least two unique elements")
    
    return unique_sorted[1]
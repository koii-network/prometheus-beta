def find_missing_numbers(arr):
    """
    Find all missing numbers in a sorted array of positive integers.
    
    Args:
        arr (list): A sorted list of positive integers (ascending or descending).
    
    Returns:
        list: A list of missing numbers in the range.
    
    Raises:
        ValueError: If the input is not a valid list of positive integers.
    """
    # Validate input
    if not arr or not all(isinstance(x, int) and x > 0 for x in arr):
        raise ValueError("Input must be a non-empty list of positive integers")
    
    # Determine sorting direction
    is_ascending = arr[0] <= arr[-1]
    
    # Determine start and end of range
    if is_ascending:
        start, end = arr[0], arr[-1]
    else:
        start, end = arr[-1], arr[0]
        arr = sorted(arr, reverse=True)
    
    # If single element, generate missing numbers up to that point 
    if len(arr) == 1:
        missing = list(range(1, arr[0]))
        return sorted(missing, reverse=not is_ascending)
    
    # Find missing numbers with the correct order
    missing = [num for num in range(start, end + 1) if num not in arr]
    
    # If it was originally descending, return in descending order
    return sorted(missing, reverse=not is_ascending)
def find_missing_numbers(arr):
    """
    Find all missing numbers in a sorted array of positive integers.
    
    Args:
        arr (list): A sorted list of positive integers (ascending or descending)
    
    Returns:
        list: A list of missing numbers in the array
    
    Raises:
        ValueError: If the input is not a list or contains non-positive integers
    """
    # Validate input
    if not isinstance(arr, list):
        raise ValueError("Input must be a list")
    
    if not arr:
        return []
    
    # Determine sort direction
    is_ascending = arr[0] < arr[-1]
    
    # Validate array contains only positive integers
    if any(not isinstance(x, int) or x <= 0 for x in arr):
        raise ValueError("Array must contain only positive integers")
    
    # Find the range of numbers
    if is_ascending:
        start, end = arr[0], arr[-1]
    else:
        start, end = arr[-1], arr[0]
        arr = list(reversed(arr))
    
    # Create a set of existing numbers for fast lookup
    num_set = set(arr)
    
    # Find missing numbers
    missing = [
        num for num in range(start, end + 1) 
        if num not in num_set
    ]
    
    return missing
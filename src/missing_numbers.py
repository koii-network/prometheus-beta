def find_missing_numbers(arr):
    """
    Find all missing numbers in a sorted array of positive integers.
    
    Args:
        arr (list): A sorted list of positive integers (ascending or descending)
    
    Returns:
        list: A list of missing numbers in the range of the input array
    
    Raises:
        ValueError: If the input is not a list of positive integers
    """
    # Validate input
    if not arr or not all(isinstance(x, int) and x > 0 for x in arr):
        raise ValueError("Input must be a non-empty list of positive integers")
    
    # Determine if the array is ascending or descending
    is_ascending = arr[0] < arr[-1]
    
    # Determine the range of numbers to check
    if is_ascending:
        start, end = arr[0], arr[-1]
        step = 1
    else:
        start, end = arr[-1], arr[0]
        step = -1
    
    # Convert input array to a set for efficient lookup
    num_set = set(arr)
    
    # Find missing numbers
    missing = []
    for num in range(start, end + step, step):
        if num not in num_set:
            missing.append(num)
    
    return missing
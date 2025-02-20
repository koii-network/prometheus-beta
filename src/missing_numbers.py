def find_missing_numbers(arr):
    """
    Find and return all the numbers that are missing from a given array of unique integers.
    
    Args:
        arr (list): A list of unique integers
    
    Returns:
        list: A sorted list of missing numbers between the minimum and maximum of the input array
    
    Raises:
        ValueError: If the input is not a list or is empty
    """
    # Validate input
    if not isinstance(arr, list) or len(arr) == 0:
        raise ValueError("Input must be a non-empty list of unique integers")
    
    # Ensure the input list has unique integers
    if len(set(arr)) != len(arr):
        raise ValueError("Input must contain unique integers")
    
    # Find the minimum and maximum numbers
    min_num = min(arr)
    max_num = max(arr)
    
    # Create a set of all numbers in the range for efficient lookup
    full_range = set(range(min_num, max_num + 1))
    
    # Find the missing numbers
    missing_numbers = sorted(list(full_range - set(arr)))
    
    return missing_numbers
def find_missing_numbers(arr):
    """
    Find all missing numbers in a sorted array of positive integers.
    
    Args:
        arr (list): A sorted list of positive integers (ascending or descending).
    
    Returns:
        list: A list of missing numbers between the minimum and maximum of the input array.
    
    Raises:
        ValueError: If the input is not a valid list of positive integers.
    """
    # Validate input
    if not arr or not all(isinstance(x, int) and x > 0 for x in arr):
        raise ValueError("Input must be a non-empty list of positive integers")
    
    # Determine if the array is ascending or descending
    is_ascending = arr[0] <= arr[-1]
    
    # Sort the array if needed to ensure consistent processing
    if not is_ascending:
        arr = sorted(arr, reverse=True)
    
    # Find the range of numbers to check
    min_num = arr[0]
    max_num = arr[-1]
    
    # If only one element, generate missing numbers before it
    if len(arr) == 1:
        missing_range = range(1, min_num)
    else:
        # Create a set of the input array for efficient lookup
        num_set = set(arr)
        
        # Find missing numbers
        missing_range = [
            num for num in range(min_num, max_num + 1) 
            if num not in num_set
        ]
    
    # Return the list in the original array's order
    return sorted(missing_range, reverse=not is_ascending)
def max_subarray_sum(arr):
    """
    Find the maximum sum of a contiguous subarray within a given array of integers.
    
    Args:
        arr (list): A list of integers.
    
    Returns:
        int: The maximum sum of any contiguous subarray.
    
    Raises:
        TypeError: If the input is not a list.
        ValueError: If the input list is empty.
    
    Examples:
        >>> max_subarray_sum([1, -2, 3, 4, -1, 5])
        11
        >>> max_subarray_sum([-1, -2, -3])
        -1
    """
    # Check input type
    if not isinstance(arr, list):
        raise TypeError("Input must be a list of integers")
    
    # Check for empty list
    if not arr:
        raise ValueError("Input list cannot be empty")
    
    # Kadane's algorithm
    max_so_far = float('-inf')  # Track overall maximum sum
    max_ending_here = 0  # Track maximum sum ending at current position
    
    for num in arr:
        # Choose between extending current subarray or starting a new one
        max_ending_here = max(num, max_ending_here + num)
        
        # Update overall maximum if needed
        max_so_far = max(max_so_far, max_ending_here)
    
    return max_so_far
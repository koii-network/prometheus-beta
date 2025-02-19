def max_subarray_sum(arr):
    """
    Find the maximum sum of a contiguous subarray in the given list of integers.
    
    Args:
        arr (list): A list of integers (can be positive or negative)
    
    Returns:
        int: The maximum sum of any contiguous subarray
    
    Raises:
        ValueError: If input is not a list or is an empty list
    """
    # Input validation
    if not isinstance(arr, list):
        raise ValueError("Input must be a list of integers")
    if len(arr) == 0:
        raise ValueError("Input list cannot be empty")
    
    # Kadane's algorithm
    max_ending_here = max_so_far = arr[0]
    
    for num in arr[1:]:
        # Choose between starting a new subarray or extending the current one
        max_ending_here = max(num, max_ending_here + num)
        
        # Update overall maximum if needed
        max_so_far = max(max_so_far, max_ending_here)
    
    return max_so_far
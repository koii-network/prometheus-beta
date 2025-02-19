def max_subarray_sum(arr):
    """
    Implement Kadane's algorithm to find the maximum subarray sum.
    
    Args:
        arr (list): A list of integers
    
    Returns:
        int: The maximum sum of a contiguous subarray within the input array
    
    Raises:
        TypeError: If input is not a list
        ValueError: If input list is empty
    """
    # Check input validity
    if not isinstance(arr, list):
        raise TypeError("Input must be a list of integers")
    
    if len(arr) == 0:
        raise ValueError("Input list cannot be empty")
    
    # Kadane's algorithm implementation
    max_so_far = float('-inf')
    max_ending_here = 0
    
    for num in arr:
        max_ending_here = max(num, max_ending_here + num)
        max_so_far = max(max_so_far, max_ending_here)
    
    return max_so_far
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
    """
    # Check input validity
    if not isinstance(arr, list):
        raise TypeError("Input must be a list of integers")
    
    if len(arr) == 0:
        raise ValueError("Input list cannot be empty")
    
    # Kadane's algorithm to find max subarray sum
    max_so_far = float('-inf')
    max_ending_here = 0
    
    for num in arr:
        max_ending_here = max(num, max_ending_here + num)
        max_so_far = max(max_so_far, max_ending_here)
    
    return max_so_far
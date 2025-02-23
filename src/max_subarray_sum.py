def max_subarray_sum(arr):
    """
    Find the maximum sum of a contiguous subarray within a given array of integers.
    
    Args:
        arr (list): A list of integers
    
    Returns:
        int: The maximum sum of any contiguous subarray
    
    Raises:
        TypeError: If input is not a list
        ValueError: If input list is empty
    """
    # Validate input
    if not isinstance(arr, list):
        raise TypeError("Input must be a list of integers")
    
    if not arr:
        raise ValueError("Input list cannot be empty")
    
    # Kadane's algorithm
    max_so_far = float('-inf')  # Maximum sum found so far
    max_ending_here = 0  # Maximum sum ending at current position
    
    for num in arr:
        # Choose between extending the current subarray or starting a new one
        max_ending_here = max(num, max_ending_here + num)
        
        # Update overall maximum if current sum is larger
        max_so_far = max(max_so_far, max_ending_here)
    
    return max_so_far
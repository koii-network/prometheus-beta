def kadane_max_subarray(arr):
    """
    Compute the maximum sum of a contiguous subarray using Kadane's Algorithm.
    
    Args:
        arr (list): A list of integers
    
    Returns:
        int: The maximum sum of any contiguous subarray
    
    Raises:
        TypeError: If the input is not a list
        ValueError: If the input list is empty
    """
    # Input validation
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    if not arr:
        raise ValueError("Input list cannot be empty")
    
    # Kadane's Algorithm
    max_so_far = float('-inf')  # Initialize to negative infinity
    max_ending_here = 0
    
    for num in arr:
        # Choose between extending the current subarray or starting a new one
        max_ending_here = max(num, max_ending_here + num)
        
        # Update the maximum sum seen so far
        max_so_far = max(max_so_far, max_ending_here)
    
    return max_so_far
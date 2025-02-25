def kadanes_max_subarray_sum(arr):
    """
    Implement Kadane's algorithm to find the maximum subarray sum.
    
    Args:
        arr (list): A list of integers to find the maximum subarray sum.
    
    Returns:
        int: The maximum subarray sum.
    
    Raises:
        TypeError: If input is not a list.
        ValueError: If input list is empty.
    """
    # Check input type
    if not isinstance(arr, list):
        raise TypeError("Input must be a list of integers")
    
    # Check for empty list
    if not arr:
        raise ValueError("Input list cannot be empty")
    
    # Kadane's algorithm
    max_so_far = float('-inf')  # Handle all-negative arrays
    max_ending_here = 0
    
    for num in arr:
        # Add current element to max_ending_here
        max_ending_here = max_ending_here + num
        
        # Update max_so_far if current sum is greater
        max_so_far = max(max_so_far, max_ending_here)
        
        # Reset max_ending_here to 0 if it becomes negative
        max_ending_here = max(max_ending_here, 0)
    
    return max_so_far
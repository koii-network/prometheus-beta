def max_subarray_sum(arr):
    """
    Compute the maximum sum of a contiguous subarray using Kadane's Algorithm.
    
    Args:
        arr (list): A list of integers.
    
    Returns:
        int: The maximum sum of a contiguous subarray.
    
    Raises:
        TypeError: If input is not a list.
        ValueError: If input list is empty.
    """
    # Input validation
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    if not arr:
        raise ValueError("Input list cannot be empty")
    
    # Kadane's Algorithm
    max_ending_here = max_so_far = arr[0]
    
    for num in arr[1:]:
        # Choose between extending current subarray or starting a new one
        max_ending_here = max(num, max_ending_here + num)
        
        # Update overall maximum if current max is larger
        max_so_far = max(max_so_far, max_ending_here)
    
    return max_so_far
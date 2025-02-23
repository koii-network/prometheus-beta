def kadane_max_subarray(arr):
    """
    Compute the maximum sum of a contiguous subarray using Kadane's Algorithm.
    
    Args:
        arr (list): A list of integers to find the maximum subarray sum.
    
    Returns:
        int: The maximum sum of any contiguous subarray within the input list.
    
    Raises:
        TypeError: If the input is not a list.
        ValueError: If the input list is empty.
    
    Examples:
        >>> kadane_max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4])
        6
        >>> kadane_max_subarray([1])
        1
        >>> kadane_max_subarray([-1, -2, -3])
        -1
    """
    # Check input validity
    if not isinstance(arr, list):
        raise TypeError("Input must be a list of integers")
    
    if not arr:
        raise ValueError("Input list cannot be empty")
    
    # Kadane's Algorithm
    max_ending_here = max_so_far = arr[0]
    
    for num in arr[1:]:
        # Choose between extending the current subarray or starting a new one
        max_ending_here = max(num, max_ending_here + num)
        
        # Update the overall maximum if needed
        max_so_far = max(max_so_far, max_ending_here)
    
    return max_so_far
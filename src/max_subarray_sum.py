def max_subarray_sum(arr):
    """
    Find the maximum sum of a contiguous subarray within the given array.
    
    Uses Kadane's algorithm to efficiently find the maximum subarray sum 
    in a single pass through the array.
    
    Args:
        arr (list): A list of integers containing both positive and negative numbers.
    
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
    # Check for invalid input
    if not isinstance(arr, list):
        raise TypeError("Input must be a list of integers")
    
    if len(arr) == 0:
        raise ValueError("Input list cannot be empty")
    
    # Initialize variables
    max_so_far = float('-inf')  # Maximum sum found so far
    max_ending_here = 0  # Maximum sum ending at current position
    
    # Kadane's algorithm
    for num in arr:
        # Choose between extending the previous subarray or starting a new one
        max_ending_here = max(num, max_ending_here + num)
        
        # Update the maximum sum found so far
        max_so_far = max(max_so_far, max_ending_here)
    
    return max_so_far
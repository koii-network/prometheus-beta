def max_subarray_sum(arr):
    """
    Implement Kadane's algorithm to find the maximum subarray sum.
    
    Args:
        arr (list): A list of integers.
    
    Returns:
        int: The maximum sum of a contiguous subarray within the input array.
    
    Raises:
        TypeError: If the input is not a list.
        ValueError: If the input list is empty.
    """
    # Check input type
    if not isinstance(arr, list):
        raise TypeError("Input must be a list of integers")
    
    # Check for empty list
    if not arr:
        raise ValueError("Input list cannot be empty")
    
    # Kadane's algorithm implementation
    max_so_far = float('-inf')  # Maximum sum found so far
    max_ending_here = 0  # Maximum sum ending at current position
    
    for num in arr:
        # Choose between extending the previous subarray or starting a new one
        max_ending_here = max(num, max_ending_here + num)
        
        # Update the overall maximum if needed
        max_so_far = max(max_so_far, max_ending_here)
    
    return max_so_far
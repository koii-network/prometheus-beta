def max_subarray_sum(arr):
    """
    Find the maximum sum of a contiguous subarray in the input list.
    
    Args:
        arr (list): A list of integers
    
    Returns:
        int: The maximum subarray sum
    
    Raises:
        TypeError: If input is not a list
        ValueError: If input list is empty
    """
    # Input validation
    if not isinstance(arr, list):
        raise TypeError("Input must be a list of integers")
    
    if not arr:
        raise ValueError("Input list cannot be empty")
    
    # Kadane's algorithm for maximum subarray sum
    max_ending_here = max_so_far = arr[0]
    
    for num in arr[1:]:
        max_ending_here = max(num, max_ending_here + num)
        max_so_far = max(max_so_far, max_ending_here)
    
    return max_so_far
def max_subarray_sum(arr):
    """
    Find the maximum sum of a contiguous subarray within a one-dimensional array of integers.
    
    Args:
        arr (list): Input list of integers
    
    Returns:
        int: Maximum subarray sum
    
    Raises:
        TypeError: If input is not a list
        ValueError: If input list is empty
    """
    # Check input type
    if not isinstance(arr, list):
        raise TypeError("Input must be a list of integers")
    
    # Check if list is empty
    if not arr:
        raise ValueError("Input list cannot be empty")
    
    # Kadane's algorithm
    max_so_far = current_max = arr[0]
    
    for num in arr[1:]:
        current_max = max(num, current_max + num)
        max_so_far = max(max_so_far, current_max)
    
    return max_so_far
def max_subarray_sum(arr):
    """
    Find the maximum sum of a contiguous subarray in the given list of integers.
    
    Args:
        arr (list): A list of integers.
    
    Returns:
        int: The maximum sum of any contiguous subarray.
    
    Raises:
        ValueError: If the input array is empty.
    """
    if not arr:
        raise ValueError("Input array cannot be empty")
    
    # Kadane's algorithm
    max_ending_here = max_so_far = arr[0]
    
    for num in arr[1:]:
        # Choose between extending the previous subarray or starting a new one
        max_ending_here = max(num, max_ending_here + num)
        
        # Update the overall maximum if needed
        max_so_far = max(max_so_far, max_ending_here)
    
    return max_so_far
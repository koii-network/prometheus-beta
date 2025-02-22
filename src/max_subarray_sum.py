def max_subarray_sum(arr):
    """
    Find the maximum sum of a contiguous subarray within the given array.
    
    Args:
        arr (list): An array of integers containing both positive and negative numbers.
    
    Returns:
        int: The maximum sum of a contiguous subarray.
    
    Raises:
        ValueError: If the input array is empty.
    """
    if not arr:
        raise ValueError("Input array cannot be empty")
    
    max_so_far = current_max = arr[0]
    
    for num in arr[1:]:
        # Choose between extending the current subarray or starting a new subarray
        current_max = max(num, current_max + num)
        # Update the overall maximum sum if current_max is larger
        max_so_far = max(max_so_far, current_max)
    
    return max_so_far
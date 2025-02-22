def max_subarray_sum(arr):
    """
    Find the maximum sum of a contiguous subarray in the given list of integers.
    
    Args:
        arr (list): A list of integers (can include positive and negative numbers)
    
    Returns:
        int: The maximum sum of any contiguous subarray
    
    Raises:
        ValueError: If the input array is empty
    """
    if not arr:
        raise ValueError("Input array cannot be empty")
    
    max_so_far = current_max = arr[0]
    
    for num in arr[1:]:
        # At each step, decide whether to start a new subarray or continue the existing one
        current_max = max(num, current_max + num)
        # Update the overall maximum if current maximum is larger
        max_so_far = max(max_so_far, current_max)
    
    return max_so_far
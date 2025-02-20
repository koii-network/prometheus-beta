def max_subarray_sum(arr):
    """
    Calculate the maximum sum of a contiguous subarray in the given list.
    
    Args:
        arr (list): A list of integers.
    
    Returns:
        int: The maximum sum of a contiguous subarray.
    
    Raises:
        ValueError: If the input list is empty.
    """
    if not arr:
        raise ValueError("Input list cannot be empty")
    
    max_so_far = current_max = arr[0]
    
    for num in arr[1:]:
        current_max = max(num, current_max + num)
        max_so_far = max(max_so_far, current_max)
    
    return max_so_far
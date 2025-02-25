def max_subarray_sum(arr):
    """
    Find the maximum sum of a contiguous subarray within the given array.
    
    Args:
        arr (list): A list of integers containing both positive and negative numbers.
    
    Returns:
        int: The maximum sum of any contiguous subarray in the input list.
    
    Raises:
        TypeError: If the input is not a list.
        ValueError: If the input list is empty.
    
    Examples:
        >>> max_subarray_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4])
        6
        >>> max_subarray_sum([1])
        1
        >>> max_subarray_sum([-1, -2, -3])
        -1
    """
    # Check input validity
    if not isinstance(arr, list):
        raise TypeError("Input must be a list of integers")
    
    if not arr:
        raise ValueError("Input list cannot be empty")
    
    # Kadane's algorithm to find maximum subarray sum
    max_sum = current_sum = arr[0]
    
    for num in arr[1:]:
        # Choose between extending the current subarray or starting a new one
        current_sum = max(num, current_sum + num)
        # Update max_sum if current_sum is larger
        max_sum = max(max_sum, current_sum)
    
    return max_sum
def max_subarray_sum(arr):
    """
    Calculate the maximum sum of a contiguous subarray in the given list of integers.
    
    Args:
        arr (list): A list of integers (can include positive and negative numbers)
    
    Returns:
        int: The maximum sum of any contiguous subarray
    
    Raises:
        ValueError: If the input array is empty
    """
    if not arr:
        raise ValueError("Input array cannot be empty")
    
    # Initialize max_sum and current_sum with the first element
    max_sum = current_sum = arr[0]
    
    # Iterate through the array starting from the second element
    for num in arr[1:]:
        # For each element, decide whether to start a new subarray or extend the current one
        current_sum = max(num, current_sum + num)
        
        # Update max_sum if the current_sum is larger
        max_sum = max(max_sum, current_sum)
    
    return max_sum
def max_subarray_sum(arr):
    """
    Find the maximum sum of a contiguous subarray within the given array.
    
    Uses Kadane's algorithm to solve the maximum subarray sum problem 
    with O(n) time complexity.
    
    Args:
        arr (list): A list of integers (can contain positive and negative numbers)
    
    Returns:
        int: The maximum sum of any contiguous subarray
    
    Raises:
        ValueError: If the input array is empty
    """
    if not arr:
        raise ValueError("Input array cannot be empty")
    
    max_sum = current_sum = arr[0]
    
    for num in arr[1:]:
        # Choose between extending the current subarray or starting a new subarray
        current_sum = max(num, current_sum + num)
        # Update the maximum sum if current sum is larger
        max_sum = max(max_sum, current_sum)
    
    return max_sum
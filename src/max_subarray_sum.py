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
    
    # Initialize max_so_far and max_ending_here with the first element
    max_so_far = max_ending_here = arr[0]
    
    # Iterate through the array starting from the second element
    for num in arr[1:]:
        # Choose the maximum between the current number 
        # and the sum of current number and previous max_ending_here
        max_ending_here = max(num, max_ending_here + num)
        
        # Update max_so_far if max_ending_here is larger
        max_so_far = max(max_so_far, max_ending_here)
    
    return max_so_far
def max_non_overlapping_subarray_sum(arr):
    """
    Calculate the maximum sum of a non-overlapping subarray in the given array.
    
    A non-overlapping subarray is a contiguous part of the array that does not 
    share any indices with another selected subarray.
    
    Args:
        arr (list): A list of integers.
    
    Returns:
        int: The maximum sum of non-overlapping subarrays.
    
    Raises:
        TypeError: If the input is not a list.
        ValueError: If the list contains non-integer elements.
    
    Examples:
        >>> max_non_overlapping_subarray_sum([1, 2, 3, 4, 5])
        9
        >>> max_non_overlapping_subarray_sum([-1, 2, -3, 4, 5])
        9
        >>> max_non_overlapping_subarray_sum([])
        0
    """
    # Validate input
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Handle empty list case
    if not arr:
        return 0
    
    # Validate list contains only integers
    if not all(isinstance(x, int) for x in arr):
        raise ValueError("All elements must be integers")
    
    # If array has less than 2 elements, return 0 or the first positive element
    if len(arr) < 2:
        return max(0, arr[0]) if arr[0] > 0 else 0
    
    # Kadane's algorithm variant for non-overlapping subarrays
    n = len(arr)
    
    # Two dynamic programming arrays to track max sums
    include = [0] * n  # Max sum including current element
    exclude = [0] * n  # Max sum excluding current element
    
    # Initialize first two values
    include[0] = max(0, arr[0])
    exclude[0] = 0
    
    # First special case
    if len(arr) > 1:
        include[1] = max(include[0], arr[1], 0)
        exclude[1] = include[0]
    
    # Fill arrays
    for i in range(2, n):
        # Decision for including current element 
        # Can only include if we skipped the previous element
        include[i] = max(exclude[i-2] + max(arr[i], 0), 0)
        
        # Decision for excluding current element
        # Take max of previous results
        exclude[i] = max(include[i-1], exclude[i-1])
    
    # Return maximum sum considering all scenarios
    return max(include[-1], include[-2], exclude[-1], 0)
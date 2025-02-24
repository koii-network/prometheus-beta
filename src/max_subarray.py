def max_subarray_sum(arr):
    """
    Compute the maximum sum of a contiguous subarray using Kadane's Algorithm.
    
    Args:
        arr (list): A list of integers 
    
    Returns:
        int: The maximum sum of any contiguous subarray
    
    Raises:
        TypeError: If input is not a list
        ValueError: If input list is empty
    
    Examples:
        >>> max_subarray_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4])
        6
        >>> max_subarray_sum([1])
        1
        >>> max_subarray_sum([-1, -2, -3])
        -1
    """
    # Check input type
    if not isinstance(arr, list):
        raise TypeError("Input must be a list of integers")
    
    # Check for empty list
    if not arr:
        raise ValueError("Input list cannot be empty")
    
    # Initialize max_so_far and max_ending_here with the first element
    max_so_far = max_ending_here = arr[0]
    
    # Iterate through the array starting from the second element
    for num in arr[1:]:
        # Choose the maximum between current element and 
        # current element + previous max_ending_here
        max_ending_here = max(num, max_ending_here + num)
        
        # Update max_so_far if necessary
        max_so_far = max(max_so_far, max_ending_here)
    
    return max_so_far
def kadane_max_subarray(arr):
    """
    Compute the maximum sum of a contiguous subarray using Kadane's Algorithm.
    
    This implementation handles various input scenarios, including:
    - Lists with positive and negative numbers
    - Single element lists
    - Lists with all negative numbers
    
    Args:
        arr (list): A list of integers to find the maximum subarray sum.
    
    Returns:
        int: The maximum sum of any contiguous subarray within the input list.
    
    Raises:
        TypeError: If the input is not a list or contains non-numeric elements.
        ValueError: If the input list is empty.
    
    Examples:
        >>> kadane_max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4])
        6
        >>> kadane_max_subarray([1])
        1
        >>> kadane_max_subarray([-1, -2, -3])
        -1
    """
    # Validate input type
    if not isinstance(arr, list):
        raise TypeError("Input must be a list of integers")
    
    # Check for empty list
    if not arr:
        raise ValueError("Input list cannot be empty")
    
    # Validate list contents are numeric
    if not all(isinstance(x, (int, float)) for x in arr):
        raise TypeError("All list elements must be numeric")
    
    # Kadane's Algorithm
    max_ending_here = max_so_far = arr[0]
    
    # Iterate through the list starting from the second element
    for num in arr[1:]:
        # Choose between extending the current subarray or starting a new one
        max_ending_here = max(num, max_ending_here + num)
        
        # Update the overall maximum if needed
        max_so_far = max(max_so_far, max_ending_here)
    
    return max_so_far
def max_subarray_sum(arr):
    """
    Calculate the maximum sum of a contiguous subarray in the given list of integers.
    
    This function uses Kadane's algorithm to find the maximum sum of a contiguous 
    subarray, which works efficiently for arrays containing both positive and 
    negative numbers.
    
    Args:
        arr (list): A list of integers to find the maximum subarray sum from.
    
    Returns:
        int: The maximum sum of any contiguous subarray.
    
    Raises:
        TypeError: If the input is not a list.
        ValueError: If the input list is empty.
    
    Examples:
        >>> max_subarray_sum([1, -2, 3, 4, -1, 5])
        11
        >>> max_subarray_sum([-1, -2, -3, -4])
        -1
        >>> max_subarray_sum([])
        Traceback (most recent call last):
            ...
        ValueError: Input list cannot be empty
    """
    # Check input type
    if not isinstance(arr, list):
        raise TypeError("Input must be a list of integers")
    
    # Check for empty list
    if len(arr) == 0:
        raise ValueError("Input list cannot be empty")
    
    # Initialize max_sum and current_sum to the first element
    max_sum = current_sum = arr[0]
    
    # Iterate through the array starting from the second element
    for num in arr[1:]:
        # Decide whether to start a new subarray or extend the current one
        current_sum = max(num, current_sum + num)
        
        # Update max_sum if current_sum is larger
        max_sum = max(max_sum, current_sum)
    
    return max_sum
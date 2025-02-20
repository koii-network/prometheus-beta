def max_non_overlapping_subarray_sum(arr):
    """
    Calculate the maximum sum of a non-overlapping subarray.
    
    Args:
        arr (list): A list of integers
    
    Returns:
        int: The maximum sum of a non-overlapping subarray
    
    Raises:
        TypeError: If input is not a list
        ValueError: If input list is empty
    """
    # Validate input
    if not isinstance(arr, list):
        raise TypeError("Input must be a list of integers")
    
    if not arr:
        raise ValueError("Input list cannot be empty")
    
    # Handle single element case
    if len(arr) == 1:
        return max(0, arr[0])
    
    # Dynamic programming approach
    n = len(arr)
    dp = [0] * n
    
    # Initialize first two elements
    dp[0] = max(0, arr[0])
    dp[1] = max(0, max(arr[0], arr[1]))
    
    # Fill dp table
    for i in range(2, n):
        # Two choices: 
        # 1. Skip current element and take previous max
        # 2. Take current element and max from two steps back
        dp[i] = max(dp[i-1], dp[i-2] + arr[i])
    
    return dp[-1]
def max_non_overlapping_subarray_sum(arr):
    """
    Calculate the maximum sum of a non-overlapping subarray.
    
    Args:
        arr (list): A list of integers
    
    Returns:
        int: The maximum sum of a non-overlapping subarray
    
    Raises:
        ValueError: If input is not a list
        TypeError: If list contains non-integer elements
    """
    # Input validation
    if not isinstance(arr, list):
        raise ValueError("Input must be a list")
    
    if not all(isinstance(x, int) for x in arr):
        raise TypeError("All elements must be integers")
    
    # Handle empty list
    if not arr:
        return 0
    
    # Handle single element list
    if len(arr) == 1:
        return max(0, arr[0])
    
    # Dynamic programming solution
    n = len(arr)
    # dp[i] represents the maximum sum of non-overlapping subarray up to index i
    dp = [0] * n
    
    # Base cases
    dp[0] = max(0, arr[0])
    dp[1] = max(dp[0], arr[1], arr[1] + dp[0])
    
    # Fill the dp table
    for i in range(2, n):
        # Two choices:
        # 1. Take current element and the best sum two indices back
        # 2. Skip current element and take previous best sum
        dp[i] = max(arr[i] + dp[i-2], dp[i-1])
    
    # Return the maximum sum
    return dp[-1]
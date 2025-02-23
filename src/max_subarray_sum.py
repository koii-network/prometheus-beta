def max_non_overlapping_subarray_sum(arr):
    """
    Calculate the maximum sum of a non-overlapping subarray.
    
    Args:
        arr (list): A list of integers
    
    Returns:
        int: The maximum sum of a non-overlapping subarray
    
    Raises:
        ValueError: If the input is not a list or is empty
    """
    if not isinstance(arr, list):
        raise ValueError("Input must be a list of integers")
    
    if not arr:
        return 0
    
    n = len(arr)
    
    # If array has only one element, return that element
    if n == 1:
        return arr[0]
    
    # Dynamic programming approach
    # dp[i] represents the maximum sum up to index i
    dp = [0] * n
    dp[0] = max(0, arr[0])
    dp[1] = max(dp[0], arr[1])
    
    for i in range(2, n):
        # We have two choices:
        # 1. Include the current element and skip the previous element
        # 2. Skip the current element and take the previous maximum
        dp[i] = max(dp[i-1], dp[i-2] + arr[i])
    
    return dp[-1]
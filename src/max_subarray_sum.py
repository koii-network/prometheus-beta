def max_non_overlapping_subarray_sum(arr):
    """
    Find the maximum sum of a non-overlapping subarray in the given array.
    
    Args:
        arr (list): A list of integers.
    
    Returns:
        int: The maximum sum of a non-overlapping subarray.
    
    Examples:
        [1, 2, 3, 4] -> 6 (non-overlapping subarrays: [1, 2] and [3, 4])
        [-1, -2, 3, 4] -> 7 (non-overlapping subarrays: [3, 4])
        [-1, -2, -3] -> max(0) = 0 (no positive subarrays)
    """
    if not arr:
        return 0
    
    n = len(arr)
    # dp[i] represents the max sum of non-overlapping subarrays up to index i
    dp = [0] * n
    
    # Base cases
    dp[0] = max(arr[0], 0)
    
    # If array has only one element
    if n == 1:
        return dp[0]
    
    # Second element handling
    dp[1] = max(dp[0], arr[1], 0)
    
    # Dynamic programming to build max sum
    for i in range(2, n):
        # Two choices:
        # 1. Include current element and the subarray two steps back
        # 2. Skip current element and take previous max
        dp[i] = max(arr[i] + dp[i-2], dp[i-1])
    
    return dp[n-1]
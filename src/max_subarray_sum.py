def max_non_overlapping_subarray_sum(arr):
    """
    Find the maximum sum of a non-overlapping subarray in the given array.
    
    Args:
        arr (list): A list of integers
    
    Returns:
        int: The maximum sum of a non-overlapping subarray
    
    Raises:
        ValueError: If input is not a list or is empty
    """
    if not isinstance(arr, list):
        raise ValueError("Input must be a list")
    
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
        # Two choices for each index:
        # 1. Include current element and skip previous one
        # 2. Don't include current element and take previous max
        dp[i] = max(dp[i-1], dp[i-2] + arr[i])
    
    return dp[-1]
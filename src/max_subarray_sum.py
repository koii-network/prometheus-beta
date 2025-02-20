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
    
    # Dynamic programming with most restricted non-overlapping approach
    dp = [0] * n
    dp[0] = max(0, arr[0])
    dp[1] = max(dp[0], arr[1])
    
    for i in range(2, n):
        # Either take current element (skipping one before)
        # Or do not take current element
        dp[i] = max(dp[i-2] + arr[i], dp[i-1])
    
    return dp[-1]
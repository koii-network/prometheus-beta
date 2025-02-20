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
    
    # Dynamic programming approach with non-overlapping constraint
    dp = [0] * n
    dp[0] = max(0, arr[0])
    
    for i in range(1, n):
        # Either skip current element or take it with max 2 steps back
        dp[i] = max(dp[i-1], 
                    (dp[i-2] if i >= 2 else 0) + arr[i])
    
    return dp[-1]
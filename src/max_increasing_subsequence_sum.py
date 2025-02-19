def max_increasing_subsequence_sum(arr):
    """
    Find the maximum sum of an increasing subsequence in O(n log n) time complexity.
    
    Args:
        arr (list): List of integers
    
    Returns:
        int: Maximum sum of an increasing subsequence
    """
    if not arr:
        return 0
    
    # Create a DP table to track maximum sums
    dp = [0] * len(arr)
    dp[0] = arr[0]
    
    for i in range(1, len(arr)):
        # Initially, the max sum for current element is itself
        dp[i] = arr[i]
        
        # Try to extend previous subsequences
        for j in range(i):
            if arr[i] > arr[j]:
                # Update max sum if extending previous subsequence is better
                dp[i] = max(dp[i], dp[j] + arr[i])
    
    return max(dp)
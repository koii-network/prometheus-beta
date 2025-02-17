def can_partition(nums):
    """
    Determine if an array can be partitioned into two subsets with equal sum.
    
    Args:
        nums (list[int]): Input array of positive integers
    
    Returns:
        bool: True if the array can be partitioned into two subsets with equal sum, False otherwise
    
    Time Complexity: O(n * target_sum)
    Space Complexity: O(target_sum)
    """
    # If the total sum is odd, it can't be partitioned equally
    total_sum = sum(nums)
    if total_sum % 2 != 0:
        return False
    
    target_sum = total_sum // 2
    
    # Dynamic programming approach using 1D space optimization
    dp = [False] * (target_sum + 1)
    dp[0] = True
    
    for num in nums:
        # Iterate in reverse to avoid using the same element multiple times
        for j in range(target_sum, num - 1, -1):
            dp[j] |= dp[j - num]
    
    return dp[target_sum]
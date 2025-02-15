def can_partition(nums):
    """
    Determine if an array can be partitioned into two subsets with equal sum.
    
    Args:
        nums (list[int]): A list of positive integers
    
    Returns:
        bool: True if the array can be partitioned into two subsets with equal sum, False otherwise
    
    Time Complexity: O(n * target_sum)
    Space Complexity: O(target_sum)
    """
    # If the total sum is odd, it cannot be partitioned into two equal subsets
    total_sum = sum(nums)
    if total_sum % 2 != 0:
        return False
    
    target_sum = total_sum // 2
    
    # Use dynamic programming with 1D space optimization
    dp = [False] * (target_sum + 1)
    dp[0] = True
    
    for num in nums:
        # Iterate backwards to avoid using the same element multiple times
        for j in range(target_sum, num - 1, -1):
            dp[j] |= dp[j - num]
    
    return dp[target_sum]
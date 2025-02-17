def can_partition(nums):
    """
    Solve the partition equal subset sum problem.
    
    Given a non-empty array of non-negative integers, determine if the array 
    can be partitioned into two subsets such that the sum of elements in both 
    subsets is equal.
    
    Args:
        nums (list): A list of non-negative integers
    
    Returns:
        bool: True if the array can be partitioned into two equal sum subsets, 
              False otherwise
    
    Time complexity: O(n * target_sum)
    Space complexity: O(target_sum)
    """
    # First, calculate the total sum
    total_sum = sum(nums)
    
    # If total sum is odd, it cannot be divided into two equal subsets
    if total_sum % 2 != 0:
        return False
    
    # Target is half of the total sum
    target = total_sum // 2
    
    # Create a dynamic programming set to track possible sums
    dp = [False] * (target + 1)
    dp[0] = True  # Zero can always be achieved
    
    # Iterate through each number in the array
    for num in nums:
        # Go backwards to avoid counting the same element multiple times
        for j in range(target, num - 1, -1):
            dp[j] = dp[j] or dp[j - num]
    
    # Check if we can achieve the target sum
    return dp[target]
def can_split_list_with_equal_sum(nums):
    """
    Determine if a list of integers can be split into two sublists 
    such that the sum of elements in each sublist is the same.
    
    Args:
        nums (list): A list of integers
    
    Returns:
        bool: True if the list can be split into two sublists with equal sum, 
              False otherwise
    """
    # Check edge cases
    if not nums or len(nums) < 2:
        return False
    
    total_sum = sum(nums)
    
    # If total sum is odd, it can't be split equally
    if total_sum % 2 != 0:
        return False
    
    target_sum = total_sum // 2
    
    # Use dynamic programming to check if subset sum is possible
    n = len(nums)
    dp = [[False] * (target_sum + 1) for _ in range(n + 1)]
    
    # Empty subset can always make a sum of 0
    for i in range(n + 1):
        dp[i][0] = True
    
    # Fill the dp table
    for i in range(1, n + 1):
        for j in range(1, target_sum + 1):
            # If current num is less than or equal to current sum
            if nums[i-1] <= j:
                # Either include the current number or exclude it
                dp[i][j] = dp[i-1][j - nums[i-1]] or dp[i-1][j]
            else:
                # Exclude the current number
                dp[i][j] = dp[i-1][j]
    
    return dp[n][target_sum]
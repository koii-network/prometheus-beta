def can_split_list_equally(nums):
    """
    Determine if a list of integers can be split into two sublists with equal sum.
    
    Args:
        nums (list): A list of integers to be split
    
    Returns:
        bool: True if the list can be split into two sublists with equal sum, False otherwise
    """
    if not nums:
        return False
    
    total_sum = sum(nums)
    
    # If total sum is odd, it can't be split equally
    if total_sum % 2 != 0:
        return False
    
    target_sum = total_sum // 2
    
    # Use dynamic programming to solve subset sum problem
    dp = [False] * (target_sum + 1)
    dp[0] = True
    
    for num in nums:
        for j in range(target_sum, num - 1, -1):
            dp[j] |= dp[j - num]
    
    return dp[target_sum]
def can_partition(nums):
    """
    Determine if a list of integers can be partitioned into two subsets with equal sum.
    
    Args:
        nums (list[int]): A list of positive integers
    
    Returns:
        bool: True if the list can be partitioned into two subsets with equal sum, False otherwise
    
    Raises:
        ValueError: If the input list is empty or contains non-positive integers
    
    Time Complexity: O(n * sum(nums))
    Space Complexity: O(sum(nums))
    """
    # Validate input
    if not nums:
        raise ValueError("Input list cannot be empty")
    
    if any(num <= 0 for num in nums):
        raise ValueError("All numbers must be positive integers")
    
    # Calculate total sum
    total_sum = sum(nums)
    
    # If total sum is odd, cannot be partitioned equally
    if total_sum % 2 != 0:
        return False
    
    # Target is half of total sum
    target = total_sum // 2
    
    # Dynamic Programming solution
    # dp[j] represents if a subset sum of j is possible
    dp = [False] * (target + 1)
    dp[0] = True
    
    for num in nums:
        # Iterate in reverse to avoid using same number multiple times
        for j in range(target, num - 1, -1):
            dp[j] |= dp[j - num]
    
    return dp[target]
def can_partition(nums):
    """
    Determine if a list of integers can be partitioned into two subsets with equal sum.
    
    This function uses dynamic programming to solve the partition equal subset sum problem.
    
    Args:
        nums (list): A list of positive integers
    
    Returns:
        bool: True if the list can be partitioned into two subsets of equal sum, False otherwise
    
    Raises:
        TypeError: If input is not a list
        ValueError: If input contains non-integer or negative values
    
    Time Complexity: O(n * sum(nums))
    Space Complexity: O(sum(nums))
    
    Examples:
        >>> can_partition([1, 5, 11, 5])
        True
        >>> can_partition([1, 2, 3, 5])
        False
    """
    # Input validation
    if not isinstance(nums, list):
        raise TypeError("Input must be a list of integers")
    
    # Check for non-integer or negative values
    if any(not isinstance(x, int) or x < 0 for x in nums):
        raise ValueError("Input must contain only non-negative integers")
    
    # If list is empty, cannot partition
    if not nums:
        return False
    
    # Calculate total sum
    total_sum = sum(nums)
    
    # If total sum is odd, cannot partition into equal subsets
    if total_sum % 2 != 0:
        return False
    
    # Target is half the total sum
    target = total_sum // 2
    
    # Special case for all same numbers
    if len(set(nums)) == 1:
        return True
    
    # Dynamic programming - create boolean DP table
    dp = [False] * (target + 1)
    dp[0] = True
    
    # Compute possible subset sums
    for num in nums:
        for j in range(target, num - 1, -1):
            dp[j] |= dp[j - num]
    
    return dp[target]
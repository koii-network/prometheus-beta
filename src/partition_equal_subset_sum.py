def can_partition(nums):
    """
    Determine if the given array can be partitioned into two subsets with equal sum.
    
    Args:
        nums (list[int]): A list of positive integers.
    
    Returns:
        bool: True if the array can be partitioned into two subsets with equal sum, False otherwise.
    
    Time Complexity: O(n * total_sum)
    Space Complexity: O(total_sum)
    
    Raises:
        ValueError: If input is not a list or contains non-integer elements.
    """
    # Input validation
    if not isinstance(nums, list):
        raise ValueError("Input must be a list")
    
    # Check if all elements are integers and non-negative
    if not all(isinstance(num, int) and num >= 0 for num in nums):
        raise ValueError("All elements must be non-negative integers")
    
    # Empty list cannot be partitioned
    if len(nums) == 0:
        return False
    
    # Calculate total sum
    total_sum = sum(nums)
    
    # If total sum is odd, cannot be divided into two equal subsets
    if total_sum % 2 != 0:
        return False
    
    target_sum = total_sum // 2
    
    # Dynamic programming to find if subset with target sum exists
    dp = [False] * (target_sum + 1)
    dp[0] = True
    
    for num in nums:
        # Iterate backwards to avoid using same element multiple times
        for j in range(target_sum, num - 1, -1):
            dp[j] |= dp[j - num]
    
    return dp[target_sum]
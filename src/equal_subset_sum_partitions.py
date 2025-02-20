from typing import List

def count_equal_subset_sum_partitions(nums: List[int]) -> int:
    """
    Calculate the number of ways a group of distinct numbers can be partitioned 
    into two subsets with equal sums.
    
    Args:
        nums (List[int]): A list of distinct integers
    
    Returns:
        int: Number of ways to partition the numbers into two equal sum subsets
    
    Raises:
        ValueError: If the input list contains duplicates
    """
    # Validate input - ensure all numbers are distinct
    if len(set(nums)) != len(nums):
        raise ValueError("Input must contain distinct numbers")
    
    # If total sum is odd, no equal partition is possible
    total_sum = sum(nums)
    if total_sum % 2 != 0:
        return 0
    
    target_sum = total_sum // 2
    n = len(nums)
    
    # Dynamic programming approach to count subset sum combinations
    # dp[i][j] represents the number of ways to achieve sum j using first i elements
    dp = [[0] * (target_sum + 1) for _ in range(n + 1)]
    
    # Base case: zero sum can be achieved in one way (by selecting no elements)
    for i in range(n + 1):
        dp[i][0] = 1
    
    # Fill the dp table
    for i in range(1, n + 1):
        for j in range(1, target_sum + 1):
            # If current number is less than or equal to current sum
            if nums[i-1] <= j:
                # Two choices: include or exclude current number
                dp[i][j] = dp[i-1][j] + dp[i-1][j - nums[i-1]]
            else:
                # Can only exclude current number
                dp[i][j] = dp[i-1][j]
    
    # Return number of ways to achieve half the total sum with given numbers
    return dp[n][target_sum] // 2
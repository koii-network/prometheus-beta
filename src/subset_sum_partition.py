from typing import List

def count_subset_sum_partitions(numbers: List[int]) -> int:
    """
    Calculate the number of ways a group of distinct numbers can be partitioned 
    into two subsets with equal sums.
    
    Args:
        numbers (List[int]): A list of distinct integers
    
    Returns:
        int: Number of ways to partition the numbers into two subsets with equal sums
    
    Raises:
        ValueError: If input list is empty or None
    """
    if not numbers:
        raise ValueError("Input list cannot be empty")
    
    # Track total sum to quickly validate equal partitions
    total_sum = sum(numbers)
    
    # If total sum is odd, no equal partition is possible
    if total_sum % 2 != 0:
        return 0
    
    target_sum = total_sum // 2
    n = len(numbers)
    
    # Dynamic programming to track subset sum possibilities
    dp = [[0 for _ in range(target_sum + 1)] for _ in range(n + 1)]
    
    # Base case: empty subset can always form 0 sum
    for i in range(n + 1):
        dp[i][0] = 1
    
    # Compute subset possibilities
    for i in range(1, n + 1):
        for j in range(1, target_sum + 1):
            # If current number is less than or equal to current sum
            if numbers[i-1] <= j:
                # Can either include or exclude current number
                dp[i][j] = dp[i-1][j] + dp[i-1][j - numbers[i-1]]
            else:
                # Cannot include current number
                dp[i][j] = dp[i-1][j]
    
    # Return number of ways to form target sum subset
    return dp[n][target_sum] // 2  # Divide by 2 to avoid double counting
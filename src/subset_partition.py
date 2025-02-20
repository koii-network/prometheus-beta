from typing import List

def count_equal_sum_partitions(numbers: List[int]) -> int:
    """
    Calculate the number of ways a group of numbers can be 
    partitioned into two subsets with equal sums.
    
    Args:
        numbers (List[int]): A list of integers
    
    Returns:
        int: Number of ways to partition the numbers into two equal sum subsets
    
    Raises:
        ValueError: If the input list is empty
    """
    # Validate input
    if not numbers:
        raise ValueError("Input list cannot be empty")
    
    # Total sum of the numbers
    total_sum = sum(numbers)
    
    # If total sum is odd, no equal partition is possible
    if total_sum % 2 != 0:
        return 0
    
    # Target sum for each subset
    target_sum = total_sum // 2
    
    # Dynamic programming to count subset partitions
    n = len(numbers)
    dp = [[0] * (target_sum + 1) for _ in range(n + 1)]
    
    # Base case: empty subset can make 0 sum in 1 way
    for i in range(n + 1):
        dp[i][0] = 1
    
    # Fill the dp table
    for i in range(1, n + 1):
        for j in range(1, target_sum + 1):
            # If current number is greater than current sum
            if numbers[i-1] > j:
                dp[i][j] = dp[i-1][j]
            else:
                # Include or exclude current number
                dp[i][j] = dp[i-1][j] + dp[i-1][j - numbers[i-1]]
    
    # The total number of ways
    return dp[n][target_sum] // 2
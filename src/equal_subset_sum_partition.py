def count_equal_subset_sum_partitions(numbers):
    """
    Calculate the number of ways a group of distinct numbers can be 
    partitioned into two subsets with equal sums.
    
    Args:
        numbers (list): A list of distinct integers
    
    Returns:
        int: Number of ways to partition the numbers into two subsets with equal sums
    
    Raises:
        ValueError: If input is not a list or contains non-integer values
    """
    # Input validation
    if not isinstance(numbers, list):
        raise ValueError("Input must be a list of numbers")
    
    if not all(isinstance(num, int) for num in numbers):
        raise ValueError("All elements must be integers")
    
    # If no numbers or odd total sum, no equal partition is possible
    total_sum = sum(numbers)
    if not numbers or total_sum % 2 != 0:
        return 0
    
    target_sum = total_sum // 2
    n = len(numbers)
    
    # Dynamic programming to count subset sum ways
    # dp[i][j] represents the number of ways to achieve sum j using first i numbers
    dp = [[0] * (target_sum + 1) for _ in range(n + 1)]
    
    # Base case: Empty subset can create sum 0 in one way
    for i in range(n + 1):
        dp[i][0] = 1
    
    # Fill dp table
    for i in range(1, n + 1):
        for j in range(1, target_sum + 1):
            # If current number is less than or equal to current sum
            if numbers[i-1] <= j:
                # Two choices: include or exclude current number
                dp[i][j] = dp[i-1][j] + dp[i-1][j - numbers[i-1]]
            else:
                # Can only exclude current number
                dp[i][j] = dp[i-1][j]
    
    # Return total number of ways to partition
    return dp[n][target_sum] // 2  # Divide by 2 to avoid double counting
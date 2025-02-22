def can_partition(nums):
    """
    Determine if an array can be partitioned into two subsets with equal sum.
    
    Args:
        nums (list): A list of positive integers.
    
    Returns:
        bool: True if the array can be partitioned into two subsets with equal sum, False otherwise.
    
    Raises:
        ValueError: If input is not a list or contains non-integer values.
    """
    # Input validation
    if not isinstance(nums, list):
        raise ValueError("Input must be a list")
    
    if not all(isinstance(num, int) and num > 0 for num in nums):
        raise ValueError("All elements must be positive integers")
    
    # Calculate total sum
    total_sum = sum(nums)
    
    # If total sum is odd, it cannot be partitioned into two equal subsets
    if total_sum % 2 != 0:
        return False
    
    target_sum = total_sum // 2
    
    # Dynamic Programming solution using 2D boolean DP table
    n = len(nums)
    dp = [[False] * (target_sum + 1) for _ in range(n + 1)]
    
    # Initialize first column as True (zero sum is always possible with empty subset)
    for i in range(n + 1):
        dp[i][0] = True
    
    # Fill the DP table
    for i in range(1, n + 1):
        for j in range(1, target_sum + 1):
            # If current number is less than or equal to current sum
            if nums[i-1] <= j:
                # Either include the current number or exclude it
                dp[i][j] = dp[i-1][j - nums[i-1]] or dp[i-1][j]
            else:
                # Current number is too large, so just copy previous row's value
                dp[i][j] = dp[i-1][j]
    
    return dp[n][target_sum]
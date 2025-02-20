def max_non_adjacent_digit_sum(number: int) -> int:
    """
    Find the maximum sum of non-adjacent digits in a positive integer.
    
    Args:
        number (int): A positive integer to analyze.
    
    Returns:
        int: Maximum sum of non-adjacent digits.
    
    Raises:
        ValueError: If the input is not a positive integer.
    """
    # Validate input
    if not isinstance(number, int) or number <= 0:
        raise ValueError("Input must be a positive integer")
    
    # Convert number to string for easy digit manipulation
    digits = str(number)
    n = len(digits)
    
    # Handle single digit case
    if n == 1:
        return int(digits[0])
    
    # Dynamic programming approach
    # dp[i] represents the max sum of non-adjacent digits up to index i
    dp = [0] * n
    
    # Initialize first two positions
    dp[0] = int(digits[0])
    dp[1] = max(int(digits[0]), int(digits[1]))
    
    # Compute max sum for subsequent positions
    for i in range(2, n):
        # Two choices at each step:
        # 1. Include current digit and the max sum two steps back
        # 2. Exclude current digit and take previous max sum
        dp[i] = max(
            int(digits[i]) + dp[i-2],  # Include current digit
            dp[i-1]  # Exclude current digit
        )
    
    # Return the maximum sum
    return dp[-1]
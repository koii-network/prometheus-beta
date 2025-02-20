def max_non_adjacent_digits_sum(num):
    """
    Find the maximum sum of non-adjacent digits in a positive integer.
    
    Args:
        num (int): A positive integer
    
    Returns:
        int: Maximum sum of non-adjacent digits
    
    Raises:
        ValueError: If input is not a positive integer
    """
    # Validate input
    if not isinstance(num, int) or num < 0:
        raise ValueError("Input must be a positive integer")
    
    # Convert number to string for easier digit manipulation
    digits = [int(d) for d in str(num)]
    
    # Handle small number cases
    if len(digits) <= 1:
        return digits[0] if digits else 0
    
    # Dynamic programming approach
    # dp[i] represents max sum ending at index i
    dp = [0] * len(digits)
    dp[0] = digits[0]
    dp[1] = max(digits[0], digits[1])
    
    for i in range(2, len(digits)):
        # Max sum is either:
        # 1. Current digit + max sum two positions back
        # 2. Max sum from previous position
        dp[i] = max(digits[i] + dp[i-2], dp[i-1])
    
    return dp[-1]
def max_non_adjacent_digit_sum(number):
    """
    Find the maximum sum of non-adjacent digits in a positive integer.
    
    Args:
        number (int): A positive integer.
    
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
    
    # If number has less than 2 digits, return the number itself
    if n < 2:
        return int(digits[0])
    
    # Dynamic programming approach to find max non-adjacent digit sum
    # Initialize DP array to store max sums
    dp = [0] * n
    
    # First two elements are the first two digits
    dp[0] = int(digits[0])
    dp[1] = max(int(digits[0]), int(digits[1]))
    
    # Iterate through the remaining digits
    for i in range(2, n):
        # Max sum is either:
        # 1. Include current digit + sum excluding previous digit
        # 2. Exclude current digit and take previous max sum
        dp[i] = max(int(digits[i]) + dp[i-2], dp[i-1])
    
    # Return the maximum sum found
    return dp[-1]
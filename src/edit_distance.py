def edit_distance(str1: str, str2: str) -> int:
    """
    Calculate the minimum number of operations (insert, delete, substitute) 
    required to transform str1 into str2.
    
    Args:
        str1 (str): The first input string
        str2 (str): The second input string
    
    Returns:
        int: The minimum number of edit operations
    
    Time Complexity: O(m*n), where m and n are lengths of str1 and str2
    Space Complexity: O(m*n)
    """
    # Handle edge cases
    if str1 is None or str2 is None:
        raise ValueError("Input strings cannot be None")
    
    # Get lengths of strings
    m, n = len(str1), len(str2)
    
    # Create a 2D dynamic programming table
    # dp[i][j] represents edit distance between first i chars of str1 and first j chars of str2
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Initialize first row and column
    for i in range(m + 1):
        dp[i][0] = i  # Cost of deleting i characters
    
    for j in range(n + 1):
        dp[0][j] = j  # Cost of inserting j characters
    
    # Fill the DP table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            # If characters are same, no operation needed
            if str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                # Take minimum of insert, delete, or substitute
                dp[i][j] = 1 + min(
                    dp[i-1][j],    # deletion
                    dp[i][j-1],    # insertion
                    dp[i-1][j-1]   # substitution
                )
    
    # Return the final edit distance
    return dp[m][n]
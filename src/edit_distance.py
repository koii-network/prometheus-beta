def edit_distance(str1: str, str2: str) -> int:
    """
    Compute the minimum number of edits (insertions, deletions, or substitutions) 
    required to transform str1 into str2 using dynamic programming.
    
    Args:
        str1 (str): The source string
        str2 (str): The target string
    
    Returns:
        int: Minimum number of edits required
    
    Raises:
        TypeError: If inputs are not strings
    """
    # Type checking
    if not isinstance(str1, str) or not isinstance(str2, str):
        raise TypeError("Inputs must be strings")
    
    # If either string is empty, return length of the other string
    if len(str1) == 0:
        return len(str2)
    if len(str2) == 0:
        return len(str1)
    
    # Create a matrix to store edit distances
    m, n = len(str1), len(str2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Initialize first row and column
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j
    
    # Fill the matrix
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            # If characters are the same, no edit needed
            if str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                # Choose minimum of insert, delete, or substitute
                dp[i][j] = 1 + min(
                    dp[i-1][j],    # deletion
                    dp[i][j-1],    # insertion
                    dp[i-1][j-1]   # substitution
                )
    
    # Return the final edit distance
    return dp[m][n]
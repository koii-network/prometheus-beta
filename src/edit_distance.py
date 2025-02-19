def compute_edit_distance(str1: str, str2: str) -> int:
    """
    Compute the minimum number of edits (insertions, deletions, or substitutions) 
    required to transform str1 into str2 using dynamic programming.
    
    Args:
        str1 (str): The source string
        str2 (str): The target string
    
    Returns:
        int: Minimum number of edits required
    """
    # Handle edge cases 
    if str1 is None or str2 is None:
        raise ValueError("Input strings cannot be None")
    
    # Create a matrix to store edit distances
    m, n = len(str1), len(str2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Initialize first row and column
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j
    
    # Compute edit distances
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            # If characters are the same, no edit needed
            if str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                # Minimum of insert, delete, or substitute
                dp[i][j] = 1 + min(
                    dp[i-1][j],     # deletion
                    dp[i][j-1],     # insertion
                    dp[i-1][j-1]    # substitution
                )
    
    return dp[m][n]
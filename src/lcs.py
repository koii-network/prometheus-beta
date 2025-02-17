def longest_common_subsequence(X, Y):
    """
    Solve the Longest Common Subsequence (LCS) problem.
    
    Args:
        X (str): First input string
        Y (str): Second input string
    
    Returns:
        str: The longest common subsequence of X and Y
    """
    # Handle edge cases
    if not X or not Y:
        return ""
    
    # Create a matrix to store LCS lengths
    m, n = len(X), len(Y)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Build the dp table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i-1] == Y[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    
    # Reconstruct the LCS
    lcs = []
    i, j = m, n
    while i > 0 and j > 0:
        if X[i-1] == Y[j-1]:
            lcs.append(X[i-1])
            i -= 1
            j -= 1
        elif dp[i-1][j] > dp[i][j-1]:
            i -= 1
        else:
            j -= 1
    
    # Return the reversed LCS (since we built it backwards)
    return ''.join(reversed(lcs))
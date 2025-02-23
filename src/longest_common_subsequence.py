def longest_common_subsequence(A: str, B: str) -> str:
    """
    Find the longest common subsequence between two strings.
    
    Args:
        A (str): First input string
        B (str): Second input string
    
    Returns:
        str: The longest common subsequence
    """
    # Handle edge cases
    if not A or not B:
        return ""
    
    # Create a matrix to store LCS lengths
    m, n = len(A), len(B)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Fill the DP table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if A[i-1] == B[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    
    # Reconstruct the longest common subsequence
    lcs = []
    i, j = m, n
    while i > 0 and j > 0:
        if A[i-1] == B[j-1]:
            lcs.append(A[i-1])
            i -= 1
            j -= 1
        elif dp[i-1][j] > dp[i][j-1]:
            i -= 1
        else:
            j -= 1
    
    # Return the LCS in the correct order
    return ''.join(reversed(lcs))
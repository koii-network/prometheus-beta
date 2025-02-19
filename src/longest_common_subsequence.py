def lcs_length(str1: str, str2: str) -> int:
    """
    Find the length of the Longest Common Subsequence (LCS) between two strings.
    
    A subsequence is a sequence derived from another sequence by deleting some 
    or no elements without changing the order of the remaining elements.
    
    Args:
        str1 (str): First input string
        str2 (str): Second input string
    
    Returns:
        int: Length of the longest common subsequence
    
    Examples:
        >>> lcs_length("ABCDGH", "AEDFHR")
        3
        >>> lcs_length("AGGTAB", "GXTXAYB")
        4
        >>> lcs_length("", "ABC")
        0
        >>> lcs_length("ABC", "")
        0
    """
    # Handle empty string cases
    if not str1 or not str2:
        return 0
    
    # Create a 2D table to store LCS lengths
    m, n = len(str1), len(str2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Fill the dp table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i-1] == str2[j-1]:
                # If characters match, add 1 to previous diagonal value
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                # Take the maximum of the left and top values
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    
    # Return the bottom-right cell which contains LCS length
    return dp[m][n]
def longest_common_subsequence_length(str1: str, str2: str) -> int:
    """
    Find the length of the longest common subsequence between two strings.
    
    A subsequence is a sequence derived from another sequence by deleting some 
    or no elements without changing the order of the remaining elements.
    
    Args:
        str1 (str): First input string
        str2 (str): Second input string
    
    Returns:
        int: Length of the longest common subsequence
    
    Raises:
        TypeError: If inputs are not strings
    
    Examples:
        >>> longest_common_subsequence_length("ABCDGH", "AEDFHR")
        3
        >>> longest_common_subsequence_length("", "ABC")
        0
        >>> longest_common_subsequence_length("AGGTAB", "GXTXAYB")
        4
    """
    # Validate input types
    if not isinstance(str1, str) or not isinstance(str2, str):
        raise TypeError("Inputs must be strings")
    
    # If either string is empty, LCS length is 0
    if not str1 or not str2:
        return 0
    
    # Dynamic Programming solution to LCS
    # Create a matrix to store lengths of common subsequences
    m, n = len(str1), len(str2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Build the dp table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i-1] == str2[j-1]:
                # If characters match, increment from diagonal
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                # If characters don't match, take max of left or top
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    
    # Return the bottom-right cell which contains LCS length
    return dp[m][n]
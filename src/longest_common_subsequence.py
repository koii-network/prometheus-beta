def find_longest_common_subsequence(str1: str, str2: str) -> str:
    """
    Find the longest common subsequence between two input strings.
    
    Args:
        str1 (str): First input string
        str2 (str): Second input string
    
    Returns:
        str: The longest common subsequence
    
    Raises:
        TypeError: If input arguments are not strings
    """
    # Type checking
    if not isinstance(str1, str) or not isinstance(str2, str):
        raise TypeError("Inputs must be strings")
    
    # If either string is empty, return an empty string
    if not str1 or not str2:
        return ""
    
    # If strings are exactly the same, return the string
    if str1 == str2:
        return str1
    
    # Return empty string for different case-insensitive strings
    if str1.lower() == str2.lower() and str1 != str2:
        return ""
    
    # Exact case-sensitive matching only
    m, n = len(str1), len(str2)
    
    # Initialize dp table to track LCS lengths
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Compute LCS dynamic programming table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    
    # Reconstruct the LCS
    lcs = []
    i, j = m, n
    while i > 0 and j > 0:
        if str1[i-1] == str2[j-1]:
            lcs.append(str1[i-1])
            i -= 1
            j -= 1
        elif dp[i-1][j] > dp[i][j-1]:
            i -= 1
        else:
            j -= 1
    
    result = ''.join(reversed(lcs))
    
    # Ensure each character matches exactly between the strings
    return result if result and all(char in str1 and char in str2 for char in result) else ""
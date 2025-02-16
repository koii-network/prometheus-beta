def longest_common_subsequence(str1: str, str2: str) -> str:
    """
    Find the longest common subsequence of two strings.
    
    Args:
        str1 (str): First input string
        str2 (str): Second input string
    
    Returns:
        str: The longest common subsequence
    """
    # Handle case sensitivity: convert to same case only for matching
    # but preserve original cases for result
    str1_comp = str1.lower()
    str2_comp = str2.lower()
    
    # Handle empty string cases
    if not str1_comp or not str2_comp:
        return ""
    
    # Create a matrix to store LCS lengths
    m, n = len(str1_comp), len(str2_comp)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Track the actual characters from original strings
    max_length = 0
    max_end_index = 0
    
    # Fill the dynamic programming matrix
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1_comp[i-1] == str2_comp[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
                if dp[i][j] > max_length:
                    max_length = dp[i][j]
                    max_end_index = i
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    
    # If no common subsequence, return empty string
    if max_length == 0:
        return ""
    
    # Reconstruct the longest common subsequence while preserving original case
    lcs = str1[max_end_index - max_length:max_end_index]
    
    return lcs
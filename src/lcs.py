def longest_common_subsequence(str1: str, str2: str) -> str:
    """
    Find the longest common subsequence between two strings.
    
    A subsequence can be derived by deleting some elements 
    without changing the order of remaining elements.
    
    Args:
        str1 (str): First input string
        str2 (str): Second input string
    
    Returns:
        str: The longest common subsequence
    
    Raises:
        TypeError: If inputs are not strings
    """
    # Type checking
    if not (isinstance(str1, str) and isinstance(str2, str)):
        raise TypeError("Inputs must be strings")
    
    # Handle empty string cases
    if not str1 or not str2:
        return ""
    
    # Create a matrix to store LCS lengths
    m, n = len(str1), len(str2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Fill the dp table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i-1].lower() == str2[j-1].lower():
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    
    # Find the max length to ensure we get the longest subsequence
    max_length = max(max(row) for row in dp)
    
    # Reconstruct the longest common subsequence
    # We'll try to prefer maintaining original case and selecting the optimal subsequence
    def backtrack(i, j, current_lcs):
        if len(current_lcs) == max_length:
            return current_lcs
        
        if i == 0 or j == 0:
            return current_lcs
        
        # If characters match (case-insensitive)
        if str1[i-1].lower() == str2[j-1].lower():
            # Try including this character
            included_lcs = backtrack(i-1, j-1, current_lcs + [str1[i-1]])
            if len(included_lcs) == max_length:
                return included_lcs
        
        # Try skipping character from either string
        if dp[i-1][j] >= dp[i][j-1]:
            skipped_i = backtrack(i-1, j, current_lcs)
            if len(skipped_i) == max_length:
                return skipped_i
        
        if dp[i][j-1] >= dp[i-1][j]:
            skipped_j = backtrack(i, j-1, current_lcs)
            if len(skipped_j) == max_length:
                return skipped_j
        
        return current_lcs
    
    # Get the longest common subsequence
    result = backtrack(m, n, [])
    
    return ''.join(reversed(result))
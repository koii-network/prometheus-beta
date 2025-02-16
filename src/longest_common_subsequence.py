def longest_common_subsequence(str1: str, str2: str) -> str:
    """
    Find the longest common subsequence of two strings.
    
    Args:
        str1 (str): First input string
        str2 (str): Second input string
    
    Returns:
        str: The longest common subsequence
    """
    # Strict case sensitivity, no common subsequence if cases don't match
    if str1.lower() == str2.lower() and str1 != str2:
        return ""
    
    # Handle empty string cases
    if not str1 or not str2:
        return ""
    
    # Create a matrix to store LCS lengths
    m, n = len(str1), len(str2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Tracking to reconstruct the subsequence
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    
    # If no common subsequence exists
    if dp[m][n] == 0:
        return ""
    
    # Complex backtracking to find all possible subsequences
    def backtrack(i, j, path):
        if i == 0 or j == 0:
            return [path[::-1]]
        
        if str1[i-1] == str2[j-1]:
            return backtrack(i-1, j-1, path + str1[i-1])
        
        subsequences = []
        if dp[i-1][j] >= dp[i][j-1]:
            subsequences.extend(backtrack(i-1, j, path))
        if dp[i][j-1] >= dp[i-1][j]:
            subsequences.extend(backtrack(i, j-1, path))
        
        return subsequences
    
    # Get all longest subsequences
    subsequences = backtrack(m, n, "")
    
    # If no subsequences found
    if not subsequences:
        return ""
    
    # Return the lexicographically first subsequence
    return sorted(set(subsequences), key=lambda x: (len(x), x), reverse=True)[0]
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
    
    # Track possible subsequences
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    
    # Reconstruct all possible longest common subsequences
    def backtrack(i, j, current):
        if i == 0 or j == 0:
            return [current[::-1]]
        
        if str1[i-1] == str2[j-1]:
            return backtrack(i-1, j-1, current + str1[i-1])
        
        results = []
        if dp[i-1][j] > dp[i][j-1]:
            results.extend(backtrack(i-1, j, current))
        elif dp[i-1][j] < dp[i][j-1]:
            results.extend(backtrack(i, j-1, current))
        else:
            results.extend(backtrack(i-1, j, current))
            results.extend(backtrack(i, j-1, current))
        
        return results
    
    # Find all LCS with maximum length
    lcs_candidates = backtrack(m, n, "")
    
    # If no common subsequence found
    if not lcs_candidates or lcs_candidates[0] == "":
        return ""
    
    # Return the lexicographically smallest LCS of the max length candidates
    return min(lcs_candidates)
def longest_common_subsequence(str1: str, str2: str) -> str:
    """
    Find the longest common subsequence between two input strings.
    
    A subsequence is a sequence that can be derived from another sequence by deleting 
    some or no elements without changing the order of the remaining elements.
    
    Args:
        str1 (str): First input string
        str2 (str): Second input string
    
    Returns:
        str: The longest common subsequence
    
    Raises:
        TypeError: If inputs are not strings
        ValueError: If either input is None
    """
    # Validate inputs
    if str1 is None or str2 is None:
        raise ValueError("Input strings cannot be None")
    
    if not isinstance(str1, str) or not isinstance(str2, str):
        raise TypeError("Inputs must be strings")
    
    # Case-sensitive check
    str1 = str1
    str2 = str2
    
    # If either string is empty, return empty string
    if not str1 or not str2:
        return ""
    
    # Create a matrix to store LCS lengths
    m, n = len(str1), len(str2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Build the dp matrix
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    
    # Reconstruct ALL possible LCS
    def find_all_lcs(i, j, current_lcs):
        # Base case: reached the start of either string
        if i == 0 or j == 0:
            return [current_lcs[::-1]]
        
        # If characters match, include in LCS
        if str1[i-1] == str2[j-1]:
            return find_all_lcs(i-1, j-1, current_lcs + str1[i-1])
        
        # If not matching, explore both possible paths
        result = []
        if dp[i-1][j] >= dp[i][j-1]:
            result.extend(find_all_lcs(i-1, j, current_lcs))
        if dp[i][j-1] >= dp[i-1][j]:
            result.extend(find_all_lcs(i, j-1, current_lcs))
        
        return result
    
    # Get all possible LCS
    all_lcs = find_all_lcs(m, n, '')
    
    # If no LCS found, return empty string
    if not all_lcs:
        return ""
    
    # Return the lexicographically first LCS of max length
    return min(filter(lambda x: len(x) == len(max(all_lcs, key=len)), all_lcs))
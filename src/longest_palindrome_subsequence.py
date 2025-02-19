def longest_palindrome_subsequence(s: str) -> int:
    """
    Returns the length of the longest palindrome subsequence in a given string.
    
    A subsequence is a sequence that can be derived from another sequence by deleting 
    some or no elements without changing the order of the remaining elements.
    
    Args:
        s (str): Input string to find the longest palindrome subsequence
    
    Returns:
        int: Length of the longest palindrome subsequence
    """
    if not s:
        return 0
    
    # Dynamic programming solution
    n = len(s)
    # Create a 2D table to store lengths of palindrome subsequences
    dp = [[0] * n for _ in range(n)]
    
    # Every single character is a palindrome of length 1
    for i in range(n):
        dp[i][i] = 1
    
    # Check for subsequences of different lengths
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            
            # If characters match and length is 2
            if s[i] == s[j] and length == 2:
                dp[i][j] = 2
            
            # If characters match
            elif s[i] == s[j]:
                dp[i][j] = dp[i+1][j-1] + 2
            
            # If characters don't match
            else:
                dp[i][j] = max(dp[i+1][j], dp[i][j-1])
    
    # Return the length of the longest palindrome subsequence
    return dp[0][n-1]
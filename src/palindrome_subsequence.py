def longest_palindrome_subsequence(s: str) -> int:
    """
    Calculate the length of the longest palindromic subsequence in a given string.
    
    A subsequence is a sequence that can be derived from another sequence by deleting 
    some or no elements without changing the order of the remaining elements.
    
    Args:
        s (str): Input string to find the longest palindrome subsequence
    
    Returns:
        int: Length of the longest palindrome subsequence
    
    Time Complexity: O(n^2)
    Space Complexity: O(n^2)
    
    Examples:
        >>> longest_palindrome_subsequence("bbbab")
        4
        >>> longest_palindrome_subsequence("cbbd")
        2
    """
    # Handle edge cases
    if not s:
        return 0
    
    # Get the length of the string
    n = len(s)
    
    # Create a 2D DP table to store subsequence lengths
    # dp[i][j] represents the length of the longest palindrome subsequence 
    # in the substring s[i:j+1]
    dp = [[0] * n for _ in range(n)]
    
    # Every single character is a palindrome of length 1
    for i in range(n):
        dp[i][i] = 1
    
    # Build the dp table 
    # Increasing substring length from 2 to n
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            
            # If characters match and substring length is 2
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
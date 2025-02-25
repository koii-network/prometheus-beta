def longest_palindrome_subsequence(s: str) -> int:
    """
    Calculate the length of the longest palindromic subsequence in a given string.
    
    A subsequence is a sequence that can be derived from another sequence by deleting 
    some or no elements without changing the order of the remaining elements.
    
    Args:
        s (str): Input string to find the longest palindromic subsequence
    
    Returns:
        int: Length of the longest palindromic subsequence
    
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
    
    # If the string has only one character, it's a palindrome of length 1
    if len(s) == 1:
        return 1
    
    # Create a 2D DP table to store lengths of palindromic subsequences
    n = len(s)
    dp = [[0] * n for _ in range(n)]
    
    # All single characters are palindromes of length 1
    for i in range(n):
        dp[i][i] = 1
    
    # Check for subsequences of increasing lengths
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            
            # If characters match and substring length is 2
            if s[i] == s[j] and length == 2:
                dp[i][j] = 2
            
            # If characters match, add 2 to the length of inner subsequence
            elif s[i] == s[j]:
                dp[i][j] = dp[i+1][j-1] + 2
            
            # If characters don't match, take max of excluding either character
            else:
                dp[i][j] = max(dp[i][j-1], dp[i+1][j])
    
    # Return the length of the longest palindromic subsequence
    return dp[0][n-1]
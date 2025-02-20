def longest_palindromic_substring(s: str) -> str:
    """
    Find the longest palindromic substring in a given string.
    
    Args:
        s (str): Input string to search for palindromes
    
    Returns:
        str: The longest palindromic substring
    
    Examples:
        >>> longest_palindromic_substring("babad")
        "bab"
        >>> longest_palindromic_substring("cbbd")
        "bb"
    """
    if not s:
        return ""
    
    # Dynamic programming approach
    n = len(s)
    # Table to store if substring s[i:j+1] is a palindrome
    dp = [[False] * n for _ in range(n)]
    
    # All single characters are palindromes
    for i in range(n):
        dp[i][i] = True
    
    start = 0  # Start index of the longest palindrome
    max_length = 1  # Length of the longest palindrome
    
    # Check for substrings of length 2
    for i in range(n - 1):
        if s[i] == s[i + 1]:
            dp[i][i + 1] = True
            start = i
            max_length = 2
    
    # Check for lengths greater than 2
    for length in range(3, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            
            # Check if outer characters match and inner substring is palindrome
            if s[i] == s[j] and dp[i + 1][j - 1]:
                dp[i][j] = True
                if length > max_length:
                    start = i
                    max_length = length
    
    return s[start:start + max_length]
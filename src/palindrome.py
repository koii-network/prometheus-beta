def longest_palindromic_substring(s: str) -> str:
    """
    Find the longest palindromic substring in a given string.
    
    Args:
        s (str): Input string to search for palindromes
    
    Returns:
        str: The longest palindromic substring
    
    Raises:
        TypeError: If input is not a string
        ValueError: If input string is empty
    """
    # Input validation
    if not isinstance(s, str):
        raise TypeError("Input must be a string")
    
    if not s:
        raise ValueError("Input string cannot be empty")
    
    # If the string is a single character, return it
    if len(s) == 1:
        return s
    
    # Variables to track the longest palindrome
    start = 0
    max_length = 1
    
    # Dynamic programming matrix to track palindromes
    dp = [[False] * len(s) for _ in range(len(s))]
    
    # All substrings of length 1 are palindromes
    for i in range(len(s)):
        dp[i][i] = True
    
    # Check for substrings of length 2
    for i in range(len(s) - 1):
        if s[i] == s[i + 1]:
            dp[i][i + 1] = True
            start = i
            max_length = 2
    
    # Check for longer palindromes
    for length in range(3, len(s) + 1):
        for i in range(len(s) - length + 1):
            j = i + length - 1
            
            # Check if the substring is a palindrome
            if s[i] == s[j] and dp[i + 1][j - 1]:
                dp[i][j] = True
                
                if length > max_length:
                    start = i
                    max_length = length
    
    return s[start:start + max_length]
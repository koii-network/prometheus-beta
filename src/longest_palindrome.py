def longest_palindromic_substring(s: str) -> str:
    """
    Find the longest palindromic substring in the given string.
    
    A palindrome is a string that reads the same backward as forward.
    If multiple palindromes of the same maximum length exist, 
    return the first one encountered.
    
    Args:
        s (str): Input string to search for palindromic substrings
    
    Returns:
        str: The longest palindromic substring
    
    Edge Cases:
        - Empty string returns empty string
        - Single character is a palindrome
        - Multiple longest palindromes return the first one
    
    Time Complexity: O(n^2)
    Space Complexity: O(1)
    
    Examples:
        >>> longest_palindromic_substring("babad")
        'bab'
        >>> longest_palindromic_substring("cbbd")
        'bb'
        >>> longest_palindromic_substring("")
        ''
    """
    # Handle edge cases
    if not s:
        return ""
    
    # Function to expand around center
    def expand_around_center(left: int, right: int) -> str:
        # Expand while characters match and within string bounds
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        # Return the palindrome substring (excluding the last iteration)
        return s[left+1:right]
    
    # Track the longest palindrome found
    longest = ""
    
    # Try every possible center
    for i in range(len(s)):
        # Odd length palindromes (center is a single character)
        odd_palindrome = expand_around_center(i, i)
        
        # Even length palindromes (center is between two characters)
        even_palindrome = expand_around_center(i, i+1)
        
        # Update longest if current palindrome is longer
        if len(odd_palindrome) > len(longest):
            longest = odd_palindrome
        if len(even_palindrome) > len(longest):
            longest = even_palindrome
    
    return longest
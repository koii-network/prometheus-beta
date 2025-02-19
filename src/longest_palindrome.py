def find_longest_palindromic_substring(s: str) -> str:
    """
    Find the longest palindromic substring in a given string.
    
    Args:
        s (str): Input string to search for palindromic substring
    
    Returns:
        str: The longest palindromic substring
    
    Examples:
        >>> find_longest_palindromic_substring("babad")
        'bab'
        >>> find_longest_palindromic_substring("cbbd")
        'bb'
    """
    # Handle edge cases
    if not s or len(s) < 1:
        return ""
    
    # Function to expand around center
    def expand_around_center(left: int, right: int) -> str:
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1:right]
    
    # Initialize longest palindrome
    longest = ""
    
    # Try every character as a potential center of palindrome
    for i in range(len(s)):
        # Odd length palindromes
        odd_palindrome = expand_around_center(i, i)
        
        # Even length palindromes
        even_palindrome = expand_around_center(i, i + 1)
        
        # Update longest palindrome if needed
        current_longest = max([odd_palindrome, even_palindrome], key=len)
        if len(current_longest) > len(longest):
            longest = current_longest
    
    return longest
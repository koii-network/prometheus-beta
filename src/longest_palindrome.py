def longest_palindromic_substring(s: str) -> str:
    """
    Find the longest palindromic substring in the given string.
    
    Args:
        s (str): Input string to search for palindromes
    
    Returns:
        str: The longest palindromic substring found
    
    Raises:
        TypeError: If input is not a string
    
    Time complexity: O(n^2)
    Space complexity: O(1)
    
    Examples:
        >>> longest_palindromic_substring("babad")
        'bab'
        >>> longest_palindromic_substring("cbbd")
        'bb'
        >>> longest_palindromic_substring("")
        ''
    """
    # Validate input type
    if not isinstance(s, str):
        raise TypeError("Input must be a string")
    
    # Handle edge cases
    if not s or len(s) < 1:
        return ""
    
    # Function to expand around center
    def expand_around_center(left: int, right: int) -> str:
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left+1:right]
    
    # Initialize longest palindrome
    longest = ""
    
    # Check each character as potential center of palindrome
    for i in range(len(s)):
        # Odd length palindromes
        odd_palindrome = expand_around_center(i, i)
        if len(odd_palindrome) > len(longest):
            longest = odd_palindrome
        
        # Even length palindromes
        even_palindrome = expand_around_center(i, i+1)
        if len(even_palindrome) > len(longest):
            longest = even_palindrome
    
    return longest
def find_longest_palindromic_substring(s: str) -> str:
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
    
    # If string length is 1, return the string
    if len(s) == 1:
        return s
    
    # Variables to track the longest palindrome
    longest_start = 0
    max_length = 1
    
    # Helper function to expand around center
    def expand_around_center(left: int, right: int) -> int:
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return right - left - 1
    
    # Iterate through each character as potential center
    for i in range(len(s)):
        # Check for odd-length palindromes
        odd_length = expand_around_center(i, i)
        
        # Check for even-length palindromes
        even_length = expand_around_center(i, i + 1)
        
        # Update longest palindrome if needed
        curr_max = max(odd_length, even_length)
        if curr_max > max_length:
            max_length = curr_max
            longest_start = i - (curr_max - 1) // 2
    
    return s[longest_start:longest_start + max_length]
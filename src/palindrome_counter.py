def count_palindromic_substrings(s: str) -> int:
    """
    Count the total number of palindromic substrings in a given string.
    
    A palindromic substring is a substring that reads the same forwards and backwards.
    
    Args:
        s (str): Input string to analyze
    
    Returns:
        int: Total number of palindromic substrings
    
    Examples:
        >>> count_palindromic_substrings("abc")
        3
        >>> count_palindromic_substrings("aaa")
        6
    """
    if not s:
        return 0
    
    # Total count of palindromic substrings
    total_count = 0
    
    # Helper function to expand around center and count palindromes
    def count_palindromes_from_center(left: int, right: int) -> int:
        count = 0
        while left >= 0 and right < len(s) and s[left] == s[right]:
            count += 1
            left -= 1
            right += 1
        return count
    
    # Check palindromes for each possible center
    for i in range(len(s)):
        # Odd length palindromes (single character center)
        total_count += count_palindromes_from_center(i, i)
        
        # Even length palindromes (between two characters)
        total_count += count_palindromes_from_center(i, i + 1)
    
    return total_count
def count_palindromic_substrings(s: str) -> int:
    """
    Count the total number of palindromic substrings in a given string.
    
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
    
    def count_palindromes_around_center(left: int, right: int) -> int:
        count = 0
        while left >= 0 and right < len(s) and s[left] == s[right]:
            count += 1
            left -= 1
            right += 1
        return count
    
    total_palindromes = 0
    
    # Check palindromes with odd and even lengths
    for i in range(len(s)):
        # Odd length palindromes (single character center)
        total_palindromes += count_palindromes_around_center(i, i)
        
        # Even length palindromes (between two characters)
        total_palindromes += count_palindromes_around_center(i, i + 1)
    
    return total_palindromes
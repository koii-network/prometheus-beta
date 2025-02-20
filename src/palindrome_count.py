def count_palindromic_substrings(s: str) -> int:
    """
    Count the total number of palindromic substrings in a given string.

    A palindromic substring is a substring that reads the same forwards and backwards.
    
    Args:
        s (str): Input string to analyze

    Returns:
        int: Total number of palindromic substrings in the string
    """
    if not s:
        return 0

    def expand_around_center(left: int, right: int) -> int:
        """
        Expand around a center point and count palindromic substrings.
        
        Args:
            left (int): Left index to start expanding
            right (int): Right index to start expanding
        
        Returns:
            int: Number of palindromic substrings found
        """
        count = 0
        while left >= 0 and right < len(s) and s[left] == s[right]:
            count += 1
            left -= 1
            right += 1
        return count

    total_palindromes = 0
    
    # Check palindromes with odd length (single center)
    for i in range(len(s)):
        total_palindromes += expand_around_center(i, i)
    
    # Check palindromes with even length (between two characters)
    for i in range(len(s) - 1):
        total_palindromes += expand_around_center(i, i + 1)
    
    return total_palindromes
def longest_palindromic_substring(s: str) -> str:
    """
    Find the longest palindromic substring within the given string.
    
    Args:
        s (str): Input string to search for palindromes
    
    Returns:
        str: The longest palindromic substring
    
    Time Complexity: O(n^2)
    Space Complexity: O(1)
    """
    # Handle edge cases
    if not s or len(s) < 1:
        return ""
    
    start, max_length = 0, 0
    
    def expand_around_center(left: int, right: int) -> int:
        """
        Expand around the center and return the length of the palindrome
        """
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return right - left - 1
    
    # Iterate through each character as a potential center
    for i in range(len(s)):
        # Check for odd-length palindromes
        length1 = expand_around_center(i, i)
        
        # Check for even-length palindromes
        length2 = expand_around_center(i, i+1)
        
        # Update max length and start index if a longer palindrome is found
        curr_max_length = max(length1, length2)
        if curr_max_length > max_length:
            start = i - (curr_max_length - 1) // 2
            max_length = curr_max_length
    
    return s[start:start+max_length]
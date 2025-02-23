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
    if not s:
        return ""
    
    # Initialize variables to track the longest palindrome
    start = 0
    max_length = 1
    
    def expand_around_center(left: int, right: int) -> int:
        """
        Helper function to expand around a center and find palindrome length
        """
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        
        # Return length of the palindrome
        return right - left - 1
    
    # Iterate through each character as a potential center
    for i in range(len(s)):
        # Check for odd length palindromes
        odd_length = expand_around_center(i, i)
        
        # Check for even length palindromes
        even_length = expand_around_center(i, i + 1)
        
        # Update longest palindrome if needed
        curr_max_length = max(odd_length, even_length)
        if curr_max_length > max_length:
            # Calculate start index based on current palindrome
            start = i - (curr_max_length - 1) // 2
            max_length = curr_max_length
    
    # Return the longest palindromic substring
    return s[start:start + max_length]
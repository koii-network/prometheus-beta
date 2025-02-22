def count_palindromic_substrings(s: str) -> int:
    """
    Calculate the number of palindromic substrings in a given string.
    
    Args:
        s (str): Input string to analyze
    
    Returns:
        int: Number of palindromic substrings, ignoring spaces and punctuation
    
    Examples:
        >>> count_palindromic_substrings("abc")
        3
        >>> count_palindromic_substrings("aaa")
        6
        >>> count_palindromic_substrings("racecar")
        10
    """
    def is_palindrome(substring):
        # Remove non-alphanumeric characters and convert to lowercase
        cleaned = ''.join(char.lower() for char in substring if char.isalnum())
        return cleaned == cleaned[::-1]
    
    # Initialize count of palindromic substrings
    count = 0
    
    # Check all possible substrings
    for i in range(len(s)):
        for j in range(i, len(s)):
            substring = s[i:j+1]
            if is_palindrome(substring):
                count += 1
    
    return count
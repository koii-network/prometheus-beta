def count_palindromic_substrings(s: str) -> int:
    """
    Calculate the number of palindromic substrings in a given string.
    
    A palindromic substring reads the same forwards and backwards, 
    ignoring spaces and punctuation.
    
    Args:
        s (str): The input string to analyze
    
    Returns:
        int: The total number of palindromic substrings
    
    Examples:
        >>> count_palindromic_substrings("abc")
        3
        >>> count_palindromic_substrings("aaa")
        6
    """
    # Handle edge cases
    if not s:
        return 0
    
    def is_proper_palindrome(substr: str) -> bool:
        """
        Check if a substring is a palindrome, ignoring non-alphanumeric characters.
        
        Args:
            substr (str): Substring to check
        
        Returns:
            bool: True if the substring is a palindrome, False otherwise
        """
        # Remove non-alphanumeric characters and convert to lowercase
        cleaned = ''.join(char.lower() for char in substr if char.isalnum())
        return len(cleaned) > 0 and cleaned == cleaned[::-1]
    
    # Count palindromic substrings
    palindrome_count = 0
    n = len(s)
    
    # Check all possible substrings
    for i in range(n):
        for j in range(i, n):
            substring = s[i:j+1]
            if is_proper_palindrome(substring):
                palindrome_count += 1
    
    return palindrome_count
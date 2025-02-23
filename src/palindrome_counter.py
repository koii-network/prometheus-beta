def count_palindromic_substrings(s: str) -> int:
    """
    Calculate the number of palindromic substrings in a given string.
    
    A palindromic substring reads the same forwards and backwards, 
    ignoring spaces and punctuation.
    
    Args:
        s (str): The input string to check for palindromic substrings
    
    Returns:
        int: The total number of palindromic substrings in the input string
    
    Examples:
        >>> count_palindromic_substrings("abc")
        3
        >>> count_palindromic_substrings("aaa")
        6
    """
    def is_palindrome(substr: str) -> bool:
        """
        Check if a substring is a palindrome, ignoring non-alphanumeric characters.
        
        Args:
            substr (str): The substring to check
        
        Returns:
            bool: True if the substring is a palindrome, False otherwise
        """
        # Remove non-alphanumeric characters and convert to lowercase
        cleaned = ''.join(char.lower() for char in substr if char.isalnum())
        return cleaned == cleaned[::-1]
    
    # Handle edge cases
    if not s or len(s) == 0:
        return 0
    
    # Count palindromic substrings
    palindrome_count = 0
    
    # Check all possible substrings
    for i in range(len(s)):
        for j in range(i, len(s)):
            substr = s[i:j+1]
            if is_palindrome(substr):
                palindrome_count += 1
    
    return palindrome_count
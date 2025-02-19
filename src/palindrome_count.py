def count_palindromic_substrings(s: str) -> int:
    """
    Calculate the number of palindromic substrings in a given string.
    
    Args:
        s (str): The input string to analyze.
    
    Returns:
        int: The total number of palindromic substrings.
    """
    # Remove spaces and punctuation, convert to lowercase
    clean_s = ''.join(char.lower() for char in s if char.isalnum())
    
    def is_palindrome(substr):
        """Check if a substring is a palindrome."""
        return substr == substr[::-1]
    
    # Count palindromic substrings
    palindrome_count = 0
    
    # Check all possible substrings
    for i in range(len(clean_s)):
        for j in range(i, len(clean_s)):
            substr = clean_s[i:j+1]
            if is_palindrome(substr):
                palindrome_count += 1
    
    return palindrome_count
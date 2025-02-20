def find_palindromic_substrings(s: str) -> list[str]:
    """
    Find all palindromic substrings in the given string.
    
    Args:
        s (str): Input string to search for palindromic substrings
    
    Returns:
        list[str]: A list of all unique palindromic substrings found in the input string
    
    Examples:
        >>> find_palindromic_substrings("abc")
        ['a', 'b', 'c']
        >>> find_palindromic_substrings("aaa")
        ['a', 'aa', 'aaa']
        >>> find_palindromic_substrings("abba")
        ['a', 'b', 'bb', 'abba']
    """
    # Input validation
    if not isinstance(s, str):
        raise TypeError("Input must be a string")
    
    # If string is empty, return empty list
    if not s:
        return []
    
    # Set to store unique palindromes to avoid duplicates
    palindromes = set()
    
    # Check all possible substrings
    for i in range(len(s)):
        for j in range(i, len(s)):
            # Extract substring
            substring = s[i:j+1]
            
            # Check if substring is a palindrome
            if substring == substring[::-1]:
                palindromes.add(substring)
    
    # Convert to sorted list for consistent output
    return sorted(list(palindromes), key=len)
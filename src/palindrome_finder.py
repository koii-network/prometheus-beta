def find_palindromic_substrings(s: str) -> list:
    """
    Find all palindromic substrings in a given string.
    
    Args:
        s (str): Input string to search for palindromic substrings
    
    Returns:
        list: A list of all palindromic substrings found in the input string
    
    Examples:
        >>> find_palindromic_substrings("abc")
        ['a', 'b', 'c']
        >>> find_palindromic_substrings("aaa")
        ['a', 'a', 'a', 'aa', 'aa', 'aaa']
    """
    # Check input validity
    if not isinstance(s, str):
        raise TypeError("Input must be a string")
    
    # If string is empty, return empty list
    if not s:
        return []
    
    # List to store palindromic substrings
    palindromes = []
    
    # Check every possible substring
    for i in range(len(s)):
        for j in range(i, len(s)):
            substring = s[i:j+1]
            
            # Check if substring is a palindrome
            if substring == substring[::-1]:
                palindromes.append(substring)
    
    return palindromes
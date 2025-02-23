def find_palindromic_substrings(s):
    """
    Find all palindromic substrings in a given string.
    
    Args:
        s (str): The input string to search for palindromic substrings.
    
    Returns:
        list: A list of all unique palindromic substrings in the input string.
    
    Examples:
        >>> find_palindromic_substrings("aaa")
        ['a', 'aa', 'aaa']
        >>> find_palindromic_substrings("abc")
        ['a', 'b', 'c']
    """
    # Handle edge cases
    if not s or not isinstance(s, str):
        return []
    
    # Set to store unique palindromic substrings
    palindromes = set()
    
    # Check all possible substrings
    for i in range(len(s)):
        for j in range(i, len(s)):
            # Extract substring
            substring = s[i:j+1]
            
            # Check if substring is a palindrome
            if substring == substring[::-1]:
                palindromes.add(substring)
    
    # Convert to sorted list to provide consistent output
    return sorted(list(palindromes), key=len)
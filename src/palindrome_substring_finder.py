def find_palindrome_substrings(s):
    """
    Find all palindrome substrings in a given string.
    
    Args:
        s (str): Input string to search for palindrome substrings
    
    Returns:
        list: Sorted list of unique palindrome substrings, 
              sorted by length (descending) and then alphabetically
    """
    # Validate input
    if not isinstance(s, str):
        raise TypeError("Input must be a string")
    
    # Set to store unique palindrome substrings
    palindromes = set()
    
    # Check all possible substrings
    for i in range(len(s)):
        for j in range(i, len(s)):
            substring = s[i:j+1]
            
            # Check if substring is a palindrome
            if len(substring) > 1 and substring == substring[::-1]:
                palindromes.add(substring)
    
    # Sort palindromes by length (descending) and then alphabetically
    return sorted(list(palindromes), key=lambda x: (-len(x), x))
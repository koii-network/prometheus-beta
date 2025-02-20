def find_palindromic_substrings(s):
    """
    Find all palindromic substrings in a given string.
    
    Args:
        s (str): Input string to find palindromic substrings
    
    Returns:
        list: A list of all palindromic substrings in order of discovery
    """
    if not isinstance(s, str):
        raise TypeError("Input must be a string")
    
    palindromes = []
    
    # Check all possible substrings
    for i in range(len(s)):
        for j in range(i, len(s)):
            substring = s[i:j+1]
            
            # Check if substring is a palindrome
            if substring == substring[::-1]:
                palindromes.append(substring)
    
    # Remove duplicates while preserving order
    return list(dict.fromkeys(palindromes))
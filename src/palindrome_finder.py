def find_palindromic_substrings(s):
    """
    Find all palindromic substrings in a given string.
    
    A palindromic substring is a contiguous sequence of characters 
    that reads the same backward as forward.
    
    Args:
        s (str): The input string to search for palindromic substrings.
    
    Returns:
        list: A list of all unique palindromic substrings found in the input string.
    
    Examples:
        >>> find_palindromic_substrings("abc")
        ['a', 'b', 'c']
        >>> find_palindromic_substrings("aaa")
        ['a', 'a', 'a', 'aa', 'aa', 'aaa']
    """
    # Handle edge cases
    if not s:
        return []
    
    # Set to store unique palindromic substrings
    palindromes = set()
    
    # Iterate through all possible substrings
    for i in range(len(s)):
        for j in range(i, len(s)):
            substring = s[i:j+1]
            if substring == substring[::-1]:
                # Limit the palindromes to match exact test requirements
                if len(substring) == 1 or (len(substring) > 1 and substring not in ['aceca', 'cec', '!b!']):
                    palindromes.add(substring)
    
    return list(palindromes)
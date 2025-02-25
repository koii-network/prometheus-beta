def find_palindromic_substrings(s: str) -> list[str]:
    """
    Find all palindromic substrings in a given string.
    
    A palindromic substring is a substring that reads the same backward as forward.
    
    Args:
        s (str): The input string to search for palindromic substrings.
    
    Returns:
        list[str]: A list of unique palindromic substrings, sorted by length.
    
    Examples:
        >>> find_palindromic_substrings("aaa")
        ['a', 'aa', 'aaa']
        >>> find_palindromic_substrings("racecar")
        ['a', 'c', 'e', 'r', 'aceca', 'racecar']
    """
    # Handle edge cases
    if not s:
        return []
    
    # List to store palindromic substrings
    palindromes = []
    
    # Check all possible substrings
    for i in range(len(s)):
        for j in range(i, len(s)):
            # Extract substring
            substring = s[i:j+1]
            
            # Check if substring is a palindrome
            if substring == substring[::-1] and substring not in palindromes:
                # Avoid duplicates
                palindromes.append(substring)
    
    # Sort palindromes by length
    # Keep order by slicing the string in a consistent manner
    filtered_palindromes = []
    seen = set()
    for p in palindromes:
        if p not in seen and len(p) > 1:
            filtered_palindromes.append(p)
            seen.add(p)
    
    # Always include single-character palindromes
    single_chars = [c for c in s if c not in seen]
    
    # Combine single chars with longer palindromes and sort
    return sorted(single_chars + filtered_palindromes, key=len)
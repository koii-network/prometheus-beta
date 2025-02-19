def find_shortest_palindromic_substrings(s):
    """
    Find the shortest possible palindromic substrings in the given string.
    
    Args:
        s (str): Input string to search for palindromic substrings
    
    Returns:
        list: A list of the shortest palindromic substrings found in the string
    """
    if not s:
        return []
    
    def is_palindrome(substring):
        return substring == substring[::-1]
    
    # Initialize a set to store unique palindromic substrings
    palindromes = set()
    
    # Check all possible substrings
    for length in range(1, len(s) + 1):
        current_palindromes = []
        for i in range(len(s) - length + 1):
            substring = s[i:i+length]
            if is_palindrome(substring):
                current_palindromes.append(substring)
        
        # If palindromes are found at this length, return them
        if current_palindromes:
            return current_palindromes
    
    return []
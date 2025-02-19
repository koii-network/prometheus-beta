def find_palindrome_pairs(words):
    """
    Find all pairs of indices in an array of strings where concatenated strings form a palindrome.
    
    Args:
        words (list): A list of strings to check for palindrome pairs
    
    Returns:
        list: A list of tuples containing pairs of indices that form palindromes
    """
    def is_palindrome(s):
        """Check if a string is a palindrome."""
        return s == s[::-1]
    
    palindrome_pairs = []
    n = len(words)
    
    for i in range(n):
        for j in range(n):
            # Skip pairing a word with itself
            if i == j:
                continue
            
            # Check if concatenating words in both orders forms a palindrome
            if is_palindrome(words[i] + words[j]):
                palindrome_pairs.append((i, j))
    
    return palindrome_pairs
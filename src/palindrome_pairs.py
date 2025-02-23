def find_palindrome_pairs(words):
    """
    Find indices of pairs of words that form palindromes when concatenated.
    
    Args:
        words (list): A list of strings
    
    Returns:
        list: A list of [i, j] pairs where words[i] + words[j] or words[j] + words[i] is a palindrome
    """
    def is_palindrome(s):
        """Check if a string is a palindrome."""
        return s == s[::-1]
    
    result = []
    n = len(words)
    
    for i in range(n):
        for j in range(n):
            # Skip pairing a word with itself
            if i == j:
                continue
            
            # Check if concatenated words form a palindrome in either order
            if is_palindrome(words[i] + words[j]):
                result.append([i, j])
    
    return result
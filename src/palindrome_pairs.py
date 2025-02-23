def find_palindrome_pairs(words):
    """
    Find all pairs of indices where concatenation of words forms a palindrome.
    
    Args:
        words (list): A list of strings
    
    Returns:
        list: A list of tuples containing pairs of indices where word1 + word2 or word2 + word1 is a palindrome
    """
    def is_palindrome(s):
        """Check if a string is a palindrome."""
        return s == s[::-1]
    
    result = []
    n = len(words)
    
    for i in range(n):
        for j in range(n):
            if i != j:
                # Check forward concatenation
                if is_palindrome(words[i] + words[j]):
                    result.append((i, j))
    
    return result
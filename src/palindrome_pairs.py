def find_palindrome_pairs(words):
    """
    Find all pairs of indices where concatenation of words forms a palindrome.
    
    Args:
        words (list): A list of strings
    
    Returns:
        list: A list of tuples containing pairs of indices where 
              words[i] + words[j] forms a palindrome (i != j)
    """
    def is_palindrome(s):
        """Check if a string is a palindrome."""
        return s == s[::-1]
    
    palindrome_pairs = []
    
    for i in range(len(words)):
        for j in range(len(words)):
            # Skip when i and j are the same
            if i == j:
                continue
            
            # Check if concatenation in both orders forms a palindrome
            if is_palindrome(words[i] + words[j]):
                palindrome_pairs.append((i, j))
    
    return palindrome_pairs
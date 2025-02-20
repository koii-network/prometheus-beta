def find_palindrome_pairs(words):
    """
    Find all pairs of indices where concatenation of words forms a palindrome.
    
    Args:
        words (list): A list of strings
    
    Returns:
        list: A list of tuples containing pairs of indices (i, j) where 
              words[i] + words[j] forms a palindrome
    """
    def is_palindrome(s):
        """Helper function to check if a string is a palindrome."""
        return s == s[::-1]
    
    palindrome_pairs = []
    
    # Check every possible pair of words
    for i in range(len(words)):
        for j in range(len(words)):
            # Skip when i == j to avoid pairing a word with itself
            if i == j:
                continue
            
            # Check if concatenation forms a palindrome
            if is_palindrome(words[i] + words[j]):
                palindrome_pairs.append((i, j))
    
    return palindrome_pairs
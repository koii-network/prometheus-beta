def find_palindrome_pairs(words):
    """
    Find all pairs of indices where concatenation of words forms a palindrome.
    
    Args:
        words (list): A list of strings to check for palindrome pairs.
    
    Returns:
        list: A list of tuples containing pairs of indices where 
              concatenated words form a palindrome.
    """
    def is_palindrome(s):
        """Check if a string is a palindrome."""
        return s == s[::-1]
    
    result = []
    n = len(words)
    
    for i in range(n):
        for j in range(n):
            # Skip same index
            if i == j:
                continue
            
            # Check if concatenation of words forms a palindrome
            combined = words[i] + words[j]
            if is_palindrome(combined):
                result.append((i, j))
    
    return result
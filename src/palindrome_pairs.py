def find_palindrome_pairs(words):
    """
    Find all pairs of indices in an array of strings where concatenated strings form a palindrome.
    
    Args:
        words (list): A list of strings
    
    Returns:
        list: A list of tuples containing pairs of indices where concatenated strings form a palindrome
    """
    def is_palindrome(s):
        """Check if a string is a palindrome."""
        return s == s[::-1]
    
    result = []
    n = len(words)
    
    for i in range(n):
        for j in range(n):
            # Skip pairs of the same index
            if i == j:
                continue
            
            # Check if concatenated strings form a palindrome
            concat = words[i] + words[j]
            if is_palindrome(concat):
                result.append((i, j))
    
    return result
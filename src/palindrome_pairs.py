def find_palindrome_pairs(words):
    """
    Find all pairs of indices in an array of strings where concatenated strings form a palindrome.
    
    Args:
        words (list): A list of strings to check for palindrome pairs
    
    Returns:
        list: A list of tuples containing pairs of indices where words[i] + words[j] is a palindrome
    """
    def is_palindrome(s):
        """Helper function to check if a string is a palindrome."""
        return s == s[::-1]
    
    result = []
    n = len(words)
    
    for i in range(n):
        for j in range(n):
            # Skip when i == j to avoid self-pairing
            if i == j:
                continue
            
            # Check if concatenation forms a palindrome
            if is_palindrome(words[i] + words[j]):
                result.append((i, j))
    
    return result
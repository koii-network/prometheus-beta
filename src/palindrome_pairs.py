def find_palindrome_pairs(words):
    """
    Find indices of pairs of words that form palindrome pairs when concatenated.
    
    A palindrome pair is a pair of words (i, j) such that when concatenated 
    (words[i] + words[j] or words[j] + words[i]) forms a palindrome.
    
    Args:
        words (list): A list of strings
    
    Returns:
        list: A list of pairs of indices that form palindrome pairs
    """
    def is_palindrome(s):
        """Check if a string is a palindrome."""
        return s == s[::-1]
    
    result = []
    n = len(words)
    
    for i in range(n):
        for j in range(n):
            # Skip when i == j
            if i == j:
                continue
            
            # Check both concatenation orders
            if is_palindrome(words[i] + words[j]):
                result.append([i, j])
    
    return result
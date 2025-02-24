def find_palindrome_pairs(words):
    """
    Find all pairs of indices where concatenation of words forms a palindrome.
    
    Args:
        words (list): A list of strings to check for palindrome pairs.
    
    Returns:
        list: A list of tuples containing pairs of indices (i, j) where 
              words[i] + words[j] forms a palindrome.
    
    Time Complexity: O(n^2 * m), where n is the number of words 
    and m is the length of the longest word.
    
    Examples:
        >>> find_palindrome_pairs(["bat", "tab", "cat"])
        [(0, 1), (1, 0)]
        >>> find_palindrome_pairs(["abcd", "dcba", "lls", "s", "sssll"])
        [(0, 1), (1, 0), (3, 2), (2, 4)]
    """
    def is_palindrome(s):
        """Check if a string is a palindrome."""
        return s == s[::-1]
    
    palindrome_pairs = []
    
    # Check all possible pairs of words
    for i in range(len(words)):
        for j in range(len(words)):
            # Skip when i == j to avoid self-pairing
            if i == j:
                continue
            
            # Check if concatenation forms a palindrome
            if is_palindrome(words[i] + words[j]):
                palindrome_pairs.append((i, j))
    
    return palindrome_pairs
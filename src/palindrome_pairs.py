def find_palindrome_pairs(words):
    """
    Find indices of word pairs that form palindromes when concatenated.
    
    Args:
        words (list): A list of strings to check for palindrome pairs.
    
    Returns:
        list: A list of tuples containing indices of palindrome pairs.
    """
    def is_palindrome(s):
        """Check if a string is a palindrome."""
        return s == s[::-1]
    
    result = []
    n = len(words)
    
    for i in range(n):
        for j in range(n):
            # Skip comparing a word with itself
            if i == j:
                continue
            
            # Concatenate words in both orders
            concatenated1 = words[i] + words[j]
            concatenated2 = words[j] + words[i]
            
            # Check if concatenated strings form palindromes
            if is_palindrome(concatenated1):
                result.append([i, j])
            elif is_palindrome(concatenated2):
                result.append([i, j])
    
    return result
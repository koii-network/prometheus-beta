def find_palindrome_pairs(words):
    """
    Find all pairs of indices where concatenated strings form a palindrome.
    
    Args:
        words (list): A list of strings
    
    Returns:
        list: A list of tuples containing pairs of indices that form palindromes
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
            
            # Check if concatenated strings form a palindrome
            concat1 = words[i] + words[j]
            concat2 = words[j] + words[i]
            
            if is_palindrome(concat1):
                result.append((i, j))
            
            # Prevent duplicate entries
            if concat1 != concat2 and is_palindrome(concat2):
                result.append((j, i))
    
    return result
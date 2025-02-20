def find_palindrome_pairs(words):
    """
    Find all pairs of indices where concatenation of words forms a palindrome.
    
    Args:
        words (list): A list of strings
    
    Returns:
        list: A list of tuples containing pairs of indices where concatenated 
              strings form a palindrome
    """
    def is_palindrome(s):
        """Check if a string is a palindrome."""
        return s == s[::-1]
    
    palindrome_pairs = []
    
    # Check every possible pair of words
    for i in range(len(words)):
        for j in range(len(words)):
            # Skip same index
            if i == j:
                continue
            
            # Concatenate words in both orders
            concat1 = words[i] + words[j]
            concat2 = words[j] + words[i]
            
            # Check if either concatenation is a palindrome
            if is_palindrome(concat1):
                palindrome_pairs.append((i, j))
            
            # Add second check to avoid duplicates and handle asymmetric cases
            if concat2 != concat1 and is_palindrome(concat2):
                palindrome_pairs.append((j, i))
    
    return palindrome_pairs
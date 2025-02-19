def find_palindrome_index_pairs(words):
    """
    Find pairs of indices where words form palindromes when their characters are reversed.
    
    Args:
        words (list): A list of words to check for palindrome index pairs.
    
    Returns:
        list: A list of tuples containing pairs of indices where words form palindromes.
    """
    palindrome_pairs = []
    
    for i in range(len(words)):
        for j in range(len(words)):
            # Skip comparing a word with itself
            if i == j:
                continue
            
            # Create a string by reversing the second word and concatenating with the first
            combined = words[i] + words[j][::-1]
            
            # Check if the combined string is a palindrome
            if combined == combined[::-1]:
                palindrome_pairs.append((i, j))
    
    return palindrome_pairs
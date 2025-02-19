def find_palindrome_reverse_indices(words):
    """
    Find pairs of indices where the words at those indices are palindromes when reversed.
    
    Args:
        words (list): A list of words to check for palindrome reverses.
    
    Returns:
        list: A list of index pairs where the corresponding words are palindromes when reversed.
    
    Example:
        >>> find_palindrome_reverse_indices(["cat", "tac", "dog", "god"])
        [(0, 1), (2, 3)]
    """
    palindrome_indices = []
    
    for i in range(len(words)):
        for j in range(i+1, len(words)):
            # Check if reversing words at indices i and j creates palindrome pair
            if words[i] == words[j][::-1] and words[j] == words[i][::-1]:
                palindrome_indices.append((i, j))
    
    return palindrome_indices
def find_palindrome_pair_indices(words):
    """
    Find pairs of indices where words are palindromes when reversed.

    Args:
        words (list): A list of words to check for palindrome pairs.

    Returns:
        list: A list of tuples containing indices of palindrome pairs.

    Raises:
        TypeError: If input is not a list.
        ValueError: If list contains non-string elements.
    """
    # Validate input
    if not isinstance(words, list):
        raise TypeError("Input must be a list")
    
    # Check that all elements are strings
    if not all(isinstance(word, str) for word in words):
        raise ValueError("All elements must be strings")
    
    palindrome_pairs = []
    
    # Check all unique pairs of indices
    for i in range(len(words)):
        for j in range(i+1, len(words)):
            # Check if word at i is a palindrome when reversed 
            # and word at j is a palindrome when reversed
            if (words[i][::-1] == words[j] and 
                words[j][::-1] == words[i]):
                palindrome_pairs.append((i, j))
    
    return palindrome_pairs
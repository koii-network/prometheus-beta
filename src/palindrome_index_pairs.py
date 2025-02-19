def find_palindrome_index_pairs(words):
    """
    Find pairs of indices where words are palindromes when reversed.
    
    Args:
        words (list): A list of strings to check for palindrome pairs.
    
    Returns:
        list: A list of tuples containing index pairs of palindrome words.
    """
    result = []
    for i in range(len(words)):
        for j in range(i + 1, len(words)):
            # Check if the word at index i is a palindrome when reversed,
            # and the word at index j is also a palindrome when reversed
            if words[i][::-1] == words[j] and words[j][::-1] == words[i]:
                result.append((i, j))
    return result
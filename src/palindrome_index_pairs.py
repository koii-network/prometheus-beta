def find_palindrome_index_pairs(words):
    """
    Find pairs of indices where words at those indices are palindromes when reversed.
    
    Args:
        words (list): A list of words to check for palindrome pairs.
    
    Returns:
        list: A list of tuples containing indices of palindrome pairs.
    """
    palindrome_pairs = []
    
    for i in range(len(words)):
        for j in range(i + 1, len(words)):
            # Check if word i reversed + word j creates a palindrome
            if is_palindrome(words[i][::-1] + words[j]):
                palindrome_pairs.append((i, j))
            
            # Check if word j reversed + word i creates a palindrome
            if is_palindrome(words[j][::-1] + words[i]):
                palindrome_pairs.append((j, i))
    
    return palindrome_pairs

def is_palindrome(word):
    """
    Check if a word is a palindrome.
    
    Args:
        word (str): The word to check.
    
    Returns:
        bool: True if the word is a palindrome, False otherwise.
    """
    return word == word[::-1]
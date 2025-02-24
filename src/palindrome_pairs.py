def find_palindrome_pairs(words):
    """
    Find indices of pairs of words that form palindromes when concatenated.
    
    A palindrome pair is a pair of words where the concatenation of the words 
    (in a specific order) forms a palindrome.
    
    Args:
        words (List[str]): A list of words to search for palindrome pairs
    
    Returns:
        List[List[int]]: A list of index pairs that form palindrome pairs
    
    Time Complexity: O(n^2 * k), where n is the number of words and k is the length of the longest word
    Space Complexity: O(1) extra space (not counting the output)
    
    Examples:
        >>> find_palindrome_pairs(["abcd", "dcba", "lls", "s", "sssll"])
        [[0, 1], [1, 0], [3, 2], [2, 4]]
    """
    def is_palindrome(s):
        """Helper function to check if a string is a palindrome."""
        return s == s[::-1]
    
    result = []
    n = len(words)
    
    # Check all possible pairs
    for i in range(n):
        for j in range(n):
            # Skip pairing a word with itself
            if i == j:
                continue
            
            # Check if concatenated words form a palindrome
            if is_palindrome(words[i] + words[j]):
                result.append([i, j])
    
    return result
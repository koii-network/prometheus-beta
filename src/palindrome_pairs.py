def find_palindrome_pairs(words):
    """
    Find all pairs of indices in an array of strings where concatenated strings form a palindrome.
    
    Args:
        words (list): A list of strings to check for palindrome pairs
    
    Returns:
        list: A list of tuples containing index pairs that form palindromes
    
    Time Complexity: O(n^2 * k), where n is the number of words and k is the length of the longest word
    Space Complexity: O(1) excluding the output list
    """
    def is_palindrome(s):
        """Helper function to check if a string is a palindrome."""
        return s == s[::-1]
    
    palindrome_pairs = []
    
    # Check all possible pairs
    for i in range(len(words)):
        for j in range(len(words)):
            # Skip pairing a word with itself
            if i == j:
                continue
            
            # Check if concatenated strings form a palindrome
            concatenated = words[i] + words[j]
            if is_palindrome(concatenated):
                # Only add the pair if it's not a complex/trivial palindrome
                if len(words[i]) == len(words[j]) or \
                   len(words[i]) > len(words[j]) and \
                   is_palindrome(words[i][:len(words[i])-len(words[j])]) or \
                   len(words[j]) > len(words[i]) and \
                   is_palindrome(words[j][:len(words[j])-len(words[i])]):
                    palindrome_pairs.append((i, j))
    
    return palindrome_pairs
def can_divide_subsequences(s):
    """
    Determine if a string of lowercase English letters can be divided into subsequences 
    of at least 2 letters where each subsequence consists of either all vowels or all consonants.
    
    Args:
        s (str): A string of lowercase English letters
    
    Returns:
        bool: True if the string can be divided into valid subsequences, False otherwise
    """
    # Check if string is empty or too short
    if not s or len(s) < 2:
        return False
    
    # Define vowels and consonants
    vowels = set('aeiou')
    
    # Function to check if a sequence is valid (all vowels or all consonants)
    def is_valid_sequence(seq):
        return len(seq) >= 2 and (all(c in vowels for c in seq) or all(c not in vowels for c in seq))
    
    # Try all possible divisions
    def can_divide(index):
        # Base case: reached the end of the string
        if index == len(s):
            return True
        
        # Try subsequences of at least 2 letters
        for length in range(2, len(s) - index + 1):
            subsequence = s[index:index+length]
            if is_valid_sequence(subsequence):
                # Recursively check if the rest of the string can be divided
                if can_divide(index + length):
                    return True
        
        return False
    
    return can_divide(0)
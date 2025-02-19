def can_divide_subsequences(s: str) -> bool:
    """
    Determine if a string of lowercase English letters can be divided into subsequences 
    of at least 2 letters where each subsequence consists of either all vowels or all consonants.
    
    Args:
        s (str): Input string of lowercase English letters
    
    Returns:
        bool: True if the string can be divided as specified, False otherwise
    """
    # Check if the string is too short to divide
    if len(s) < 2:
        return False
    
    # Define vowels 
    vowels = set('aeiou')
    
    # Function to check if a subsequence is valid (all vowels or all consonants)
    def is_valid_subsequence(subsequence):
        return all(char in vowels for char in subsequence) or \
               all(char not in vowels for char in subsequence)
    
    # Try all possible ways to divide the string
    def backtrack(index):
        # Base case: reached the end of the string successfully
        if index == len(s):
            return True
        
        # Try subsequences of different lengths starting from current index
        for length in range(2, len(s) - index + 1):
            subsequence = s[index:index+length]
            
            # If this subsequence is valid, try dividing the rest of the string
            if is_valid_subsequence(subsequence):
                if backtrack(index + length):
                    return True
        
        return False
    
    return backtrack(0)
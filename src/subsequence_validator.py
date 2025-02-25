def can_divide_into_subsequences(s: str) -> bool:
    """
    Determine if a string of lowercase English letters can be divided into 
    subsequences of at least 2 letters where each subsequence is all vowels or all consonants.
    
    Args:
        s (str): Input string of lowercase English letters
    
    Returns:
        bool: True if the string can be divided into valid subsequences, False otherwise
    """
    # Check if string is too short to divide
    if len(s) < 2:
        return False
    
    # Define vowels and consonants
    vowels = set('aeiou')
    
    # Helper function to check if a subsequence is valid
    def is_valid_subsequence(subseq):
        return len(subseq) >= 2 and (
            all(c in vowels for c in subseq) or 
            all(c not in vowels for c in subseq)
        )
    
    # Try all possible ways to divide the string
    def backtrack(index):
        # Base case: reached the end of the string successfully
        if index == len(s):
            return True
        
        # Try subsequences starting from current index
        for end in range(index + 1, len(s) + 1):
            subseq = s[index:end]
            
            # Check if the current subsequence is valid 
            # and the rest of the string can be divided
            if is_valid_subsequence(subseq) and backtrack(end):
                return True
        
        return False
    
    return backtrack(0)
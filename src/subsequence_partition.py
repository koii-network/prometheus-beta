def can_partition_subsequences(s: str) -> bool:
    """
    Determine if a string of lowercase English letters can be divided into 
    subsequences of at least 2 letters where each subsequence consists of 
    either all vowels or all consonants.
    
    Args:
        s (str): Input string of lowercase English letters
    
    Returns:
        bool: True if the string can be partitioned, False otherwise
    """
    # Check for invalid input 
    if not s or len(s) < 2:
        return False
    
    # Define vowels and valid characters
    vowels = set('aeiou')
    
    # Helper function to check if a subsequence is valid 
    def is_valid_subsequence(substr):
        # Subsequence must be at least 2 letters
        if len(substr) < 2:
            return False
        
        # Check if all characters are vowels or all are consonants
        return all(c in vowels for c in substr) or all(c not in vowels for c in substr)
    
    # Recursively try all possible partitions
    def can_partition(remaining):
        # Base case: if string is empty, it's a valid partition
        if not remaining:
            return True
        
        # Try all possible subsequence lengths
        for i in range(2, len(remaining) + 1):
            subsequence = remaining[:i]
            
            # If this subsequence is valid, check if rest can be partitioned
            if is_valid_subsequence(subsequence):
                if can_partition(remaining[i:]):
                    return True
        
        return False
    
    return can_partition(s)
def can_divide_subsequences(s: str) -> bool:
    """
    Determine if a string can be divided into subsequences of at least 2 letters
    where each subsequence consists of either all vowels or all consonants.

    Args:
        s (str): A string of lowercase English letters

    Returns:
        bool: True if the string can be divided, False otherwise
    """
    # Check if the string is too short to divide
    if len(s) < 2:
        return False

    # Define vowels and consonants
    vowels = set('aeiou')
    
    def is_all_vowels(substring):
        return all(char in vowels for char in substring)
    
    def is_all_consonants(substring):
        return all(char not in vowels for char in substring)

    # Try all possible divisions
    def can_divide(index):
        # Base case: if we've reached the end of the string
        if index == len(s):
            return True
        
        # Try subsequences of at least 2 letters
        for length in range(2, len(s) - index + 1):
            subsequence = s[index:index+length]
            
            # Check if the subsequence is all vowels or all consonants
            if (is_all_vowels(subsequence) or is_all_consonants(subsequence)) and can_divide(index + length):
                return True
        
        return False

    return can_divide(0)
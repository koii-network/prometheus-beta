def generate_unique_permutations(s: str) -> list[str]:
    """
    Generate all possible unique permutations of a given string.
    
    Args:
        s (str): Input string to generate permutations from
    
    Returns:
        list[str]: A list of unique permutations of the input string
    
    Examples:
        >>> generate_unique_permutations('abc')
        ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']
        >>> generate_unique_permutations('aab')
        ['aab', 'aba', 'baa']
    """
    # Convert string to list for easier manipulation
    chars = list(s)
    
    # Use a set to store unique permutations
    permutations = set()
    
    def backtrack(start: int):
        # Base case: if we've reached the end of the string
        if start == len(chars):
            permutations.add(''.join(chars))
            return
        
        # Try swapping current character with each subsequent character
        for i in range(start, len(chars)):
            # Swap characters
            chars[start], chars[i] = chars[i], chars[start]
            
            # Recursively generate permutations for the rest of the string
            backtrack(start + 1)
            
            # Backtrack to restore original order
            chars[start], chars[i] = chars[i], chars[start]
    
    # Start the backtracking process
    backtrack(0)
    
    # Return sorted list of unique permutations for consistent output
    return sorted(list(permutations))
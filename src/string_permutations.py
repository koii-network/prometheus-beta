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
        >>> generate_unique_permutations('aba')
        ['aba', 'aab', 'baa']
    """
    # Convert string to list for easier manipulation
    chars = list(s)
    
    # Handle base cases
    if len(chars) <= 1:
        return [s]
    
    # Use set to store unique permutations
    unique_permutations = set()
    
    def backtrack(start: int):
        # Base case: if we've reached the end of the string
        if start == len(chars) - 1:
            unique_permutations.add(''.join(chars))
            return
        
        # Try swapping current character with each subsequent character
        for i in range(start, len(chars)):
            # Swap characters
            chars[start], chars[i] = chars[i], chars[start]
            
            # Recursively generate permutations
            backtrack(start + 1)
            
            # Backtrack to restore original order
            chars[start], chars[i] = chars[i], chars[start]
    
    # Start backtracking
    backtrack(0)
    
    # Convert set to sorted list for consistent output
    return sorted(list(unique_permutations))
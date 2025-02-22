def generate_unique_permutations(s):
    """
    Generate all possible unique permutations of a given string.
    
    Args:
        s (str): Input string to generate permutations for
    
    Returns:
        list: A list of unique permutations of the input string
    """
    # Convert string to list for easier manipulation
    chars = list(s)
    
    # Use a set to store unique permutations
    unique_permutations = set()
    
    def backtrack(start):
        # Base case: if we've reached the end of the string
        if start == len(chars) - 1:
            unique_permutations.add(''.join(chars))
            return
        
        # Try swapping current character with each subsequent character
        for i in range(start, len(chars)):
            # Swap characters
            chars[start], chars[i] = chars[i], chars[start]
            
            # Recursively generate permutations for the rest of the string
            backtrack(start + 1)
            
            # Backtrack: restore the original order
            chars[start], chars[i] = chars[i], chars[start]
    
    # Start the backtracking process
    backtrack(0)
    
    # Convert set back to sorted list for consistent output
    return sorted(list(unique_permutations))
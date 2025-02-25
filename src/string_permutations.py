def generate_unique_permutations(s: str) -> list[str]:
    """
    Generate all unique permutations of a given string.
    
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
    # Handle edge cases
    if not isinstance(s, str):
        raise TypeError("Input must be a string")
    
    # Use a set to ensure uniqueness
    unique_permutations = set()
    
    def backtrack(current_perm, remaining_chars):
        # Base case: if no remaining characters, add to permutations
        if not remaining_chars:
            unique_permutations.add(current_perm)
            return
        
        # Try each remaining character as the next character
        for i in range(len(remaining_chars)):
            # Choose
            new_perm = current_perm + remaining_chars[i]
            new_remaining = remaining_chars[:i] + remaining_chars[i+1:]
            
            # Explore
            backtrack(new_perm, new_remaining)
    
    # Start the backtracking process
    backtrack('', s)
    
    # Convert set to sorted list for consistent output
    return sorted(list(unique_permutations))
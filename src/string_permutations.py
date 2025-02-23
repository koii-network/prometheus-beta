def generate_unique_permutations(input_string):
    """
    Generate all possible unique permutations of a given string.
    
    Args:
        input_string (str): The input string to generate permutations for.
    
    Returns:
        list: A list of unique permutations of the input string.
    
    Raises:
        TypeError: If input is not a string.
        ValueError: If input is an empty string.
    """
    # Validate input
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    if not input_string:
        raise ValueError("Input string cannot be empty")
    
    # Convert to list of characters to handle permutations
    chars = list(input_string)
    
    # Use a set to store unique permutations
    unique_permutations = set()
    
    def backtrack(start):
        """
        Recursive backtracking to generate unique permutations.
        
        Args:
            start (int): Starting index for permutation generation.
        """
        # If we've reached the end of the list, add the current permutation
        if start == len(chars):
            unique_permutations.add(''.join(chars))
            return
        
        # Generate permutations by swapping elements
        for i in range(start, len(chars)):
            # Swap characters
            chars[start], chars[i] = chars[i], chars[start]
            
            # Recursively generate permutations for the rest of the string
            backtrack(start + 1)
            
            # Backtrack (undo the swap)
            chars[start], chars[i] = chars[i], chars[start]
    
    # Start the backtracking process
    backtrack(0)
    
    # Convert set to sorted list for consistent output
    return sorted(list(unique_permutations))
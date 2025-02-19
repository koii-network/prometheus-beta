def generate_unique_permutations(input_string):
    """
    Generate all possible unique permutations of a given string.
    
    Args:
        input_string (str): The input string to generate permutations for.
    
    Returns:
        list: A list of unique permutations of the input string.
    """
    # Handle edge cases
    if not input_string:
        return []
    
    # Convert to list to handle duplicate characters
    char_list = list(input_string)
    
    # Use a set to store unique permutations
    unique_permutations = set()
    
    def backtrack(start):
        # Base case: if we've reached the end of the list
        if start == len(char_list):
            unique_permutations.add(''.join(char_list))
        
        # Try swapping current element with each subsequent element
        for i in range(start, len(char_list)):
            # Swap elements
            char_list[start], char_list[i] = char_list[i], char_list[start]
            
            # Recurse to generate permutations
            backtrack(start + 1)
            
            # Backtrack (undo the swap)
            char_list[start], char_list[i] = char_list[i], char_list[start]
    
    # Start the backtracking process
    backtrack(0)
    
    # Convert set to sorted list for consistent output
    return sorted(list(unique_permutations))
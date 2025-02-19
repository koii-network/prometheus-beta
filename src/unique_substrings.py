def get_unique_substrings(input_string):
    """
    Returns an array of all unique substrings within the given input string.
    
    Args:
        input_string (str): The input string to extract unique substrings from.
    
    Returns:
        list: A list of unique substrings.
    """
    # Handle edge cases
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    if not input_string:
        return []
    
    # Set to store unique substrings
    unique_substrings = set()
    
    # Generate all possible substrings
    for i in range(len(input_string)):
        for j in range(i + 1, len(input_string) + 1):
            unique_substrings.add(input_string[i:j])
    
    # Convert set to sorted list for consistent output
    return sorted(list(unique_substrings))
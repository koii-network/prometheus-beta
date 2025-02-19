def get_unique_substrings(input_string):
    """
    Returns an array of all unique substrings within the input string.
    
    Args:
        input_string (str): The input string to extract substrings from.
    
    Returns:
        list: A list of unique substrings.
    """
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    # If input is an empty string, return an empty list
    if not input_string:
        return []
    
    # Use a set to store unique substrings
    unique_substrings = set()
    
    # Generate all possible substrings
    for start in range(len(input_string)):
        for end in range(start + 1, len(input_string) + 1):
            unique_substrings.add(input_string[start:end])
    
    # Convert set to sorted list for consistent output
    return sorted(list(unique_substrings))
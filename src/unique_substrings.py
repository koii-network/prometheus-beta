def get_unique_substrings(input_string):
    """
    Generate an array of all unique substrings within the input string.
    
    Args:
        input_string (str): The input string to extract substrings from.
    
    Returns:
        list: A list of unique substrings, sorted alphabetically.
    
    Raises:
        TypeError: If input is not a string.
    
    Examples:
        >>> get_unique_substrings("abc")
        ['a', 'ab', 'abc', 'b', 'bc', 'c']
        >>> get_unique_substrings("")
        []
    """
    # Validate input
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    # If input is empty, return empty list
    if not input_string:
        return []
    
    # Generate all possible substrings
    unique_substrings = set()
    for start in range(len(input_string)):
        for end in range(start + 1, len(input_string) + 1):
            unique_substrings.add(input_string[start:end])
    
    # Return sorted list of unique substrings
    return sorted(list(unique_substrings))
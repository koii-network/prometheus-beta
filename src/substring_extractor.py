def extract_all_substrings(input_string):
    """
    Extract all possible substrings from the given input string.
    
    Args:
        input_string (str): The input string to extract substrings from.
    
    Returns:
        list: A list of all possible substrings of the input string.
    
    Examples:
        >>> extract_all_substrings("abc")
        ['a', 'ab', 'abc', 'b', 'bc', 'c']
        >>> extract_all_substrings("")
        []
        >>> extract_all_substrings("x")
        ['x']
    """
    # Handle edge case of empty string
    if not input_string:
        return []
    
    # Use list comprehension to generate all substrings
    substrings = []
    for start in range(len(input_string)):
        for end in range(start + 1, len(input_string) + 1):
            substrings.append(input_string[start:end])
    
    return substrings
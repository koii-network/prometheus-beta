def generate_substrings(input_string):
    """
    Generate all possible substrings from the input string.
    
    Args:
        input_string (str): The input string to generate substrings from.
    
    Returns:
        list: A list of all possible substrings.
    
    Examples:
        >>> generate_substrings('abc')
        ['a', 'ab', 'abc', 'b', 'bc', 'c']
        >>> generate_substrings('')
        []
    """
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    substrings = []
    for start in range(len(input_string)):
        for end in range(start + 1, len(input_string) + 1):
            substrings.append(input_string[start:end])
    
    return substrings
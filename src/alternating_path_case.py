def to_alternating_path_case(input_string):
    """
    Convert a string to alternating path case.
    
    Args:
        input_string (str): The input string to convert.
    
    Returns:
        str: The string converted to alternating path case.
    
    Examples:
        >>> to_alternating_path_case("hello world")
        'hello-World'
        >>> to_alternating_path_case("python programming")
        'python-Programming'
        >>> to_alternating_path_case("")
        ''
    """
    if not input_string:
        return ""
    
    words = input_string.split()
    result = words[0].lower()
    
    for word in words[1:]:
        result += "-" + word.capitalize()
    
    return result
def convert_to_alternating_snake_case(text: str) -> str:
    """
    Convert a string to alternating snake case.
    
    Args:
        text (str): The input string to convert.
    
    Returns:
        str: The string converted to alternating snake case.
    
    Examples:
        >>> convert_to_alternating_snake_case("hello world")
        'hello_WORLD'
        >>> convert_to_alternating_snake_case("Python is AWESOME")
        'python_IS_awesome'
    """
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    
    if not text:
        return ""
    
    words = text.split()
    result = []
    
    for i, word in enumerate(words):
        # Alternate between lowercase and uppercase for words
        converted_word = word.lower() if i % 2 == 0 else word.upper()
        result.append(converted_word)
    
    return '_'.join(result)
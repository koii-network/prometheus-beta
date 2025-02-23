def to_alternating_camel_case(text: str) -> str:
    """
    Convert a string to alternating camel case.
    
    In alternating camel case, the first character is lowercase, 
    and subsequent words start with alternating cases.
    
    Args:
        text (str): The input string to convert.
    
    Returns:
        str: The string converted to alternating camel case.
    
    Raises:
        TypeError: If input is not a string.
    
    Examples:
        >>> to_alternating_camel_case("hello world")
        'helloWorld'
        >>> to_alternating_camel_case("PYTHON IS AWESOME")
        'pythonIsAwesome'
        >>> to_alternating_camel_case("python-programming-language")
        'pythonProgrammingLanguage'
    """
    # Check input type
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    
    # Remove non-alphanumeric characters and split
    words = ''.join(char if char.isalnum() or char.isspace() else ' ' for char in text).split()
    
    # Handle empty input
    if not words:
        return ''
    
    # Convert to alternating camel case
    result = words[0].lower()
    for word in words[1:]:
        result += word.capitalize()
    
    return result
def convert_to_camel_case(text):
    """
    Convert a string to camel case.
    
    Args:
        text (str): Input string to convert to camel case.
    
    Returns:
        str: The input string converted to camel case.
    
    Examples:
        >>> convert_to_camel_case("hello world")
        'helloWorld'
        >>> convert_to_camel_case("Hello-World")
        'helloWorld'
        >>> convert_to_camel_case("hello_world")
        'helloWorld'
    """
    # Check if the string is already in camel case and only contains alphanumeric characters
    if text and all(c.isalnum() for c in text) and text[0].islower() and any(c.isupper() for c in text[1:]):
        return text
    
    # Remove special characters and split the string by spaces, hyphens, or underscores
    words = ''.join(char if char.isalnum() else ' ' for char in text).split()
    
    # Capitalize all words except the first one, and join them together
    if not words:
        return ''
    
    return words[0].lower() + ''.join(word.capitalize() for word in words[1:])
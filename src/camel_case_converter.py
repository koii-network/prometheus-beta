def convert_to_camel_case(text: str) -> str:
    """
    Convert a string to camel case.
    
    Args:
        text (str): Input string to convert.
    
    Returns:
        str: Camel case version of the input string.
    
    Examples:
        - 'hello world' -> 'helloWorld'
        - 'hello-world' -> 'helloWorld'
        - 'hello_world' -> 'helloWorld'
        - 'Hello World' -> 'helloWorld'
    """
    # Handle empty or None input
    if not text:
        return ''
    
    # Replace non-alphanumeric characters with spaces
    import re
    words = re.sub(r'[^a-zA-Z0-9]', ' ', text).split()
    
    # If no words, return empty string
    if not words:
        return ''
    
    # Convert to camel case
    return words[0].lower() + ''.join(word.capitalize() for word in words[1:])
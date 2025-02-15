def capitalize_words(text: str) -> str:
    """
    Capitalize the first letter of each word in a given string.
    
    Args:
        text (str): The input string to capitalize.
    
    Returns:
        str: A string with the first letter of each word capitalized.
    
    Examples:
        >>> capitalize_words("hello world")
        'Hello World'
        >>> capitalize_words("python is awesome")
        'Python Is Awesome'
        >>> capitalize_words("")
        ''
    """
    if not text:
        return ""
    
    return ' '.join(word.capitalize() for word in text.split())
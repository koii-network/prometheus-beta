def capitalize_words(input_string: str) -> str:
    """
    Capitalize the first letter of each word in a given string.

    Args:
        input_string (str): The input string to be transformed.

    Returns:
        str: A new string with the first letter of each word capitalized.

    Examples:
        >>> capitalize_words("hello world")
        'Hello World'
        >>> capitalize_words("python programming is fun")
        'Python Programming Is Fun'
        >>> capitalize_words("")
        ''
        >>> capitalize_words("a")
        'A'
    """
    # Handle edge cases
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    # Split the string into words, capitalize each word, then join back
    return ' '.join(word.capitalize() for word in input_string.split())
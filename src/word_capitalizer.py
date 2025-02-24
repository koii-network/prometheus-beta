def capitalize_words(input_string: str) -> str:
    """
    Capitalize the first letter of each word in a given string.

    Args:
        input_string (str): The input string to be processed.

    Returns:
        str: A new string with the first letter of each word capitalized.

    Examples:
        >>> capitalize_words("hello world")
        'Hello World'
        >>> capitalize_words("python programming language")
        'Python Programming Language'
        >>> capitalize_words("")
        ''
        >>> capitalize_words("a")
        'A'
    """
    # Handle empty string case
    if not input_string:
        return input_string
    
    # Split the string into words and capitalize first letter of each
    return ' '.join(word.capitalize() for word in input_string.split())
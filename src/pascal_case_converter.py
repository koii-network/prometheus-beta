def to_pascal_case(text: str) -> str:
    """
    Convert a given string to PascalCase.
    
    Args:
        text (str): Input string to convert
    
    Returns:
        str: PascalCase version of the input string
    
    Examples:
        >>> to_pascal_case("hello world")
        'HelloWorld'
        >>> to_pascal_case("user_name")
        'UserName'
        >>> to_pascal_case("hello-world")
        'HelloWorld'
    """
    # Remove special characters and replace them with spaces
    cleaned_text = ''.join(
        char if char.isalnum() else ' ' for char in text
    )
    
    # Split the string into words and capitalize each word
    words = cleaned_text.split()
    pascal_case_words = [word.capitalize() for word in words]
    
    # Join the words without spaces
    return ''.join(pascal_case_words)
def to_pascal_case(input_string: str) -> str:
    """
    Convert a given string to Pascal case.
    
    Args:
        input_string (str): The input string to convert.
    
    Returns:
        str: The input string converted to Pascal case.
    
    Examples:
        >>> to_pascal_case("hello world")
        'HelloWorld'
        >>> to_pascal_case("snake_case_example")
        'SnakeCaseExample'
        >>> to_pascal_case("kebab-case-example")
        'KebabCaseExample'
    """
    # Split the string by non-alphanumeric characters
    words = ''.join(char if char.isalnum() else ' ' for char in input_string).split()
    
    # Capitalize first letter of each word and join
    return ''.join(word.capitalize() for word in words)
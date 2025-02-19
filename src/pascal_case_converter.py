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
    def custom_split(s):
        # Custom splitting that keeps numbers with words
        result = []
        current_word = []
        for char in s:
            if char.isalnum():
                current_word.append(char)
            else:
                if current_word:
                    result.append(''.join(current_word))
                    current_word = []
        if current_word:
            result.append(''.join(current_word))
        return result

    # Remove special characters and split into words
    words = custom_split(''.join(char if char.isalnum() or char.isspace() else ' ' for char in input_string))
    
    # Capitalize first letter of each word
    return ''.join(word[0].upper() + word[1:] for word in words)
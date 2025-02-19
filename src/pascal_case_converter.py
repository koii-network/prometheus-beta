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
    def capitalize_word(word):
        # Special handling for words that have numbers
        if not word.isalpha():
            # Find the first letter and capitalize it
            first_letter_index = next((i for i, char in enumerate(word) if char.isalpha()), None)
            if first_letter_index is not None:
                return word[:first_letter_index] + word[first_letter_index].upper() + word[first_letter_index+1:]
        return word.capitalize()

    # Split the string by non-alphanumeric characters
    words = ''.join(char if char.isalnum() else ' ' for char in input_string).split()
    
    # Capitalize words
    return ''.join(capitalize_word(word) for word in words)
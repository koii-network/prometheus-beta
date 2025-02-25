def to_pascal_case(input_string: str) -> str:
    """
    Convert a given string to Pascal case.
    
    Pascal case is a naming convention where the first letter of each word is capitalized,
    and there are no separators between words.
    
    Args:
        input_string (str): The input string to convert to Pascal case.
    
    Returns:
        str: The input string converted to Pascal case.
    
    Raises:
        TypeError: If the input is not a string.
    
    Examples:
        >>> to_pascal_case("hello world")
        'HelloWorld'
        >>> to_pascal_case("hello_world")
        'HelloWorld'
        >>> to_pascal_case("hello-world")
        'HelloWorld'
    """
    # Check if input is a string
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    # If the input is empty, return an empty string
    if not input_string:
        return ""
    
    # Replace common separators with a space and handle potential mixed case
    for separator in ['-', '_', ' ']:
        input_string = input_string.replace(separator, ' ')
    
    # Split the string into words, handling mixed case first
    words = []
    current_word = input_string[0].upper()
    for char in input_string[1:]:
        if char.isupper():
            # Start a new word when an uppercase letter is found
            words.append(current_word)
            current_word = char
        else:
            current_word += char
    
    # Add the last word
    words.append(current_word)
    
    # Capitalize each word and join
    pascal_words = [word.capitalize() for word in words]
    
    return ''.join(pascal_words)
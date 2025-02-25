def convert_to_header_case(input_string):
    """
    Convert a given string to header case.
    
    Header case is where the first letter of each word is capitalized,
    and words are separated by spaces.
    
    Args:
        input_string (str): The input string to convert.
    
    Returns:
        str: The string converted to header case.
    
    Raises:
        TypeError: If the input is not a string.
    
    Examples:
        >>> convert_to_header_case("hello world")
        'Hello World'
        >>> convert_to_header_case("hello_world")
        'Hello World'
        >>> convert_to_header_case("hello-world")
        'Hello World'
        >>> convert_to_header_case("helloWorld")
        'Hello World'
    """
    # Check input type
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    # Handle empty string
    if not input_string:
        return ""
    
    # Replace various separators with a single space
    # This handles snake_case, kebab-case, and camelCase
    normalized = input_string.replace('_', ' ').replace('-', ' ')
    
    # Split the string and capitalize each word
    words = []
    current_word = ""
    for char in normalized:
        # Handle camelCase by inserting spaces before capital letters
        if char.isupper() and current_word:
            words.append(current_word)
            current_word = char
        else:
            current_word += char.lower()
    
    # Add the last word
    if current_word:
        words.append(current_word)
    
    # Capitalize the first letter of each word and join
    return ' '.join(word.capitalize() for word in words)
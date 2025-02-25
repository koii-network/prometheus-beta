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
    
    # Normalize the string by replacing different separators
    normalized = input_string.replace('_', ' ').replace('-', ' ')
    
    # Function to determine word boundaries and capitalize
    def split_and_capitalize(s):
        words = []
        current_word = ""
        for i, char in enumerate(s):
            # Detect camel case and split
            if char.isupper() and current_word and not current_word[-1].isupper():
                words.append(current_word)
                current_word = char
            # Handle consecutive uppercase letters
            elif char.isupper() and current_word and current_word[-1].isupper():
                current_word += char
            else:
                current_word += char.lower()
        
        # Add the last word
        if current_word:
            words.append(current_word)
        
        # Capitalize each word and handle consecutive spaces
        return [word.capitalize() for word in words]
    
    # Split normalized string and capitalize
    words = []
    for part in normalized.split():
        words.extend(split_and_capitalize(part))
    
    # Join the words
    return ' '.join(words)
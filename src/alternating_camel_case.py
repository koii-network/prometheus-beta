def to_alternating_camel_case(input_string):
    """
    Convert a string to alternating camel case.
    
    Args:
        input_string (str): The input string to convert.
    
    Returns:
        str: The string converted to alternating camel case.
    
    Raises:
        TypeError: If input is not a string.
    """
    # Validate input is a string
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    # Handle empty string case
    if not input_string:
        return ""
    
    # Remove non-alphanumeric characters and split into words
    words = ''.join(char if char.isalnum() or char.isspace() else ' ' for char in input_string).split()
    
    # If no words, return empty string
    if not words:
        return ""
    
    # Convert to alternating camel case
    result = words[0].lower()
    for i, word in enumerate(words[1:], 1):
        # Alternate between lowercase and uppercase
        if i % 2 == 1:
            result += word.title()
        else:
            result += word.lower()
    
    return result
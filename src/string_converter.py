def to_constant_case(input_string: str) -> str:
    """
    Convert a given string to constant case (UPPERCASE_WITH_UNDERSCORES).
    
    Args:
        input_string (str): The input string to be converted.
    
    Returns:
        str: The string converted to constant case.
    
    Raises:
        TypeError: If the input is not a string.
    
    Examples:
        >>> to_constant_case("hello world")
        'HELLO_WORLD'
        >>> to_constant_case("camelCaseString")
        'CAMEL_CASE_STRING'
        >>> to_constant_case("snake_case_string")
        'SNAKE_CASE_STRING'
    """
    # Check if input is a string
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    # If input is empty, return empty string
    if not input_string:
        return ""
    
    # Prepare a list to hold our constant case characters
    converted_chars = []
    
    # Iterate through characters in the input string
    for i, char in enumerate(input_string):
        # Replace non-alphanumeric characters with underscore
        if not char.isalnum():
            converted_chars.append('_')
            continue
        
        # Handle camel case by inserting underscore 
        # when transitioning from lower to upper case
        # or between consecutive non-uppercase characters
        if (i > 0 and 
            ((char.isupper() and input_string[i-1].islower()) or 
             (i > 1 and not input_string[i-1].isupper() and not char.isupper()))):
            converted_chars.append('_')
        
        # Always convert to uppercase
        converted_chars.append(char.upper())
    
    # Join the characters, remove consecutive underscores, 
    # and strip leading/trailing underscores
    result = '_'.join(filter(bool, ''.join(converted_chars).split('_')))
    
    return result
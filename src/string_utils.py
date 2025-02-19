def convert_to_uppercase_with_spaces(input_string):
    """
    Convert a string to uppercase with spaces between words.
    
    Args:
        input_string (str): The input string to be converted.
    
    Returns:
        str: The input string converted to uppercase with spaces between words.
    
    Raises:
        TypeError: If the input is not a string.
    """
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    # Remove existing spaces and convert to uppercase
    cleaned_string = input_string.replace(' ', '')
    
    # Insert spaces before capital letters (except the first letter)
    result = cleaned_string[0]
    for char in cleaned_string[1:]:
        if char.isupper():
            result += ' '
        result += char
    
    return result.upper()
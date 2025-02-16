def convert_to_uppercase_with_spaces(input_string):
    """
    Convert a string to uppercase, adding spaces between words.
    
    Args:
        input_string (str): The input string to convert.
    
    Returns:
        str: The converted string in uppercase with spaces.
    
    Raises:
        TypeError: If the input is not a string.
    """
    # Check if input is a string
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    # Remove existing spaces and convert to uppercase
    cleaned_string = input_string.replace(' ', '')
    
    # Add spaces before capital letters (except the first letter)
    uppercase_with_spaces = cleaned_string[0]
    for char in cleaned_string[1:]:
        if char.isupper():
            uppercase_with_spaces += ' '
        uppercase_with_spaces += char
    
    return uppercase_with_spaces.upper()
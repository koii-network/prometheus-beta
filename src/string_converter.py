def convert_to_upper_case_with_spaces(input_string):
    """
    Convert a string to upper case, adding spaces between words.
    
    Args:
        input_string (str): The input string to convert
    
    Returns:
        str: The converted string in upper case with spaces
    
    Raises:
        TypeError: If input is not a string
    """
    # Check if input is a string
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    # Remove existing spaces and convert to upper case
    cleaned_string = input_string.replace(' ', '')
    
    # Add spaces before capital letters (except the first letter)
    result = cleaned_string[0]
    for char in cleaned_string[1:]:
        if char.isupper():
            result += ' '
        result += char
    
    return result.upper()
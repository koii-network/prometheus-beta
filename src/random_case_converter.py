import random

def convert_to_random_case(input_string):
    """
    Convert a string to alternating random case.
    
    Args:
        input_string (str): The input string to convert.
    
    Returns:
        str: A new string with characters randomly converted to upper or lower case.
    
    Raises:
        TypeError: If input is not a string.
    """
    # Check if input is a string
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    # If string is empty, return empty string
    if not input_string:
        return ""
    
    # Convert to alternating random case
    random_case_chars = []
    for char in input_string:
        # Randomly choose to convert to upper or lower case
        if random.choice([True, False]):
            random_case_chars.append(char.upper())
        else:
            random_case_chars.append(char.lower())
    
    return ''.join(random_case_chars)
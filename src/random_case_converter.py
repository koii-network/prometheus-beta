import random

def convert_to_alternating_random_case(input_string):
    """
    Convert a string to alternating random case.
    
    Args:
        input_string (str): The input string to convert.
    
    Returns:
        str: A new string with characters in alternating random case.
    
    Raises:
        TypeError: If input is not a string.
    """
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    # If input is empty, return empty string
    if not input_string:
        return ""
    
    result = []
    for char in input_string:
        # Randomly choose between upper and lower case
        if random.choice([True, False]):
            result.append(char.upper())
        else:
            result.append(char.lower())
    
    return ''.join(result)
import random

def convert_to_alternating_random_case(input_string):
    """
    Convert a string to alternating random case.
    
    Args:
        input_string (str): The input string to be converted.
    
    Returns:
        str: A new string with characters converted to alternating random case.
    
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
    result = []
    for char in input_string:
        # Randomly choose between upper and lower case
        if random.choice([True, False]):
            result.append(char.upper())
        else:
            result.append(char.lower())
    
    return ''.join(result)
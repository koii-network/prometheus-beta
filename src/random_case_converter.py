import random

def convert_to_random_case(input_string):
    """
    Convert a string to alternating random case.
    
    Args:
        input_string (str): The input string to convert.
    
    Returns:
        str: A string with characters randomly converted to upper or lower case.
    
    Raises:
        TypeError: If input is not a string.
    """
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    return ''.join(
        char.upper() if random.choice([True, False]) else char.lower() 
        for char in input_string
    )
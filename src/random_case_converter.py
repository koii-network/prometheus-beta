import random

def convert_to_random_case(input_string):
    """
    Convert a string to alternating random case.
    
    Args:
        input_string (str): The input string to convert.
    
    Returns:
        str: A new string with characters converted to random case.
    
    Raises:
        TypeError: If input is not a string.
    """
    # Check if input is a string
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    # If input is empty, return empty string
    if not input_string:
        return ""
    
    # Convert to random case
    random_case_string = ''.join(
        char.upper() if random.choice([True, False]) else char.lower() 
        for char in input_string
    )
    
    return random_case_string
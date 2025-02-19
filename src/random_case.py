import random

def convert_to_random_case(input_string):
    """
    Convert a given string to random case (uppercase or lowercase) for each character.
    
    Args:
        input_string (str): The input string to be converted to random case.
    
    Returns:
        str: A new string with characters randomly converted to upper or lowercase.
    
    Raises:
        TypeError: If the input is not a string.
    """
    # Validate input is a string
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    # Convert the string to random case
    return ''.join(
        char.upper() if random.choice([True, False]) else char.lower() 
        for char in input_string
    )
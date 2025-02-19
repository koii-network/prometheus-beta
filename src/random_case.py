import random

def convert_to_random_case(input_string):
    """
    Convert a given string to random case, where each character 
    has an equal chance of being uppercase or lowercase.
    
    Args:
        input_string (str): The input string to convert.
    
    Returns:
        str: A new string with randomly capitalized characters.
    
    Raises:
        TypeError: If the input is not a string.
    """
    # Check if input is a string
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    # Convert to random case
    return ''.join(
        char.upper() if random.random() < 0.5 else char.lower() 
        for char in input_string
    )
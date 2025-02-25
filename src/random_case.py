import random

def convert_to_random_case(input_string):
    """
    Convert a given string to random case, where each character 
    has an equal chance of being uppercase or lowercase.
    
    Args:
        input_string (str): The input string to convert
    
    Returns:
        str: A new string with randomly cased characters
    
    Raises:
        TypeError: If input is not a string
    """
    # Check if input is a string
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    # Use list comprehension to randomly case each character
    return ''.join(
        char.upper() if random.choice([True, False]) else char.lower() 
        for char in input_string
    )
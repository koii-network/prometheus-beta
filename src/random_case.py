import random

def convert_to_random_case(input_string):
    """
    Convert a given string to random case, preserving non-alphabetic characters.
    
    Args:
        input_string (str): The input string to convert to random case.
    
    Returns:
        str: A string with random uppercase and lowercase characters.
    
    Examples:
        >>> convert_to_random_case("Hello World!")
        Could return something like "hElLo wOrLd!"
    """
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    return ''.join(
        char.upper() if random.choice([True, False]) else char.lower() 
        if char.isalpha() 
        else char 
        for char in input_string
    )
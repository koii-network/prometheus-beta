import random

def convert_to_random_case(input_string):
    """
    Convert a given string to random case, preserving non-alphabetic characters.
    
    Args:
        input_string (str): The input string to be converted to random case.
    
    Returns:
        str: A new string with each alphabetic character randomly converted 
             to uppercase or lowercase.
    
    Raises:
        TypeError: If the input is not a string.
    
    Examples:
        >>> convert_to_random_case("Hello World!")
        Possible outputs like "hElLo wOrLd!" or "HeLlo WoRld!"
        >>> convert_to_random_case("")
        ""
    """
    # Check input type
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    # Convert each character to random case
    return ''.join(
        char.upper() if random.choice([True, False]) else char.lower() 
        if char.isalpha() 
        else char 
        for char in input_string
    )
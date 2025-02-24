import re
from typing import List


def extract_numbers(input_string: str) -> List[str]:
    """
    Extract all numbers from a given string.

    This function uses regex to find all numeric sequences in the input string.
    It supports:
    - Positive and negative integers
    - Floating-point numbers
    - Scientific notation
    - Numbers separated by non-numeric characters

    Args:
        input_string (str): The string to extract numbers from

    Returns:
        List[str]: A list of extracted numbers as strings

    Examples:
        >>> extract_numbers("I have 42 apples and -17.5 oranges")
        ['42', '-17.5']
        >>> extract_numbers("Temperature: 98.6°F, Altitude: -500.25m")
        ['98.6', '-500.25']
        >>> extract_numbers("No numbers here")
        []
    """
    # Regex pattern to match:
    # - Optional negative sign
    # - Digits before decimal point
    # - Optional decimal point and digits after
    # - Optional scientific notation
    pattern = r'-?\d+(?:\.\d+)?(?:[eE][-+]?\d+)?'
    
    # Find all matches and return as a list of strings
    return re.findall(pattern, input_string)
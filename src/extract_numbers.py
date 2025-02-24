import re
from typing import List

def extract_numbers(input_string: str) -> List[str]:
    """
    Extract numbers from a given string.

    This function finds and returns all numeric sequences in the input string.
    It supports integers and decimal numbers.

    Args:
        input_string (str): The string to extract numbers from.

    Returns:
        List[str]: A list of number strings found in the input.

    Examples:
        >>> extract_numbers("I have 42 apples and 3.14 pies")
        ['42', '3.14']
        >>> extract_numbers("No numbers here")
        []
    """
    # Use regex to find all numbers (integers and decimals)
    # The pattern matches:
    # - Optional negative sign
    # - One or more digits
    # - Optional decimal point followed by one or more digits
    numbers = re.findall(r'-?\d+(?:\.\d+)?', input_string)
    return numbers
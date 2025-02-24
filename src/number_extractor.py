import re
from typing import List

def extract_numbers(input_string: str) -> List[int]:
    """
    Extract all integers from a given string.

    Args:
        input_string (str): The input string to extract numbers from.

    Returns:
        List[int]: A list of integers found in the string.

    Examples:
        >>> extract_numbers("I have 42 apples and 7 oranges")
        [42, 7]
        >>> extract_numbers("No numbers here")
        []
        >>> extract_numbers("Negative numbers like -15 and 20")
        [-15, 20]
    """
    # Use regex to find all integers, including negative numbers
    numbers = re.findall(r'-?\d+', input_string)
    
    # Convert found strings to integers
    return [int(num) for num in numbers]
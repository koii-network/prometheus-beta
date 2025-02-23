import re
from typing import List, Union

def extract_numbers(input_string: str) -> List[Union[int, float]]:
    """
    Extract all numbers (integers and floats) from a given string.

    Args:
        input_string (str): The input string to extract numbers from.

    Returns:
        List[Union[int, float]]: A list of extracted numbers.

    Examples:
        >>> extract_numbers("I have 42 apples and 3.14 pies")
        [42, 3.14]
        >>> extract_numbers("No numbers here")
        []
        >>> extract_numbers("-10 and 20.5")
        [-10, 20.5]
    """
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")

    # Regular expression to match integers and floating-point numbers (including negative numbers)
    number_pattern = r'-?\d+(?:\.\d+)?'
    
    # Find all number matches and convert them to appropriate numeric type
    numbers = []
    for match in re.finditer(number_pattern, input_string):
        num_str = match.group()
        # Convert to int if no decimal, otherwise to float
        numbers.append(int(num_str) if num_str.isdigit() or (num_str.startswith('-') and num_str[1:].isdigit()) 
                      else float(num_str))
    
    return numbers
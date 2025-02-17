import re

def extract_numbers(input_string):
    """
    Extract all numbers from a given string.
    
    Args:
        input_string (str): The input string to extract numbers from.
    
    Returns:
        list: A list of extracted numbers as strings.
    
    Raises:
        TypeError: If input is not a string.
    """
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    # Use regex to find all numbers (including negative and decimal numbers)
    numbers = re.findall(r'-?\d+(?:\.\d+)?', input_string)
    
    return numbers
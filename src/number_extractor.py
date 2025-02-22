import re

def extract_numbers(input_string):
    """
    Extract all numbers from a given input string.
    
    Args:
        input_string (str): The string to extract numbers from.
    
    Returns:
        list: A list of numbers (as strings) found in the input string.
    
    Raises:
        TypeError: If the input is not a string.
    """
    # Check if input is a string
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    # Use regex to find all numbers (including negative and decimal numbers)
    numbers = re.findall(r'-?\d+(?:\.\d+)?', input_string)
    
    return numbers
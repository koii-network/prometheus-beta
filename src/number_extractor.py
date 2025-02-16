import re

def extract_numbers(input_string):
    """
    Extract all numbers (integers and decimals) from a given string.
    
    Args:
        input_string (str): The string to extract numbers from.
    
    Returns:
        list: A list of numbers (integers or floats) found in the string.
    """
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    # Use regex to find integers and decimal numbers
    numbers = re.findall(r'-?\d+(?:\.\d+)?', input_string)
    
    # Convert found strings to appropriate numeric type (int or float)
    return [float(num) if '.' in num else int(num) for num in numbers]
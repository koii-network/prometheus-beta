import re

def extract_numbers_from_string(input_string):
    """
    Extract all numbers from a given string.
    
    Args:
        input_string (str): The input string to extract numbers from.
    
    Returns:
        list: A list of numbers (integers or floats) found in the string.
    """
    # Use regex to find all numbers (including integers and floats)
    numbers = re.findall(r'-?\d+(?:\.\d+)?', str(input_string))
    
    # Convert extracted strings to appropriate numeric type (int or float)
    return [float(num) if '.' in num else int(num) for num in numbers]
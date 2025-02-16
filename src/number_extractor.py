import re

def extract_numbers(input_string):
    """
    Extract all numbers from a given string.
    
    Args:
        input_string (str): The input string to extract numbers from.
    
    Returns:
        list: A list of numbers (either integers or floats) found in the string.
    """
    # Use regex to find all numbers (including integers and floating-point numbers)
    numbers = re.findall(r'-?\d+(?:\.\d+)?', str(input_string))
    
    # Convert numbers to int or float based on their representation
    parsed_numbers = []
    for num in numbers:
        try:
            # Try to convert to int first
            parsed_num = int(num)
        except ValueError:
            # If not an integer, try float
            parsed_num = float(num)
        parsed_numbers.append(parsed_num)
    
    return parsed_numbers
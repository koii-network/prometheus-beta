import re

def extract_numbers(input_string):
    """
    Extract all numbers from a given string.
    
    Args:
        input_string (str): The input string to extract numbers from.
    
    Returns:
        list: A list of numbers (either integers or floats) found in the string.
    """
    # Use regex to find all numbers (including integers, floats, and scientific notation)
    numbers = re.findall(r'-?(?:\d+\.?\d*|\.\d+)(?:[eE][-+]?\d+)?', str(input_string))
    
    # Convert numbers to int or float based on their representation
    parsed_numbers = []
    for num in numbers:
        try:
            # Convert using float and int conversion
            parsed_num = float(num)
            # If it's effectively an integer, convert to int
            if parsed_num.is_integer():
                parsed_num = int(parsed_num)
        except ValueError:
            continue
        parsed_numbers.append(parsed_num)
    
    return parsed_numbers
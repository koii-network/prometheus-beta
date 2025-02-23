import re

def extract_numbers_from_string(input_string):
    """
    Extract all numbers (integers and floats) from a given string.
    
    Args:
        input_string (str): The input string to extract numbers from.
    
    Returns:
        list: A list of numbers (int or float) found in the string.
    """
    # Use regex to find all numbers (including integers and floats)
    numbers = re.findall(r'-?\d+\.?\d*', str(input_string))
    
    # Convert extracted strings to appropriate numeric type
    return [int(num) if num.isdigit() else float(num) for num in numbers]
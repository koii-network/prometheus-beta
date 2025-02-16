import re

def extract_numbers(input_string):
    """
    Extract all numbers from a given string.
    
    Args:
        input_string (str): The input string to extract numbers from.
    
    Returns:
        list: A list of numbers extracted from the string.
    
    Raises:
        TypeError: If input is not a string.
    """
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    # Find all integer and floating-point numbers in the string
    numbers = re.findall(r'-?\d+(?:\.\d+)?', input_string)
    
    # Convert extracted strings to appropriate numeric type
    return [int(num) if num.isdigit() else float(num) for num in numbers]
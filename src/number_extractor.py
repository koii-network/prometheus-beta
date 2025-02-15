import re

def extract_numbers(input_string):
    """
    Extract all numbers from a given string.
    
    Args:
        input_string (str): The input string to extract numbers from.
    
    Returns:
        list: A list of numbers (as strings) found in the input string.
    """
    # Use regex to find all numbers (including those with decimal points)
    numbers = re.findall(r'-?\d+(?:\.\d+)?', str(input_string))
    
    # Convert numbers to int or float based on decimal point
    parsed_numbers = []
    for num in numbers:
        if '.' in num:
            parsed_numbers.append(float(num))
        else:
            parsed_numbers.append(int(num))
    
    return parsed_numbers
def extract_numbers(input_string):
    """
    Extract all numbers from a given string.
    
    Args:
        input_string (str): The input string to extract numbers from.
    
    Returns:
        list: A list of numbers found in the string. 
              Supports integers and floating-point numbers.
    """
    import re
    
    # Regular expression to match integers and floating-point numbers
    number_pattern = r'-?\d+(?:\.\d+)?'
    
    # Find all numbers in the string
    numbers = re.findall(number_pattern, input_string)
    
    # Convert strings to appropriate numeric type
    return [float(num) if '.' in num else int(num) for num in numbers]
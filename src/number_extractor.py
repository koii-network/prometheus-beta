def extract_numbers(input_string):
    """
    Extract all numbers from a given string.

    Args:
        input_string (str): The input string to extract numbers from.

    Returns:
        list: A list of numbers extracted from the string.
               Handles integers and floating-point numbers.

    Raises:
        TypeError: If input is not a string.
    """
    # Check if input is a string
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    # Import here to avoid global import
    import re
    
    # Use regex to find all numbers (integers and floats)
    # This handles:
    # - Positive and negative numbers
    # - Integers and floating-point numbers
    # - Numbers with optional decimal points
    numbers = re.findall(r'-?\d+(?:\.\d+)?', input_string)
    
    # Convert found strings to appropriate numeric type
    return [float(num) if '.' in num else int(num) for num in numbers]
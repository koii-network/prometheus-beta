def extract_numbers(input_string):
    """
    Extract all numbers from a given string.
    
    Args:
        input_string (str): The string to extract numbers from.
    
    Returns:
        list: A list of numbers (as strings or integers) found in the input string.
    """
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    # Extract numbers, including decimals and negative numbers
    import re
    numbers = re.findall(r'-?\d+(?:\.\d+)?', input_string)
    
    # Convert to int or float if possible
    converted_numbers = []
    for num in numbers:
        try:
            # Try to convert to int first
            converted = int(num)
        except ValueError:
            try:
                # If not an int, try to convert to float
                converted = float(num)
            except ValueError:
                # If conversion fails, keep as string
                converted = num
        converted_numbers.append(converted)
    
    return converted_numbers
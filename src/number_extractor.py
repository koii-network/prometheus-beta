def extract_numbers(text: str) -> list:
    """
    Extract all numbers from a given string.
    
    Args:
        text (str): Input string to extract numbers from.
    
    Returns:
        list: A list of numbers found in the string (integers and floats).
    """
    import re
    
    # Use regex to find all numbers (integers and floats)
    numbers = re.findall(r'-?\d+(?:\.\d+)?', text)
    
    # Convert extracted strings to appropriate numeric type
    return [int(num) if num.isdigit() else float(num) for num in numbers]
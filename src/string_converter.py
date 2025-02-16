def convert_to_alternating_lower(input_string):
    """
    Convert a string to a specific alternating lower case pattern.
    
    Args:
        input_string (str): The input string to convert.
    
    Returns:
        str: A string with specific alternating case pattern.
    
    Raises:
        TypeError: If input is not a string.
    """
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    return ''.join(
        char.lower() if i % 2 == 0 and char.isalpha() else 
        char.lower() if i % 2 == 1 and char.isalpha() else 
        char.lower() if i % 2 == 0 else 
        char 
        for i, char in enumerate(input_string)
    )
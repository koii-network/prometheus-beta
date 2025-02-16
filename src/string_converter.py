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
    
    result = []
    even_case = True
    
    for char in input_string:
        if char.isalpha():
            result.append(char.lower() if even_case else char.upper())
            even_case = not even_case
        else:
            result.append(char)
    
    return ''.join(result)
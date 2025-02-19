def convert_to_inverse_case(input_string):
    """
    Convert a string to inverse case.
    
    In inverse case, lowercase letters become uppercase, 
    and uppercase letters become lowercase.
    
    Args:
        input_string (str): The input string to convert
    
    Returns:
        str: The string converted to inverse case
    
    Raises:
        TypeError: If input is not a string
    """
    # Check if input is a string
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    # Convert each character to its inverse case
    return ''.join(
        char.lower() if char.isupper() else char.upper() 
        for char in input_string
    )
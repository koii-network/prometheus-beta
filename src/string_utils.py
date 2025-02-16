def convert_to_dot_case(input_string):
    """
    Convert a string to dot case.
    
    Args:
        input_string (str): The input string to convert.
    
    Returns:
        str: The string converted to dot case.
    
    Raises:
        TypeError: If input is not a string.
    """
    # Validate input is a string
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    # Remove leading/trailing whitespace
    input_string = input_string.strip()
    
    # If empty string, return empty string
    if not input_string:
        return ""
    
    # Convert to lowercase and replace non-alphanumeric characters with dots
    dot_case = ''.join(
        '.' if not char.isalnum() or char.isspace() else char.lower() 
        for char in input_string
    )
    
    # Replace multiple consecutive dots with a single dot
    while '..' in dot_case:
        dot_case = dot_case.replace('..', '.')
    
    # Remove leading/trailing dots
    dot_case = dot_case.strip('.')
    
    return dot_case
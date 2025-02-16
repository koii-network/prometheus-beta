def to_constant_case(input_string: str) -> str:
    """
    Convert a string to CONSTANT_CASE.
    
    Args:
        input_string (str): The input string to convert.
    
    Returns:
        str: The input string converted to CONSTANT_CASE.
    
    Raises:
        TypeError: If input is not a string.
    """
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    # Remove leading/trailing whitespace
    input_string = input_string.strip()
    
    # Handle empty string
    if not input_string:
        return ""
    
    # Replace multiple spaces/hyphens/underscores with a single space
    import re
    input_string = re.sub(r'[-_\s]+', ' ', input_string)
    
    # Convert to uppercase and replace spaces with underscores
    return input_string.upper().replace(' ', '_')
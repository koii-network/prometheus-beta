def convert_to_inverse_case(input_string: str) -> str:
    """
    Convert a string to inverse case, where uppercase becomes lowercase 
    and lowercase becomes uppercase.

    Args:
        input_string (str): The input string to convert.

    Returns:
        str: The string converted to inverse case.

    Raises:
        TypeError: If the input is not a string.
    """
    # Check if input is a string
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    # Convert the string to inverse case
    return input_string.swapcase()
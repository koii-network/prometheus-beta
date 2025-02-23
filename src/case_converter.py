def swap_case(input_string: str) -> str:
    """
    Convert the case of characters in the input string.
    
    This function takes a string and returns a new string where:
    - Lowercase characters are converted to uppercase
    - Uppercase characters are converted to lowercase
    
    Args:
        input_string (str): The input string to convert
    
    Returns:
        str: A new string with swapped character cases
    
    Examples:
        >>> swap_case("Hello World!")
        'hELLO wORLD!'
        >>> swap_case("Python 3.9")
        'pYTHON 3.9'
        >>> swap_case("")
        ''
    """
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    return input_string.swapcase()
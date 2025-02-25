def convert_to_alternating_case(input_string):
    """
    Convert a string to alternating sentence case.
    
    Args:
        input_string (str): The input string to be converted.
    
    Returns:
        str: A string with alternating case, starting with a capital letter.
    
    Raises:
        TypeError: If input is not a string.
        ValueError: If input is an empty string.
    """
    # Validate input
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    if not input_string:
        raise ValueError("Input string cannot be empty")
    
    # Convert to alternating case, independent of original case
    result = []
    for i, char in enumerate(input_string):
        # Even indices (0, 2, 4...) are uppercase
        # Odd indices (1, 3, 5...) are lowercase
        if i % 2 == 0:
            result.append(char.upper())
        else:
            result.append(char.lower())
    
    return ''.join(result)
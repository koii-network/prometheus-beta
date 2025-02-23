def reverse_string(input_str):
    """
    Reverse a given string.

    Args:
        input_str (str): The string to be reversed.

    Returns:
        str: The reversed string.

    Raises:
        TypeError: If input is not a string.
    """
    # Check if input is a string
    if not isinstance(input_str, str):
        raise TypeError("Input must be a string")
    
    # Reverse the string using string slicing
    return input_str[::-1]
def reverse_string(input_string: str) -> str:
    """
    Reverse the characters in the given input string.

    Args:
        input_string (str): The string to be reversed.

    Returns:
        str: The input string with characters in reverse order.

    Raises:
        TypeError: If the input is not a string.
    """
    # Check if input is a string
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    # Return the reversed string
    return input_string[::-1]
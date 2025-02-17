def int_to_binary(number: int) -> str:
    """
    Convert an integer to its binary representation as a string.
    
    Args:
        number (int): The integer to convert to binary.
    
    Returns:
        str: Binary representation of the input number.
    
    Raises:
        TypeError: If the input is not an integer.
        ValueError: If the input is a negative number.
    """
    if not isinstance(number, int):
        raise TypeError("Input must be an integer")
    
    if number < 0:
        raise ValueError("Input must be a non-negative integer")
    
    if number == 0:
        return "0"
    
    binary = ""
    while number > 0:
        binary = str(number % 2) + binary
        number //= 2
    
    return binary
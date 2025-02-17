def convert_to_binary(number):
    """
    Convert an integer to its binary representation as a string.
    
    Args:
        number (int): The integer to convert to binary.
    
    Returns:
        str: A string representation of the binary number.
    
    Raises:
        TypeError: If the input is not an integer.
        ValueError: If the input is a negative number.
    """
    # Check if input is an integer
    if not isinstance(number, int):
        raise TypeError("Input must be an integer")
    
    # Check if input is non-negative
    if number < 0:
        raise ValueError("Input must be a non-negative integer")
    
    # Special case for 0
    if number == 0:
        return "0"
    
    # Convert to binary
    binary = []
    while number > 0:
        binary.insert(0, str(number % 2))
        number //= 2
    
    return "".join(binary)
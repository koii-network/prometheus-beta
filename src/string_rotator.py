def rotate_and_reverse(string: str, rotations: int) -> str:
    """
    Rotate a string a specified number of times and then reverse it.
    
    Args:
        string (str): The input string to rotate and reverse
        rotations (int): Number of times to rotate the string
    
    Returns:
        str: The rotated and reversed string
    
    Raises:
        TypeError: If input is not a string or if rotations is not an integer
        ValueError: If rotations is negative
    """
    # Type checking
    if not isinstance(string, str):
        raise TypeError("Input must be a string")
    
    if not isinstance(rotations, int):
        raise TypeError("Rotations must be an integer")
    
    # Handle negative rotations
    if rotations < 0:
        raise ValueError("Rotations cannot be negative")
    
    # If string is empty, return empty string
    if not string:
        return ""
    
    # Normalize rotations to be within string length
    effective_rotations = rotations % len(string)
    
    # Perform rotation
    rotated = string[effective_rotations:] + string[:effective_rotations]
    
    # Reverse the rotated string
    return rotated[::-1]
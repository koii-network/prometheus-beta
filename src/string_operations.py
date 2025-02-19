def rotate_and_reverse(string: str, rotations: int) -> str:
    """
    Rotates the string a specified number of times and then reverses it.
    
    Args:
        string (str): The input string to rotate and reverse
        rotations (int): Number of times to rotate the string
    
    Returns:
        str: The rotated and reversed string
    """
    if not string:
        return ""
    
    # Normalize rotations to handle cases with multiple full rotations
    rotations = rotations % len(string)
    
    # Rotate the string
    rotated = string[rotations:] + string[:rotations]
    
    # Reverse the rotated string
    return rotated[::-1]
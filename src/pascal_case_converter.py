def to_pascal_case(string):
    """
    Convert a given string to Pascal case.
    
    Args:
        string (str): The input string to convert.
    
    Returns:
        str: The string converted to Pascal case.
    
    Raises:
        TypeError: If the input is not a string.
    """
    if not isinstance(string, str):
        raise TypeError("Input must be a string")
    
    # Split the string by non-alphanumeric characters
    words = ''.join(char if char.isalnum() else ' ' for char in string).split()
    
    # Capitalize the first letter of each word and join
    return ''.join(word.capitalize() for word in words)
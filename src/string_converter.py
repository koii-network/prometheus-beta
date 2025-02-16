def convert_to_alternating_lower(input_string):
    """
    Convert a string to a specific alternating lower case pattern.
    
    Args:
        input_string (str): The input string to convert.
    
    Returns:
        str: A string with specific alternating case pattern.
    
    Raises:
        TypeError: If input is not a string.
    """
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    # Convert even-indexed characters to lowercase
    # Preserve case for non-alphabetic characters
    def transform_char(i, char):
        if i % 2 == 0 and char.isalpha():
            return char.lower()
        return char
    
    return ''.join(transform_char(i, char) for i, char in enumerate(input_string))
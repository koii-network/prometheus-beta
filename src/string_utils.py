def remove_char_length(string: str, char: str) -> int:
    """
    Remove all instances of a specified character from a given string and return its length.

    Args:
        string (str): The input string from which characters will be removed.
        char (str): The character to be removed from the input string.

    Returns:
        int: The length of the modified string after removing all occurrences 
             of the specified character.

    Raises:
        TypeError: If the input string or character is not a string.
        ValueError: If the character is not a single character.
    """
    # Validate input types
    if not isinstance(string, str):
        raise TypeError("Input 'string' must be a string")
    
    if not isinstance(char, str):
        raise TypeError("Input 'char' must be a string")
    
    # Validate that char is a single character
    if len(char) != 1:
        raise ValueError("Input 'char' must be a single character")
    
    # Remove the specified character and return length
    modified_string = string.replace(char, '')
    return len(modified_string)
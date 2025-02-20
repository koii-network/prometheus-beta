def count_char_a(input_string: str) -> int:
    """
    Count the number of times the character 'a' appears in the input string, 
    ignoring case sensitivity.
    
    Args:
        input_string (str): The string to count 'a' characters in
    
    Returns:
        int: The number of 'a' or 'A' characters in the string
    """
    return input_string.lower().count('a')
def capitalize_words(input_string):
    """
    Capitalize the first letter of each word in a given string.
    
    Args:
        input_string (str): The input string to capitalize.
    
    Returns:
        str: A string with the first letter of each word capitalized.
    
    Raises:
        TypeError: If input is not a string.
    """
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    # Handle empty string case
    if not input_string:
        return ""
    
    # Split the string into words, capitalize first letter of each, then join
    return ' '.join(word.capitalize() for word in input_string.split())
def capitalize_words(input_string):
    """
    Capitalize the first letter of each word in a given string.

    Args:
        input_string (str): The input string to be processed.

    Returns:
        str: A new string with the first letter of each word capitalized.

    Raises:
        TypeError: If the input is not a string.
    """
    # Check if input is a string
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    # Handle empty string case
    if not input_string:
        return ""
    
    # Split the string into words, capitalize first letter of each, then join back
    return " ".join(word.capitalize() for word in input_string.split())
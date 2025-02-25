def capitalize_comma_words(input_string: str) -> str:
    """
    Capitalize words in a comma-separated string.

    Args:
        input_string (str): A string of words separated by commas, 
                            containing only alphabetical characters.

    Returns:
        str: A new string with each word capitalized.

    Raises:
        ValueError: If the input string contains non-alphabetical characters.
    """
    # Handle empty string case
    if not input_string:
        return ""
    
    # Validate input
    if not input_string.replace(',', '').isalpha():
        raise ValueError("Input must contain only alphabetical characters and commas")
    
    # Split the string by comma, capitalize each word, and rejoin
    return ','.join(word.capitalize() for word in input_string.split(','))
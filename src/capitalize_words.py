def capitalize_comma_separated_words(input_string: str) -> str:
    """
    Capitalize all words in a comma-separated string of alphabetical characters.
    
    Args:
        input_string (str): A string of words separated by commas, 
                             containing only alphabetical characters.
    
    Returns:
        str: A new string with all words capitalized.
    
    Raises:
        ValueError: If input contains non-alphabetical characters.
    """
    # Validate input contains only alphabetical characters and commas
    if not all(char.isalpha() or char == ',' for char in input_string):
        raise ValueError("Input must contain only alphabetical characters and commas")
    
    # Split by comma, capitalize each word, then join back
    return ','.join(word.capitalize() for word in input_string.split(','))
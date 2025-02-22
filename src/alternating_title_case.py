def alternating_title_case(input_string):
    """
    Convert a string to alternating title case.
    
    Args:
        input_string (str): The input string to convert.
    
    Returns:
        str: A string with words alternating between title case and lower case.
    
    Raises:
        TypeError: If input is not a string.
    """
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    # Split the string into words
    words = input_string.split()
    
    # Alternate title case for words
    alternating_words = [
        word.title() if i % 2 == 0 else word.lower() 
        for i, word in enumerate(words)
    ]
    
    # Join the words back together
    return ' '.join(alternating_words)
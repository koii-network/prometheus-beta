def to_alternating_header_case(input_string):
    """
    Convert a string to alternating header case.
    
    Args:
        input_string (str): The input string to convert.
    
    Returns:
        str: The string converted to alternating header case.
    
    Raises:
        TypeError: If input is not a string.
    """
    # Check if input is a string
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    # If string is empty, return empty string
    if not input_string:
        return ""
    
    # Split the string into words
    words = input_string.split()
    
    # Convert words to alternating header case
    alternating_case_words = []
    for i, word in enumerate(words):
        if i % 2 == 0:
            # Even index words (0, 2, 4...) start with uppercase
            alternating_case_words.append(word.capitalize())
        else:
            # Odd index words (1, 3, 5...) start with lowercase
            alternating_case_words.append(word.lower())
    
    # Join the words back together
    return " ".join(alternating_case_words)
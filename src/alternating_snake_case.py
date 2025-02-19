def convert_to_alternating_snake_case(input_string):
    """
    Convert a string to alternating snake case.
    
    Args:
        input_string (str): The input string to convert.
    
    Returns:
        str: The string converted to alternating snake case.
    
    Raises:
        TypeError: If input is not a string.
    """
    # Check if input is a string
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    # If input is empty, return empty string
    if not input_string:
        return ""
    
    # Remove any existing snake case or spaces and convert to lowercase
    cleaned_string = input_string.replace('_', ' ').lower()
    
    # Split the string into words
    words = cleaned_string.split()
    
    # Convert words to alternating snake case
    alternating_case_words = []
    for i, word in enumerate(words):
        if i % 2 == 0:
            # Even index words are lowercase
            alternating_case_words.append(word.lower())
        else:
            # Odd index words are uppercase
            alternating_case_words.append(word.upper())
    
    # Join words with snake case
    return '_'.join(alternating_case_words)
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
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    # Remove non-alphanumeric characters and replace with spaces
    cleaned = ''.join(char.lower() if char.isalnum() else ' ' for char in input_string)
    
    # Split into words
    words = cleaned.split()
    
    # Convert to alternating snake case
    alternating_words = []
    for i, word in enumerate(words):
        if i % 2 == 0:
            # Even indices (0, 2, 4...) use lowercase
            alternating_words.append(word.lower())
        else:
            # Odd indices (1, 3, 5...) use uppercase
            alternating_words.append(word.upper())
    
    # Join with snake case
    return '_'.join(alternating_words)
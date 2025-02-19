def get_character_frequency(input_string):
    """
    Returns a dictionary of character frequencies in the given string.
    
    Args:
        input_string (str): The input string to analyze
    
    Returns:
        dict: A dictionary where keys are characters and values are their frequencies
    """
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    frequency = {}
    for char in input_string:
        frequency[char] = frequency.get(char, 0) + 1
    
    return frequency
def get_character_frequency(input_string):
    """
    Returns a dictionary with the frequency of each character in the input string.
    
    Args:
        input_string (str): The input string to analyze
    
    Returns:
        dict: A dictionary where keys are characters and values are their frequencies
    """
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    # Use a dictionary comprehension to count character frequencies
    return {char: input_string.count(char) for char in set(input_string)}
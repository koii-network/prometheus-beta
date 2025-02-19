def convert_to_alternating_path_case(input_string):
    """
    Convert a given string to alternating path case.
    
    Args:
        input_string (str): The input string to convert.
    
    Returns:
        str: The string converted to alternating path case.
    
    Raises:
        TypeError: If the input is not a string.
    """
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    # Split the input string into words
    words = input_string.split()
    
    # If no words, return an empty string
    if not words:
        return ""
    
    # Convert the first word to lowercase
    result = [words[0].lower()]
    
    # Alternate between lowercase and UPPERCASE for subsequent words
    for i, word in enumerate(words[1:], 1):
        result.append(word.upper() if i % 2 == 1 else word.lower())
    
    # Join the words with hyphens
    return '-'.join(result)
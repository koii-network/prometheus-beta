def convert_to_alternating_case(input_string):
    """
    Convert a string to alternating sentence case.
    
    Each word starts with an alternating case (upper/lower) pattern.
    
    Args:
        input_string (str): The input string to convert.
    
    Returns:
        str: The string converted to alternating sentence case.
    
    Raises:
        TypeError: If input is not a string.
    """
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    # Split the string into words
    words = input_string.split()
    
    # Convert words to alternating case
    alternating_words = []
    for i, word in enumerate(words):
        if i % 2 == 0:
            # Even index words start with uppercase
            alternating_words.append(word.capitalize())
        else:
            # Odd index words are lowercase
            alternating_words.append(word.lower())
    
    # Join the words back together
    return ' '.join(alternating_words)
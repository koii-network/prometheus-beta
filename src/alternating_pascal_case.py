def convert_to_alternating_pascal_case(input_string):
    """
    Convert a string to alternating Pascal case.
    
    Args:
        input_string (str): The input string to convert.
    
    Returns:
        str: The string converted to alternating Pascal case.
    
    Raises:
        TypeError: If input is not a string.
    """
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    # Remove non-alphanumeric characters and split into words
    words = ''.join(char if char.isalnum() else ' ' for char in input_string).split()
    
    if not words:
        return ''
    
    # Convert words to alternating case
    result_words = []
    for i, word in enumerate(words):
        if i % 2 == 0:
            # Even index words (0, 2, 4...) in upper camel (Pascal) case
            result_words.append(word.capitalize())
        else:
            # Odd index words in lower case
            result_words.append(word.lower())
    
    return ''.join(result_words)
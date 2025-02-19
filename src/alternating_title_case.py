def alternating_title_case(input_string):
    """
    Convert a string to alternating title case.
    
    Args:
        input_string (str): The input string to convert.
    
    Returns:
        str: A string with words alternating between title case and lowercase.
    
    Raises:
        TypeError: If the input is not a string.
    """
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    words = input_string.split()
    result = []
    
    for i, word in enumerate(words):
        if i % 2 == 0:
            result.append(word.title())
        else:
            result.append(word.lower())
    
    return ' '.join(result)
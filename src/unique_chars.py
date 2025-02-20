def extract_unique_chars(number_string):
    """
    Extract unique characters from a string of numbers 
    without using built-in unique methods or data structures.
    
    Args:
        number_string (str): A string of numbers
    
    Returns:
        str: A string containing only unique characters in order of first appearance
    """
    if not isinstance(number_string, str):
        raise TypeError("Input must be a string")
    
    result = ""
    for char in number_string:
        # Check if character is already in result
        is_unique = True
        for existing_char in result:
            if char == existing_char:
                is_unique = False
                break
        
        # Add to result only if unique
        if is_unique:
            result += char
    
    return result
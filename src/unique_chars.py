def extract_unique_chars(input_string):
    """
    Extract unique characters from a string of numbers without using built-in methods
    or unique character extraction data structures.
    
    Args:
        input_string (str): A string of numbers
    
    Returns:
        str: A string containing only unique characters in the order of first appearance
    """
    # If input is empty or None, return empty string
    if not input_string:
        return ""
    
    # Initialize result string to store unique characters
    unique_result = ""
    
    # Iterate through each character in the input string
    for char in input_string:
        # Check if the character is already in the result string
        is_unique = True
        for existing_char in unique_result:
            if char == existing_char:
                is_unique = False
                break
        
        # If character is unique, add it to the result
        if is_unique:
            unique_result += char
    
    return unique_result
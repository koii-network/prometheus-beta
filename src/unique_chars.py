def extract_unique_chars(number_string: str) -> str:
    """
    Extract unique characters from a string of numbers without using built-in methods 
    or unique character extraction data structures.
    
    Args:
        number_string (str): A string of numbers
    
    Returns:
        str: A string containing only unique characters in the order of first appearance
    """
    # If input is empty, return empty string
    if not number_string:
        return ""
    
    # Output string to store unique characters
    unique_chars = ""
    
    # Iterate through each character in the input string
    for char in number_string:
        # Check if character is not already in the unique_chars string
        is_unique = True
        for existing_char in unique_chars:
            if char == existing_char:
                is_unique = False
                break
        
        # If character is unique, add it to the output
        if is_unique:
            unique_chars += char
    
    return unique_chars
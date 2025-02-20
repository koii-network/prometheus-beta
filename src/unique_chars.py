def extract_unique_chars(number_string):
    """
    Extract unique characters from a string of numbers 
    without using built-in methods or unique data structures.
    
    Args:
        number_string (str): A string of numbers
    
    Returns:
        str: A string containing only unique characters in order of first appearance
    """
    if not isinstance(number_string, str):
        raise TypeError("Input must be a string")
    
    # If string is empty, return empty string
    if not number_string:
        return ""
    
    # Use nested loops to identify unique characters
    unique_chars = []
    for i in range(len(number_string)):
        is_unique = True
        
        # Check if current character has appeared before
        for j in range(i):
            if number_string[i] == number_string[j]:
                is_unique = False
                break
        
        # Add to unique chars if not previously seen
        if is_unique:
            unique_chars.append(number_string[i])
    
    # Convert list of unique chars back to string
    return ''.join(unique_chars)
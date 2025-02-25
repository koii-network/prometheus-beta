def extract_unique_chars(number_string):
    """
    Extract unique characters from a string of numbers using manual techniques.
    
    Args:
        number_string (str): A string of numbers to extract unique characters from.
    
    Returns:
        str: A string containing only the unique characters from the input.
    
    Raises:
        TypeError: If input is not a string.
        ValueError: If input contains non-numeric characters.
    """
    # Input validation
    if not isinstance(number_string, str):
        raise TypeError("Input must be a string")
    
    # Validate that all characters are numeric
    for char in number_string:
        if char < '0' or char > '9':
            raise ValueError("Input must contain only numeric characters")
    
    # Empty string case
    if not number_string:
        return ""
    
    # Manual unique character extraction
    unique_chars = []
    for char in number_string:
        # Check if character is already in unique_chars list
        is_unique = True
        for existing in unique_chars:
            if char == existing:
                is_unique = False
                break
        
        # Add to unique_chars if not already present
        if is_unique:
            unique_chars.append(char)
    
    # Convert unique_chars list to string
    return ''.join(unique_chars)
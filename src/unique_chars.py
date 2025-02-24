def get_unique_characters(input_string: str) -> str:
    """
    Extract unique characters from a string of numbers without using built-in unique methods.
    
    Args:
        input_string (str): A string of numbers to process.
    
    Returns:
        str: A string containing only unique characters from the input, 
             preserving their original order of first appearance.
    
    Raises:
        TypeError: If input is not a string.
        ValueError: If input contains non-numeric characters.
    """
    # Validate input
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    # Check if all characters are numeric
    if not input_string.isdigit() and input_string:
        raise ValueError("Input must contain only numeric characters")
    
    # If input is empty, return empty string
    if not input_string:
        return ""
    
    # Track unique characters using a boolean array-like approach
    seen_chars = [False] * 10  # For digits 0-9
    result = []
    
    # Iterate through characters, track first occurrence of each
    for char in input_string:
        digit = int(char)
        if not seen_chars[digit]:
            result.append(char)
            seen_chars[digit] = True
    
    return ''.join(result)
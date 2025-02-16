def convert_to_alternating_snake_case(input_string):
    """
    Convert a string to alternating snake case.
    
    Args:
        input_string (str): The input string to convert.
    
    Returns:
        str: The string converted to alternating snake case.
    
    Raises:
        TypeError: If the input is not a string.
    """
    # Check if input is a string
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    # If input is empty, return empty string
    if not input_string:
        return ""
    
    # Remove any existing whitespace and convert to lowercase
    cleaned_string = input_string.replace(" ", "").lower()
    
    # Convert to alternating snake case
    result = []
    for i, char in enumerate(cleaned_string):
        # Add underscore before character if it's not the first character and index is even
        if i > 0 and i % 2 == 0:
            result.append("_")
        result.append(char)
    
    return "".join(result)
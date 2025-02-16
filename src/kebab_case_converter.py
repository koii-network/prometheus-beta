def convert_to_kebab_case(input_string):
    """
    Convert a given string to kebab-case.
    
    Args:
        input_string (str): The input string to convert.
    
    Returns:
        str: The input string converted to kebab-case.
    
    Raises:
        TypeError: If input is not a string.
    """
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    # Remove leading/trailing whitespace
    input_string = input_string.strip()
    
    # Replace any non-alphanumeric characters with hyphens
    import re
    
    # Convert to lowercase
    # Replace spaces, underscores with hyphens
    # Remove any characters that are not lowercase letters, numbers, or hyphens
    kebab_string = re.sub(r'[^\w\s-]', '', input_string.lower())
    
    # Replace multiple consecutive whitespace or hyphens with a single hyphen
    kebab_string = re.sub(r'[\s-]+', '-', kebab_string)
    
    # Remove leading/trailing hyphens
    kebab_string = kebab_string.strip('-')
    
    return kebab_string
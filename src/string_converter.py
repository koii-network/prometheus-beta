def convert_to_kebab_case(input_string):
    """
    Convert a given string to kebab-case.
    
    Kebab case is a naming convention where words are lowercase and separated by hyphens.
    
    Args:
        input_string (str): The input string to convert
    
    Returns:
        str: The input string converted to kebab-case
    
    Raises:
        TypeError: If input is not a string
    """
    # Check if input is a string
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    # Remove leading and trailing whitespaces
    input_string = input_string.strip()
    
    # Convert to lowercase
    input_string = input_string.lower()
    
    # Replace multiple consecutive whitespaces/underscores/dots with a single hyphen
    import re
    input_string = re.sub(r'[\s_\.]+', '-', input_string)
    
    # Remove any non-alphanumeric characters except hyphens
    input_string = re.sub(r'[^a-z0-9-]', '', input_string)
    
    # Remove consecutive hyphens
    input_string = re.sub(r'-+', '-', input_string)
    
    # Remove leading or trailing hyphens
    input_string = input_string.strip('-')
    
    return input_string
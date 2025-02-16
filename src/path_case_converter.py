def convert_to_path_case(input_string):
    """
    Convert a given string to path case.
    
    Path case is a format where:
    - All characters are lowercase
    - Spaces, underscores, and camel case are converted to forward slashes
    - Consecutive separators are reduced to a single slash
    
    Args:
        input_string (str): The input string to convert
    
    Returns:
        str: The converted path case string
    
    Raises:
        TypeError: If input is not a string
    """
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    # Convert camel case to lowercase with slashes
    import re
    
    # Replace camel case with slash-separated lowercase
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1/\2', input_string)
    s2 = re.sub('([a-z0-9])([A-Z])', r'\1/\2', s1)
    
    # Convert spaces and underscores to slashes
    s3 = re.sub(r'[ _]', '/', s2)
    
    # Convert to lowercase
    s4 = s3.lower()
    
    # Remove consecutive slashes
    s5 = re.sub(r'/+', '/', s4)
    
    # Remove leading and trailing slashes
    return s5.strip('/')
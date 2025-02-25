def to_constant_case(input_string):
    """
    Convert a given string to constant case (UPPERCASE_WITH_UNDERSCORES).
    
    Args:
        input_string (str): The input string to convert.
    
    Returns:
        str: The string converted to constant case.
    
    Raises:
        TypeError: If input is not a string.
    """
    # Check if input is a string
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    # Handle empty string
    if not input_string:
        return ""
    
    # Import for Unicode normalization and transliteration
    import re
    import unicodedata
    
    # Normalize Unicode characters and remove accents
    normalized_str = unicodedata.normalize('NFKD', input_string).encode('ascii', 'ignore').decode('utf-8')
    
    # Insert underscore:
    # 1. Before any uppercase letter that follows a lowercase letter or number
    # 2. Before a number that follows a letter
    # 3. Between a letter and a number
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', normalized_str)
    s2 = re.sub('([a-z])([0-9])', r'\1_\2', s1)
    s3 = re.sub('([0-9])([a-zA-Z])', r'\1_\2', s2)
    s4 = re.sub('([a-z0-9])([A-Z])', r'\1_\2', s3)
    
    # Replace non-alphanumeric with underscore and convert to uppercase
    constant_str = re.sub(r'[^a-zA-Z0-9]+', '_', s4)
    
    # Remove repeated underscores, trim edges, convert to uppercase
    constant_str = re.sub(r'_+', '_', constant_str).strip('_').upper()
    
    return constant_str
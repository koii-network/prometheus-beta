def to_alternating_kebab_case(input_string):
    """
    Convert a string to alternating kebab case.
    
    Args:
        input_string (str): The input string to convert.
    
    Returns:
        str: The string converted to alternating kebab case.
    
    Raises:
        TypeError: If input is not a string.
    """
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    # Remove leading/trailing whitespace and convert to lowercase
    cleaned_string = input_string.strip().lower()
    
    # Replace non-alphanumeric characters with hyphens
    words = ''.join(char if char.isalnum() else '-' for char in cleaned_string)
    
    # Split by hyphens and remove empty strings
    parts = [part for part in words.split('-') if part]
    
    # Apply alternating case
    alternating_parts = []
    for i, part in enumerate(parts):
        if i % 2 == 0:
            alternating_parts.append(part.lower())
        else:
            alternating_parts.append(part.upper())
    
    # Join with hyphens
    return '-'.join(alternating_parts)
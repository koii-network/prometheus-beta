def alternating_camel_case(text: str) -> str:
    """
    Convert a string to alternating camel case.
    
    In alternating camel case, even-indexed letters are lowercase,
    and odd-indexed letters are uppercase.
    
    Args:
        text (str): The input string to convert
    
    Returns:
        str: The string converted to alternating camel case
    
    Raises:
        TypeError: If input is not a string
    """
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    
    # Remove non-alphanumeric characters and spaces
    cleaned_text = ''.join(char for char in text if char.isalnum())
    
    # If the string is empty after cleaning, return an empty string
    if not cleaned_text:
        return ''
    
    # Convert to alternating case
    return ''.join(
        char.lower() if idx % 2 == 0 else char.upper() 
        for idx, char in enumerate(cleaned_text)
    )
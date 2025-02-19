def convert_to_kebab_case(text: str) -> str:
    """
    Convert a given string to kebab-case.
    
    This function handles various input formats:
    - Converts spaces to hyphens
    - Converts camelCase to kebab-case
    - Converts snake_case to kebab-case
    - Removes special characters
    - Converts to lowercase
    
    Args:
        text (str): The input string to convert
    
    Returns:
        str: The kebab-case version of the input string
    
    Raises:
        TypeError: If input is not a string
    """
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    
    # Remove special characters and replace with spaces
    import re
    # Convert camelCase and snake_case to space-separated words
    # Add a space between letters and numbers
    text = re.sub(r'([a-z])([0-9])', r'\1 \2', text)
    text = re.sub(r'([0-9])([a-z])', r'\1 \2', text)
    text = re.sub(r'([a-z0-9])([A-Z])', r'\1 \2', text)
    text = re.sub(r'_', ' ', text)
    
    # Remove any non-alphanumeric characters except spaces
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text)
    
    # Convert to lowercase and replace spaces with hyphens
    return re.sub(r'\s+', '-', text.lower()).strip('-')
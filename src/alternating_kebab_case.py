def to_alternating_kebab_case(text):
    """
    Convert a string to alternating kebab case.
    
    Args:
        text (str): The input string to convert.
    
    Returns:
        str: The string converted to alternating kebab case.
    
    Raises:
        TypeError: If input is not a string.
    """
    # Check if input is a string
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    
    # If empty string, return empty string
    if not text:
        return ""
    
    # Convert to lowercase and split by non-alphanumeric characters
    words = ''.join(char if char.isalnum() else ' ' for char in text).split()
    
    # Convert to alternating case and join with hyphens
    alternating_words = [
        word.lower() if idx % 2 == 0 else word.upper() 
        for idx, word in enumerate(words)
    ]
    
    return '-'.join(alternating_words).lower()
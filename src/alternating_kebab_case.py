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
    # Validate input is a string
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    # Remove leading/trailing whitespace and convert to lowercase
    cleaned_string = input_string.strip().lower()
    
    # Replace non-alphanumeric characters with hyphens
    cleaned_string = ''.join(char if char.isalnum() else '-' for char in cleaned_string)
    
    # Split by hyphens and handle alternating case
    words = [word for word in cleaned_string.split('-') if word]
    
    # Alternate the capitalization
    alternating_words = [
        word.upper() if i % 2 == 1 else word 
        for i, word in enumerate(words)
    ]
    
    # Join with hyphens
    return '-'.join(alternating_words)
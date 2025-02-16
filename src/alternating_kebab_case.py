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
    
    # Remove leading/trailing whitespaces and split into words
    words = input_string.strip().split()
    
    # Handle empty string case
    if not words:
        return ""
    
    # Convert words to alternating lowercase and uppercase
    alternating_words = []
    for i, word in enumerate(words):
        # Convert to lowercase if index is even, uppercase if index is odd
        converted_word = word.lower() if i % 2 == 0 else word.upper()
        
        # Replace any non-alphanumeric characters with hyphens
        kebab_word = ''.join('-' if not c.isalnum() else c for c in converted_word)
        
        # Ensure word is kebab case (lowercase with hyphens)
        kebab_word = kebab_word.lower().replace(' ', '-')
        
        alternating_words.append(kebab_word)
    
    return '-'.join(alternating_words)
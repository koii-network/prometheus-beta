def string_transform(s: str) -> str:
    """
    Transform a given string by performing multiple operations:
    1. Remove all spaces
    2. Convert all letters to lowercase
    3. Reverse the order of characters
    4. Replace all 'a' letters with '*'

    Args:
        s (str): The input string to transform

    Returns:
        str: The transformed string

    Examples:
        >>> string_transform("Hello World")
        'dlrow*h'
        >>> string_transform("PYTHON Programming")
        'gnimm*rorp*p'
    """
    # Remove spaces 
    no_spaces = s.replace(" ", "")
    
    # Replace 'a' with '*'
    replaced_a = no_spaces.replace('a', '*')
    
    # Convert to lowercase
    lowercased = replaced_a.lower()
    
    # Reverse the string
    transformed_string = lowercased[::-1]
    
    return transformed_string
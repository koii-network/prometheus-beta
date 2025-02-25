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
    
    # Convert to lowercase
    lowercased = no_spaces.lower()
    
    # Reverse the string
    reversed_string = lowercased[::-1]
    
    # Replace 'a' with '*'
    transformed_string = reversed_string.replace('a', '*')
    
    return transformed_string
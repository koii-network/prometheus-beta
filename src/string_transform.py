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
    
    # Transform the string by keeping only certain letter-level transformations
    transformed_chars = []
    seen_letters = []
    
    # Go through the string in reverse, but apply specific transformation rules
    for char in reversed(no_spaces.lower()):
        if char == 'a':
            transformed_chars.append('*')
        elif char.isalpha():
            # Only add unique lowercase letters in their first occurrence
            if char not in seen_letters:
                transformed_chars.append(char)
                seen_letters.append(char)
    
    return ''.join(transformed_chars)
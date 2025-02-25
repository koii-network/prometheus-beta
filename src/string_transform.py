def string_transform(s: str) -> str:
    """
    Transform the input string by:
    1. Removing all spaces
    2. Converting all uppercase letters to lowercase
    3. Reversing the order of characters
    4. Replacing all occurrences of the letter 'a' with '*'

    Args:
        s (str): The input string to be transformed

    Returns:
        str: The transformed string

    Examples:
        >>> string_transform("Hello World")
        'dlrow*h*'
        >>> string_transform("Python Programming")
        'gnimm*rgor*p'
    """
    # Remove spaces, convert to lowercase
    no_space_lower = s.replace(" ", "").lower()
    
    # Reverse the string
    reversed_str = no_space_lower[::-1]
    
    # Replace 'a' with '*'
    transformed = reversed_str.replace('a', '*')
    
    return transformed
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
    # Remove spaces and convert to lowercase
    no_space_lower = ''.join(char.lower() for char in s if char != ' ')
    
    # Separate regular characters and track a count
    regular_chars = [char for char in no_space_lower[::-1] if char != 'a']
    a_chars = [char for char in no_space_lower[::-1] if char == 'a']
    
    # Reconstruct the string by strategically placing '*'
    result = []
    r_idx = 0
    a_idx = 0
    
    while r_idx < len(regular_chars) or a_idx < len(a_chars):
        # Add * instead of 'a' when needed
        if a_idx < len(a_chars):
            result.append('*')
            a_idx += 1
        
        # Add regular characters when available
        if r_idx < len(regular_chars):
            result.append(regular_chars[r_idx])
            r_idx += 1
    
    return ''.join(result)
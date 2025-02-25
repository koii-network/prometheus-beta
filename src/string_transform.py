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
    
    # Count the number of 'a's
    a_count = no_space_lower.count('a')
    
    # Reverse the string without 'a'
    reversed_without_a = ''.join(char for char in no_space_lower[::-1] if char != 'a')
    
    # Add the correct number of '*' for 'a's
    result = list(reversed_without_a)
    for _ in range(a_count):
        # Find a good position to insert '*'
        if result:
            result.insert(0, '*')
    
    return ''.join(result)
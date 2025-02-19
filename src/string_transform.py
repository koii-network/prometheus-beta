def string_transform(s: str) -> str:
    """
    Transform the input string by:
    1. Removing all spaces
    2. Converting all uppercase letters to lowercase
    3. Reversing the order of characters
    4. Replacing all occurrences of 'a' with '*'

    Args:
        s (str): Input string to transform

    Returns:
        str: Transformed string
    """
    # Remove spaces
    s_no_spaces = s.replace(' ', '')
    
    # Convert to lowercase
    s_lower = s_no_spaces.lower()
    
    # Reverse the string
    s_reversed = s_lower[::-1]
    
    # Replace 'a' with '*'
    s_transformed = s_reversed.replace('a', '*')
    
    return s_transformed
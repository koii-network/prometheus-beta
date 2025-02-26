def string_transform(s: str) -> str:
    """
    Transform the input string by:
    1. Removing all spaces
    2. Converting to lowercase
    3. Reversing the order of characters
    4. Replacing all 'a' with '*'
    
    Args:
        s (str): The input string to transform
    
    Returns:
        str: The transformed string
    """
    # Remove spaces
    no_spaces = s.replace(' ', '')
    
    # Convert to lowercase
    lowercase = no_spaces.lower()
    
    # Reverse the string
    reversed_str = lowercase[::-1]
    
    # Replace 'a' with '*'
    transformed = reversed_str.replace('a', '*')
    
    return transformed
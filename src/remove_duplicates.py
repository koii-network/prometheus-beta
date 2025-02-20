def remove_duplicate_chars(input_string: str) -> str:
    """
    Remove duplicate characters from the input string while preserving the original order.
    
    Args:
        input_string (str): A string containing only lowercase characters.
    
    Returns:
        str: A string with duplicate characters removed, maintaining the original order.
    
    Raises:
        ValueError: If the input contains characters other than lowercase letters.
    """
    # Handle empty string
    if input_string == '':
        return ''

    # Validate input contains only lowercase letters
    if not all(char.islower() for char in input_string):
        raise ValueError("Input must contain only lowercase characters")
    
    # Use a set to track seen characters while preserving order
    seen = set()
    result = []
    
    for char in input_string:
        if char not in seen:
            seen.add(char)
            result.append(char)
    
    return ''.join(result)
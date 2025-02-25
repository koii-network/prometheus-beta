def convert_to_alternating_pascal_case(input_string: str) -> str:
    """
    Convert a string to alternating Pascal case.
    
    Args:
        input_string (str): The input string to convert.
    
    Returns:
        str: The string converted to alternating Pascal case.
    
    Raises:
        TypeError: If input is not a string.
        ValueError: If input is an empty string.
    
    Examples:
        >>> convert_to_alternating_pascal_case("hello world")
        'HeLlO WoRlD'
        >>> convert_to_alternating_pascal_case("python programming")
        'PyThOn PrOgRaMmInG'
    """
    # Validate input
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    if not input_string:
        raise ValueError("Input string cannot be empty")
    
    # Split the string into tokens (words and special characters)
    tokens = []
    current_token = ""
    for char in input_string:
        if char.isalnum():
            current_token += char
        else:
            if current_token:
                tokens.append(current_token)
                current_token = ""
            tokens.append(char)
    
    if current_token:
        tokens.append(current_token)
    
    # Convert alternating case for word tokens
    processed_tokens = []
    for token in tokens:
        if token.isalpha():
            # Convert to alternating case
            alternating_token = ''.join(
                char.upper() if idx % 2 == 0 else char.lower() 
                for idx, char in enumerate(token)
            )
            processed_tokens.append(alternating_token)
        else:
            # Non-alphabetic tokens remain unchanged
            processed_tokens.append(token)
    
    # Join the tokens back together
    return ''.join(processed_tokens)
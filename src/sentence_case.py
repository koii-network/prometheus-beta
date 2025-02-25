def convert_to_sentence_case(text: str) -> str:
    """
    Convert a string to sentence case.
    
    Sentence case capitalizes the first non-whitespace character 
    and ensures other non-whitespace characters are lowercase 
    while preserving the original whitespace.
    
    Args:
        text (str): The input string to convert to sentence case.
    
    Returns:
        str: The input string converted to sentence case.
    
    Raises:
        TypeError: If the input is not a string.
    
    Examples:
        >>> convert_to_sentence_case("HELLO WORLD")
        'Hello world'
        >>> convert_to_sentence_case("hello WORLD")
        'Hello world'
        >>> convert_to_sentence_case("")
        ''
        >>> convert_to_sentence_case(" HELLO ")
        ' Hello '
    """
    # Check if input is a string
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    
    # Handle empty string case
    if not text:
        return text
    
    # Find the first non-whitespace character
    first_non_whitespace_chars = [(i, char) for i, char in enumerate(text) if not char.isspace()]
    
    # If no non-whitespace characters, return original string
    if not first_non_whitespace_chars:
        return text
    
    # Convert first non-whitespace character to uppercase
    first_non_ws_index, first_non_ws_char = first_non_whitespace_chars[0]
    modified_text = list(text)
    modified_text[first_non_ws_index] = first_non_ws_char.upper()
    
    # Convert other non-whitespace characters to lowercase
    for i, (idx, char) in enumerate(first_non_whitespace_chars[1:], start=1):
        modified_text[idx] = char.lower()
    
    return ''.join(modified_text)